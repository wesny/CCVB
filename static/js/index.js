var s = document.getElementById("svg");
var title = document.createElement("h1");
var fullDiv = document.getElementById("full-div");
var leftDiv = document.getElementById("left-div");
var rightDiv = document.getElementById("right-div");
var foreign = document.getElementById("foreign");
title.appendChild(document.createTextNode("Socialpedia"));
title.setAttribute('class',"center");
foreign.insertBefore(title, fullDiv);


var leftSide = document.createElementNS("http://www.w3.org/2000/svg","rect");
leftSide.setAttribute('x', "10%");
leftSide.setAttribute('y', 100);
leftSide.setAttribute('width', "30%");
leftSide.setAttribute('height',500);
leftSide.setAttribute('rx', 10);
leftSide.setAttribute('ry', 10);
leftSide.setAttribute('fill', '#eeffee');
leftSide.setAttribute('id','leftSide');
s.appendChild(leftSide);

var rightSide = document.createElementNS("http://www.w3.org/2000/svg","rect");
rightSide.setAttribute('x', "60%");
rightSide.setAttribute('y', 100);
rightSide.setAttribute('width', "30%");
rightSide.setAttribute('height', 500);
rightSide.setAttribute('rx', 10);
rightSide.setAttribute('ry', 10);
rightSide.setAttribute('fill', '#eeffee');
rightSide.setAttribute('id','rightSide');
s.appendChild(rightSide);



//rightDiv.addEventListener('mouseover', function(e) {
//    leftDiv.style.opacity = "0.2";
//    rightDiv.style.opacity = "1";
//});

//leftDiv.addEventListener('mouseover', function(e) {
//    rightDiv.style.opacity = "0.2";
//    leftDiv.style.opacity = "1";
//});

