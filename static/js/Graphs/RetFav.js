var retData = function (favs,rets,textVal) {
    
    tt = document.createElement('div'),
    leftOffset = -(~~$('html').css('padding-left').replace('px', '') + ~~$('body').css('margin-left').replace('px', '')),
    topOffset = 0;
    tt.className = 'ex-tooltip';
    document.body.appendChild(tt);

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

    for (i=0;i<favs.length;i++){
	myVal =  {
            "x": favs[i],
            "y": rets[i]
	};

	arr = data["main"][0]["data"]
	arr.push(myVal);
	data["main"][0]["data"] = arr;
    };

    var opts = {
	"mouseover": function (d,i) {
	    var pos = $(this).offset();
	    $(tt).text(textVal[i])
		.css({top: pos.top, left: pos.left })
		.show();
	},
	"mouseout": function (x) {
	    $(tt).hide();
	}
    };

    var myChart = new xChart('line-dotted', data, '#myChart', opts);
};
