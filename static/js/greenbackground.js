var s = document.getElementById('svg');
var foreign = document.getElementById('foreign');

var makeBackground = function() {
    width = parseInt(document.width);
    height = parseInt(document.height);
    
    var rects = s.getElementsByTagName('rect');
    var len = rects.length
    var leftSide = document.getElementById('leftSide'); 
    var rightSide = document.getElementById('rightSide');
    for(var i = 0; i < len; i++) {
	rects[0].parentNode.removeChild(rects[0]);
    }
    
    for(var i = 0; i < 150; i++) {
	var randpixel = document.createElementNS("http://www.w3.org/2000/svg","rect");
	var dimension = Math.random() * 10 + 1;
	randpixel.setAttribute('x',Math.random() * width);
	randpixel.setAttribute('y',Math.random() * height);
	randpixel.setAttribute('width',dimension);
	randpixel.setAttribute('height',dimension);
	randpixel.setAttribute('fill','#7aff85');
	s.appendChild(randpixel);
	
	var randpixel2 = document.createElementNS("http://www.w3.org/2000/svg","rect");
	var dimension2 = Math.random() * 10 + 1;
	randpixel2.setAttribute('x',Math.random() * width);
	randpixel2.setAttribute('y',Math.random() * height);
	randpixel2.setAttribute('width',dimension2);
	randpixel2.setAttribute('height',dimension2);
	randpixel2.setAttribute('fill','#baffc0');
	s.appendChild(randpixel2);
	
	var randpixel3 = document.createElementNS("http://www.w3.org/2000/svg","rect");
	var dimension3 = Math.random() * 10 + 1;
	randpixel3.setAttribute('x',Math.random() * width);
	randpixel3.setAttribute('y',Math.random() * height);
	randpixel3.setAttribute('width',dimension3);
	randpixel3.setAttribute('height',dimension3);
	randpixel3.setAttribute('fill','#9effa6');
	s.appendChild(randpixel3);
    }
    
    if (leftSide != null) {
	s.appendChild(leftSide);
	s.appendChild(rightSide);
    }
   
    s.appendChild(foreign);
}


window.onresize = makeBackground;
makeBackground();
