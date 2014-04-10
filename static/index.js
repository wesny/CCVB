var s = document.getElementById("svg");
var title = document.createElement("h1");
var fullDiv = document.getElementById("full-div");
var leftDiv = document.getElementById("left-div");
var rightDiv = document.getElementById("right-div");
var foreign = document.getElementById("foreign");
title.appendChild(document.createTextNode("Socialpedia"));
title.setAttribute('class',"center");
foreign.insertBefore(title, fullDiv);


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
rightLink.setAttribute('action',"thingresults");
var rightButton = document.createElement("input");
rightButton.setAttribute('type',"submit");
rightButton.setAttribute('value',"THINGS SEARCH");
rightLink.appendChild(rightButton);
var rightTextBox = document.createElement("input");
rightTextBox.setAttribute('type',"text");
rightLink.appendChild(document.createElement("br"));
rightLink.appendChild(document.createElement("br"));
rightLink.appendChild(rightTextBox);
rightDiv.appendChild(rightLink);