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

var leftLink = document.createElement("form");
leftLink.setAttribute('action',"peopleresults");
var leftButton = document.createElement("input");
leftButton.setAttribute('type',"submit");
leftButton.setAttribute('value',"PEOPLE SEARCH");
leftLink.appendChild(leftButton);
var leftTextBox = document.createElement("input");
leftTextBox.setAttribute('type',"text");
leftLink.appendChild(document.createElement("br"));
leftLink.appendChild(document.createElement("br"));
leftLink.appendChild(leftTextBox);
leftDiv.appendChild(leftLink);


var rightLink = document.createElement("form");
//rightLink.setAttribute('action',"thingresults");
rightLink.setAttribute('class',"form-horizontal");
rightLink.setAttribute('role',"form");
rightLink.setAttribute('method',"POST");
var rightId = document.createElement("input");
rightId.setAttribute('name',"id");
rightId.setAttribute('type',"hidden");
rightId.setAttribute('value',"things");
var rightButton = document.createElement("input");
rightButton.setAttribute('type',"submit");
rightButton.setAttribute('value',"THINGS SEARCH");
rightLink.appendChild(rightButton);
var rightTextBox = document.createElement("input");
rightTextBox.setAttribute('type',"text");
rightTextBox.setAttribute('name',"word");
rightLink.appendChild(document.createElement("br"));
rightLink.appendChild(document.createElement("br"));
rightLink.appendChild(rightId);
rightLink.appendChild(rightTextBox);
rightDiv.appendChild(rightLink);

