var retData = function (likes,textVal,imgval) {

    data = {
	"xScale": "linear",
	"yScale": "linear",
	"main": [
	    {
		"className": ".retfav",
		"data": [] 
	    }
	]
    };

    for (i=0;i<likes.length;i++){
	myVal =  {
            "x": i,
            "y": likes[i]
	};

	arr = data["main"][0]["data"]
	arr.push(myVal);
	data["main"][0]["data"] = arr;
    };

    var opts = {
	"mouseover": function (d,i) {
	    txt = textVal[i];
	    var txtNd=document.createTextNode(txt);
	    imageSRC = imgval[i];
	    var imgNd = document.createElement('img')
	    imgNd.src = imageSRC;
	    var br = document.createElement("br");

	    document.getElementById("dialog").appendChild(imgNd)
	    document.getElementById("dialog").appendChild(br)
	    document.getElementById("dialog").appendChild(txtNd);
	    $( "#dialog" ).dialog(); 
	},
	"mouseout": function (x,i) {
	    $("#dialog").dialog('close');
	    document.getElementById("dialog").innerHTML = "";
	    
	},
    };

    var myChart = new xChart('line-dotted', data, '#myChart', opts);
};
