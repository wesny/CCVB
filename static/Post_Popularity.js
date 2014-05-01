var favorite_vals = {{ favorite_vals }};
// Graphs your posts to tell you how popular they have been using d3.js

var height=400, width=1000;
var yPadding=10;
var xPadding=40;

var svg = d3.select("body").append('svg')
    .attr('width',width)
    .attr('height',height)
    .attr('id','svg')
    .style('border','1px solid');

d1 = []

//favorite_vals = [1,2,3,4,5]
counter = 0;
for (val in favorite_vals) {
    d1.push ({
	'label':counter,
	'x':counter,
	'y':val
    })
    counter = counter + 1;
}

var yScale = d3.scale.linear()
	.domain([0, d3.max(d1,function(d){return d.y;}) ])
	.range([height,0]);

var xScale = d3.scale.linear()
    .domain([0, d3.max(d1,function(d){
	console.log (d.x);
	return d.x;}) ])
    .range([width,0]);

var c = svg.selectAll("circle")
    .data(d1)
    .enter()
    .append("circle")
    .attr('r',5)
    .attr('cx',function(d) {return xScale(d.x);})
    .attr('cy',function(d) {return yScale(d.y);})
    .attr('fill','steelblue');
