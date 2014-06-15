//People Results Script	
$('.button-group').each( function( i, buttonGroup ) {
	var $buttonGroup = $( buttonGroup );
	$buttonGroup.on( 'click', 'button', function() {
		$buttonGroup.find('.is-checked').removeClass('is-checked');
		$( this ).addClass('is-checked');
	});
});

// EngTime
var retData = function (vals) {
    data = {
	"xScale": "linear",
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

//InstragramLikesTime
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
//RetFav
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
	},
	"click": function(x,i) {
	    x = String(textVal[i]);
	    console.log(textVal[i]);
	    alert(x);
	}
    };

    var myChart = new xChart('line-dotted', data, '#myChart', opts);
};

//TweetsFavTime
var CalcTweets = function (favorite_vals,text_vals) {    
    console.log("here")
    window.onload = function () {
	document.getElementById("dialog").innerHTML = "";
    }

    var height=400, width=1500;
    var yPadding=10;
    var xPadding=40;

    var svg = d3.select("body").append('svg')
	.attr('width',width)
	.attr('height',height)
	.attr('id','svg')
	.style('border','1px solid')
    
    d1 = []
    

    for (i=0; i<favorite_vals.length; i++) {
	d1.push ({
	    'label':i,
	    'x':i,
	    'y':favorite_vals[i],
	    'text':text_vals[i]
	})
    }

    var yScale = d3.scale.linear()
	.domain([-2, d3.max(d1,function(d){return d.y;}) ])
	.range([height,0]);

    var xScale = d3.scale.linear()
	.domain([d3.max(d1,function(d){return d.x;})+20,-9 ])
	.range([width,0]);
    var yAxis = d3.svg.axis()
	.scale(yScale)
	.ticks(10)
	.orient('left')

    var xAxis = d3.svg.axis()
	.scale(xScale)
	.ticks(10)
	.orient('')

    svg.append("g")
	.attr('class','axis')
	.attr('transform','translate (25,0)')
	.call(yAxis);

    svg.append("g")
	.attr('class','axis')
	.attr('transform','translate (0,375)')
	.call(xAxis);

    var c = svg.selectAll("circle")
	.data(d1)
	.enter()
	.append("circle")
	.attr('r',5)
	.attr('cx',function(d) {return xScale (d.x);})
	.attr('cy',function(d) {return yScale (d.y);})
	.attr('fill','steelblue')

    $("#svg").on("mouseover", "circle", function(event){
	document.getElementById("dialog").innerHTML = "";

	xCor = this.cx.baseVal.value;
	xVal = Math.round(xScale.invert(xCor));
	txt = text_vals[xVal];
	var txtNd=document.createTextNode(txt);
	document.getElementById("dialog").appendChild(txtNd);
	$( "#dialog" ).dialog(); 
    });

    $("#svg").on("mouseout", "circle", function(event){
	$("#dialog").dialog('close');
    });

};

//RetweetsTime
var CalcTweets = function (retweet_vals,text_vals) {    
    console.log("here")
    window.onload = function () {
	document.getElementById("dialog").innerHTML = "";
    }

    var height=400, width=1500;
    var yPadding=10;
    var xPadding=40;

    var svg = d3.select("body").append('svg')
	.attr('width',width)
	.attr('height',height)
	.attr('id','svg')
	.style('border','1px solid')
    
    d1 = []
    

    for (i=0; i<retweet_vals.length; i++) {
	d1.push ({
	    'label':i,
	    'x':i,
	    'y':retweet_vals[i],
	    'text':text_vals[i]
	})
    }

    var yScale = d3.scale.linear()
	.domain([-2, d3.max(d1,function(d){return d.y;}) ])
	.range([height,0]);

    var xScale = d3.scale.linear()
	.domain([d3.max(d1,function(d){return d.x;})+20,-9 ])
	.range([width,0]);
    var yAxis = d3.svg.axis()
	.scale(yScale)
	.ticks(10)
	.orient('left')

    var xAxis = d3.svg.axis()
	.scale(xScale)
	.ticks(10)
	.orient('')

    svg.append("g")
	.attr('class','axis')
	.attr('transform','translate (25,0)')
	.call(yAxis);

    svg.append("g")
	.attr('class','axis')
	.attr('transform','translate (0,375)')
	.call(xAxis);

    var c = svg.selectAll("circle")
	.data(d1)
	.enter()
	.append("circle")
	.attr('r',5)
	.attr('cx',function(d) {return xScale (d.x);})
	.attr('cy',function(d) {return yScale (d.y);})
	.attr('fill','steelblue')

    $("#svg").on("mouseover", "circle", function(event){
	document.getElementById("dialog").innerHTML = "";

	xCor = this.cx.baseVal.value;
	xVal = Math.round(xScale.invert(xCor));
	txt = text_vals[xVal];
	var txtNd=document.createTextNode(txt);
	document.getElementById("dialog").appendChild(txtNd);
	$( "#dialog" ).dialog(); 
    });

    $("#svg").on("mouseout", "circle", function(event){
	$("#dialog").dialog('close');
    });

};

//TwitterReport
var DisplayProfile = function (data) { 
    name = data ["name"];
    loc = data ["location"];
    avg_favs = data["favorite_count"];
    avg_retweet = data["retweet_count"];
    most_popular_tweets = data["popularTweets"];
    proPic = data["profilePicture"];
    friends = data["friends_count"];
    followers = data["followers_count"];
    listed = data["listed_count"];
    description = data["description"];
    statusCount = data["statuses_count"];
}

var $container = $('.graphs').isotope({
	itemSelector: '.pgraph',
	layoutMode: 'masonry',
});