var s = document.getElementById("svg");
var topDiv = document.getElementById("top-div");
var fullDiv = document.getElementById("full-div");
var leftDiv = document.getElementById("left-div");
var rightDiv = document.getElementById("right-div");
var foreign = document.getElementById("foreign");
var width = document.body.clientWidth;

/*
var topBox = document.createElementNS("http://www.w3.org/2000/svg","rect");
topBox.setAttribute('x', width / 2 - 207);
topBox.setAttribute('y', '15px');
topBox.setAttribute('width', "414px");
topBox.setAttribute('height',75);
topBox.setAttribute('rx', 10);
topBox.setAttribute('ry', 10);
topBox.setAttribute('fill', '#eeeeff');
topBox.setAttribute('stroke', '#d0d0ff');
topBox.setAttribute('id','topBox');
s.appendChild(topBox);
*/

var leftSide = document.createElementNS("http://www.w3.org/2000/svg","rect");
leftSide.setAttribute('x', width / 4 - 200.5);
leftSide.setAttribute('y', 120);
leftSide.setAttribute('width', "401px");
leftSide.setAttribute('height',500);
leftSide.setAttribute('rx', 10);
leftSide.setAttribute('ry', 10);
leftSide.setAttribute('fill', '#eeeeff');
leftSide.setAttribute('stroke', '#d0d0ff');
leftSide.setAttribute('id','leftSide');
s.appendChild(leftSide);

var rightSide = document.createElementNS("http://www.w3.org/2000/svg","rect");
rightSide.setAttribute('x', width * 3 / 4 - 200.5);
rightSide.setAttribute('y', 120);
rightSide.setAttribute('width', "401px");
rightSide.setAttribute('height', 500);
rightSide.setAttribute('rx', 10);
rightSide.setAttribute('ry', 10);
rightSide.setAttribute('fill', '#eeeeff');
rightSide.setAttribute('stroke', '#d0d0ff');
rightSide.setAttribute('id','rightSide');
s.appendChild(rightSide);


topDiv.addEventListener('mouseover', function(e) {
    d3.selectAll('#left-div').transition().duration(350).style('opacity',1);
    d3.selectAll('#right-div').transition().duration(350).style('opacity',1);
});

rightDiv.addEventListener('mouseover', function(e) {
    d3.selectAll('#left-div').transition().duration(350).style('opacity',0.2);
    d3.selectAll('#right-div').transition().duration(350).style('opacity',1);
});

leftDiv.addEventListener('mouseover', function(e) {
    d3.selectAll('#left-div').transition().duration(350).style('opacity',1);
    d3.selectAll('#right-div').transition().duration(350).style('opacity',0.2);
});



