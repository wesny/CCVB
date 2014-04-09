import json
from facebook import GraphAPI

f = open('output.json', 'w')
graph = GraphAPI("1409088379353690|Y34Vq85nCHpqCsZRHCB8tygHYZs")

def make_call(id):
	dict = {}
	dict["method"] = "GET"
	dict["relative_url"] = "%s?fields=likes.limit(1).summary(true),comments.limit(1).summary(true),shares&limit=5000" % id
	return dict

def make_batch_string(json):
	returnl = []
	entries = json['data']
	for entry in entries:
		returnl.append(make_call(entry['id']))
	print str(returnl)
	return returnl

def get_posts(id):
	r = graph.get_object("barackobama/posts", fields='id')
	return r

posts = get_posts("barackobama")

batched_requests = make_batch_string(posts)
data = graph.request("", post_args = {"batch":batched_requests})
x = json.loads(data[1]['body'])
f.write(json.dumps(x, sort_keys=True, indent=4, separators=(',', ': ')))

f.close()

"""
Notes:

/barackobama/posts?fields=id : returns a list of ids







"""