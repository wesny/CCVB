import math

def isPopular (val,L):
    avg = calcAvg (L)
    std = stdev (L)
    if (val > avg + (2 * std)):
        return True
    else:
        return False
        
def calcAvg (L):
    x = sum (L)
    avg = x / len (L)
    return avg

def stdev (L):
    avg = calcAvg (L);
    SqauredDifference = 0
    for a in L:
        val = a - avg
        valSq = val * val
        SqauredDifference = SqauredDifference + valSq
    varience = SqauredDifference / len (L)
    std = math.sqrt (varience)
    return std

# D3 + SVG
