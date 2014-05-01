// Graphs your posts to tell you how popular they have been using d3.js

var height=400, width=400;
var yPadding=10;
var xPadding=40;

var svg = d3.select("body").append('svg')
	.attr('width',width)
	.attr('height',height)
	.attr('id','svg')
	.style('border','solid px');

d3_array  = []

favorite_vals = [1,2,3,4,5]
for val in favorite_vals {
    d3_array.append {
	'x':favorite_vals.indexOf(val),
	'y':val,
	'label':favorite_vals.indexOf(val)
    }   
}

var c = svg.selectAll("circle")
	.data(d3_array)
	.enter()
	.append("circle")
	.attr('r',10)
	.attr('cx',function(d) { return d3_array.x;})
	.attr('cy',d3_array.y)
	.attr('fill','steelblue');

