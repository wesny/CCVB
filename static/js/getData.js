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
