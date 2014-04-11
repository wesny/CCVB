import json
from facebook import GraphAPI

f = open('output.json','w')

graph = GraphAPI("1409088379353690|Y34Vq85nCHpqCsZRHCB8tygHYZs")

def make_call(id):
	dict = {}
	dict["method"] = "GET"
	dict["relative_url"] = ("%s?fields=likes.limit(1).summary(true),comments.limit(1).summary(true),shares&limit=5000" % id).encode('ascii','ignore')
	return dict

def make_batch_string(json):
	returnl = []
	entries = json['data']
	for entry in entries:
		returnl.append(make_call(entry['id']))
	return returnl

def get_posts(id):
	r = graph.get_object("%s/posts" % id, fields='id', limit=50)
	return r

def create_engag_dict(data):
	d = {}
	for post in data:
		x = json.loads(post['body'])
		y = {}
		y['likes'] = x['likes']['summary']['total_count']
		y['comments'] = x['comments']['summary']['total_count']
		y['shares'] = x['shares']['count']
		d[x['id']] = y
	return d

posts = get_posts("barackobama")

batched_requests = make_batch_string(posts)
data = graph.request("", post_args = {"batch":batched_requests})
print create_engag_dict(data)
f.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))