var s = document.getElementById('svg');
var foreign = document.getElementById('foreign');

var makeBackground = function() {
    var width = parseInt(document.body.clientWidth);
    var height = parseInt(document.body.clientHeight);
    
    var circles = s.getElementsByTagName('circle');
    var lines = s.getElementsByTagName('line');
    var len = circles.length
    
    for(var i = 0; i < len; i++) {
	circles[0].parentNode.removeChild(circles[0]);
    }
    len = lines.length;
    for(var i = 0; i < len; i++) {
	lines[0].parentNode.removeChild(lines[0]);
    }

    var newCircles = [];
    
    for(var i = 0; i < 100; i++) {
	var randpixel = document.createElementNS("http://www.w3.org/2000/svg","circle");
	var dimension = Math.random() * 2 + 5;
	randpixel.setAttribute('cx',Math.random() * width * 1.5 - width * .25);
	randpixel.setAttribute('cy',Math.random() * height * 1.5 - height * .25);
	randpixel.setAttribute('r',dimension);
	randpixel.setAttribute('fill','#6a55ff');
	
	newCircles.push(randpixel);
	
	var randpixel2 = document.createElementNS("http://www.w3.org/2000/svg","circle");
	var dimension2 = Math.random() * 2 + 5;
	randpixel2.setAttribute('cx',Math.random() * width * 1.5 - width * .25);
	randpixel2.setAttribute('cy',Math.random() * height * 1.5 - height * .25);
	randpixel2.setAttribute('r',dimension2);
	randpixel2.setAttribute('fill','#5a70ff');

	newCircles.push(randpixel2);
	
	var randpixel3 = document.createElementNS("http://www.w3.org/2000/svg","circle");
	var dimension3 = Math.random() * 2 + 5;
	randpixel3.setAttribute('cx',Math.random() * width * 1.5 - width * .25);
	randpixel3.setAttribute('cy',Math.random() * height * 1.5 - height * .25);
	randpixel3.setAttribute('r',dimension3);
	randpixel3.setAttribute('fill','#5e86ff');

	newCircles.push(randpixel3);
    }
    

    for(var i = 0; i < newCircles.length; i++){
	var xcoord = newCircles[i].getAttribute('cx');
	var ycoord = newCircles[i].getAttribute('cy');
	var dists = _.map(newCircles, function(d,i) {
	    return [Math.sqrt(Math.pow(xcoord - d.getAttribute('cx'),2) +
			     Math.pow(ycoord - d.getAttribute('cy'),2)),i];
	    });

	var neighbors = _.filter(dists, function(d) {
	    return d[0] < 200 && d[1] != i;});


	var skipRate = 1 / j;

	for(var j = 0; j < neighbors.length && j < 4; j++) {
	    if(j != 0 && Math.random() > skipRate) {
		continue;
	    }
	    
	    var newline = document.createElementNS("http://www.w3.org/2000/svg","line");
	    newline.setAttribute('x1',xcoord);
	    newline.setAttribute('y1',ycoord);
	    newline.setAttribute('x2',newCircles[neighbors[j][1]].getAttribute('cx'));
	    newline.setAttribute('y2',newCircles[neighbors[j][1]].getAttribute('cy'));
	  
	    newline.setAttribute('stroke-width',1);
	    newline.setAttribute('stroke','#8888ff');
	    s.appendChild(newline);
	}
    }

    for(var i = 0; i < newCircles.length; i++) {
	s.appendChild(newCircles[i]);
    }
    
    var leftSide = document.getElementById('leftSide'); 
    var rightSide = document.getElementById('rightSide');
    var topBox = document.getElementById('topBox');

    if (leftSide != null) {
	s.appendChild(leftSide);
	s.appendChild(rightSide);
	s.appendChild(topBox);
    }
   
    s.appendChild(foreign);
}


window.onresize = makeBackground;
makeBackground();
