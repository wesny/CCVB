//console.log ("Hello");

// Goal: Organize JennaMarbles (example person) recent Instragram data to plot the relationship between likes and comment for recent posts.
// The data is pulled from Instragram.py in CCVB (part of my final project)
// Likes are on the x axis, comments are on the y axis
// Yellow dots means that a photo has many comments but not many likes. 
// Blue dots are photos that have many comments and many likes. 


// To do: ACTUALLY INTEGRATE THE RENDERING OF THE TEMPLATE


comments = [415, 275, 496, 189, 398, 891, 291, 191, 3905, 664, 215, 182, 843, 219, 928, 1126, 388, 1938, 721];
likes = [80486, 85200, 54743, 70347, 102690, 123706, 94333, 68220, 115956, 112922, 83915, 80831, 86108, 68110, 76722, 133625, 81875, 115434, 127126];
text = ['About to go to sleep and the mosquito netting on my bed in Bali totally just reminded me that I begged my mom for a canopy bed for years when I was little. I basically just wanted to live in a tent. Childhood dream accomplished \U0001f338\U0001f33a\U0001f33c',
	'Full ass flight. We were laughing cuz we almost got this crazy lady in the picture that just keeps walking around not paying attention to the fact that we are about to take off or anything like that. Get it together lady lol.', 
	"I'm so incredibly sad to leave Singapore, it was one of the most amazing experiences I have ever had. You guys are some of the kindest people I have ever met. We are off to Bali to hang out with some monkeys and then next weekend I'll see everyone at #ytff in Sydney! Weeee", 
	'I also got to meet @apldeap yesterday, this dude is happy as fuck all the time!', 
	'From yesterday at #ytff. Zero fucks were given in Singapore and I said all the swear words on stage \U0001f602\U0001f602 my bad.', 
	'Hi my name is Jenna Marbles and I flew across the world and was hoping to see my friend @notryanhiga have you seen him?', 
	"And to those of you that threw all the stuff on stage at me (\U0001f602\U0001f602lol) don't worry I got your stuff too. Love all of you.", 
	'Thank you so much to all of you that waited in line for hours today to meet me, I had such a wonderful time hugging all of you. Singapore you are amazing and your gifts are so incredible! Imma find you on twitter for real and hunt you all down \U0001f49e\U0001f49e thank you for such a spectacular day.', 
	'\U0001f602\U0001f602 where are you!?', 
	'Admiring Singapore \U0001f49e', 
	'Lol @romemcdud the view is behind you \U0001f602\U0001f602', 
	'Just a couple of goyles in a boat in the sky \U0001f602\U0001f602 nice view thanks rain. 1+rain = wet @romemcdud', 
	"Kermie Worm and the little toys I got for him and Marbles in Tokyo. The one on the left I almost died laughing at, he's like a cat squirrel with cuddle fish fins for legs \U0001f602\U0001f602 WAT IS IT", 
	'I found a little paper Marbles!', 
	'Toilet in the Tokyo airport. For all the times you want some music to play while you flush.', 
	'Look who got a new backpack.', 
	'#tbt @kym_nguyen (the girl in the middle) used to always take pictures of us and I went through like a year phase where I was on a mission to ruin every single one of them. I REGRET NOTHING. Lol', 
	'\U0001f602\U0001f602\U0001f602', 
	"My cool Elsa hair from my What Disney Videos Taught Me Part 2 video I just uploaded. So princessy and weird to braid inside out. This is some complicated hair to replicate boo, jeeze can't you just have a ponytail."];

width = 400;
height = 400;

var data;
info = new Array(comments.length);

for (i=0;i<comments.length;i++){
    info[i] = [comments[i],likes[i],text[i]];
};

var data = _.map(info, function(d) {
    return {'type':1,
	    'realtype':1,
	    'features':[d[0],d[1],d[2]]}
});
    
console.log(data);

var xMin = d3.min(data,function(d){return d.features[0];});
var xMax = d3.max(data,function(d){return d.features[0];});
var yMin = d3.min(data,function(d){return d.features[1];});
var yMax = d3.max(data,function(d){return d.features[1];});

xScale = d3.scale.linear()
    .domain([xMin,xMax])
    .range([20,width-20]);
yScale = d3.scale.linear()
    .domain([yMin,yMax])
    .range([20,height-20]);

centroids = [data [0],data [1], data [2]];
centroidColors= ['green','blue','yellow'];

var svg = d3.select('body')
    .append('svg')
    .attr('id','svg')
    .attr('height',height)
    .attr('width',width)
    .style('border','solid 1px');

var items  = svg.selectAll('item')
    .data(data)
    .enter()
    .append('circle')
    .attr('class','item')
    .attr('r',5)
    .attr('cx',function(d) {return xScale(d.features[0]);})
    .attr('cy',function(d) {return yScale(d.features[1]);})
    .attr('fill','red');

var centroidCircles = svg.selectAll('centroid')
    .data(centroids)
    .enter()
    .append('circle')
    .attr('class','centroid')
    .attr('r',5)
    .attr('cx',function(d) {return xScale(d.features[0]);})
    .attr('cy',function(d) {return yScale(d.features[1]);})
    .attr('fill',function(d,i){return centroidColors[i]});


var dist = function(a,b){
    return _.reduce(_.map(_.zip(a,b),function(d) {return (d[0]-d[1])*(d[0]-d[1]);}),
		    function(a,b) {return a+b;},0);
}

var assign = function(centroids,data) {
    _.each(data,function(d) {
	var mins = _.map(centroids,function(d2){
	    return dist(d2.features,d.features);
	});
	var min = _.min(mins);
	var minIndex = _.indexOf(mins,min);
	d['type'] = minIndex;
    });
}

var recenter = function(centroids,data) {
    _.each(centroids,function(d,i,c){

	var subset = _.filter(data,function(d2){
	    return d.type==d2.type;
	});
	subset = _.map(subset,function(d) 
		       {return d.features;});
	var z = _.zip(subset);
	
	var sums = _.map(z,function(d){
	    return _.reduce(d,function(a,b){return a+b;});
	});
	var avgs = _.map(sums,function(d,i){
	    return parseInt(d)/z[i].length;
	});
	
	c[i].features = avgs;
    });
}

var clusterit = function() {
    assign(centroids,data);
    
    items
	.transition()
	.attr('stroke-width',3)
	.attr('stroke',function(d) {return centroidColors[d.type]; });

    recenter(centroids,data);
    
    centroidCircles
	.data(centroids)
	.transition()
	.delay(function(d,i){return 1000*i;})
	.duration(3000)
	.attr('cx',function(d){return xScale(d.features[0]);})
	.attr('cy',function(d){return yScale(d.features[1]);})
    }



//var setup = d3.select("#setup").on('click',doit);
var clickme = d3.select("#clickme").on('click', clusterit);
//var bd = d3.select("#build").on('click', build);
