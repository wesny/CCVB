import Math

def isPopular (val,L):
    avg = calcAvg (L)
    std = stdev (L)
    if (val > avg + (2 * std)):
        return true
    else:
        return false
        
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
    std = Math.sqrt (varience)
    return std

# D3 + SVG
