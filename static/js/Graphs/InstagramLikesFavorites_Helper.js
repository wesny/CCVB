var getData = function (comments,likes,text) {
    var data = []
    console.log('runningFunction');
    
    for (i = 0;i<comments.length;i++) {
	info = {
	    'type': 1,
	    features:[likes[i],comments[i]],
	    'text':text
	};
	data.push(info);
    };
    return data;
};

var clickEvent = function (comments,likes,text) {
    console.log (likes);
    $("#svg").on("mouseover", "circle", function(event){
	document.getElementById("dialog").innerHTML = "";

	xCor = this.cx.baseVal.value;
	xVal = Math.round(xScale.invert(xCor));
	indx = likes.indexOf (xVal);
	txt = text[indx];
	var txtNd=document.createTextNode(txt);
	document.getElementById("dialog").appendChild(txtNd);
	$( "#dialog" ).dialog({dialogClass: "no-close"}); 
    });

    $("#svg").on("mouseout", "circle", function(event){
	$("#dialog").dialog('close');
    });

};
