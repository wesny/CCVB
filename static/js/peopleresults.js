//People Results Script	
// InstagramEngTime
var InstagramEngTime = function (pics) {
	vals = pics["media_stats"]["eng_vals"]

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
	var IGEngvsTi = new xChart("line-dotted", data, "#IG-EngvsTi");
};

// TwitterEngTime
var TwitterEngTime = function (tweets) {
	vals = tweets["eng_vals"]

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
	console.log("twitterengtime")
	var TWEngvsTi = new xChart("line", data, "#TW-EngvsTi");
};

//InstragramLikesTime
var InstagramLikesTime = function (pics) {
	likes= pics["media_stats"]["likes_vals"];
	imgval = pics["media_stats"]["images"];
	textVal = pics["media_stats"]["text_vals"];
	console.log(textVal);
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

		arr = data["main"][0]["data"];
		arr.push(myVal);
		data["main"][0]["data"] = arr;
	};

	var opts = {
		"mouseover": function (d,i) {
			//txt = textVal[i];
			//var txtNd=document.createTextNode(txt);
			imageSRC = imgval[i];
			var imgNd = document.createElement('img');
			imgNd.src = imageSRC;
			//var br = document.createElement("br");

			document.getElementById("IG-LivsTi-dialog").appendChild(imgNd);
			//document.getElementById("IG-LivsTi-dialog").appendChild(br);
			//document.getElementById("IG-LivsTi-dialog").appendChild(txtNd);
			$( "#IG-LivsTi-dialog" ).dialog(); 
		},
		"mouseout": function (x,i) {
			$("#IG-LivsTi-dialog").dialog('close');
			document.getElementById("IG-LivsTi-dialog").innerHTML = "";

		},
	};
	var IGLivsTi = new xChart('line-dotted', data, '#IG-LivsTi', opts);
};

//TwitterRetFav
var TwitterRetFav = function (tweets) {
	favs = tweets["favorite_vals"]
	rets = tweets["retweet_vals"]
	textVal = tweets ["tweet_text"]    

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
	var TWRTvsFav = new xChart('line-dotted', data, '#TW-RTvsFav');
};
