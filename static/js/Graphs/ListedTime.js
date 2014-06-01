var retData = function (vals) {
    data = {
	"xScale": "ordinal",
	"yScale": "linear",
	"type": "line",
	"main": [
	    {
		"className": ".linked",
		"data": [] 
	    }
	]
    };

    for (i=0;i<vals.length;i++){
	myVal =  {
            "x": i ,
            "y": vals[i]
	};

	arr = data["main"][0]["data"]
	arr.push(myVal);
	data["main"][0]["data"] = arr;
    };
    return data;
};
