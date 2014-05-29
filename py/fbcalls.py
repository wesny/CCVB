import gevent.monkey; gevent.monkey.patch_all()
import json
from facebook import GraphAPI
import itertools
import gevent.pool
import gevent.queue
from fbclasses import FBUser

f = open('output.json','w')

graph = GraphAPI("1409088379353690|Y34Vq85nCHpqCsZRHCB8tygHYZs")

def grouper(n, iterable):
    it = iter(iterable)
    while True:
       chunk = tuple(itertools.islice(it, n))
       if not chunk:
           return
       yield chunk

def get_posts(id):
	r = graph.get_object("%s/posts" % id, fields='id', limit=5000)
	return r

def make_batch_string(idlist):
	returnl = []
	for id in idlist:
		returnl.append(make_call(id))
	return returnl	

def make_call(id):
	dict = {}
	dict["method"] = "GET"
	dict["relative_url"] = ("%s?fields=likes.limit(1).summary(true),comments.limit(1).summary(true),shares,created_time&limit=5000" % id).encode('ascii','ignore')
	return dict

def make_id_list(json):
	idlist = []
	for entry in json['data']:
		idlist.append(entry['id'])
	return idlist

def get_engag_data(string):
	return graph.request("", post_args = {"batch":string})

def create_engag_dict(data):
	l = []
	for post in data:
		x = json.loads(post['body'])
		y = {}
		y['likes'] = x['likes']['summary']['total_count']
		y['comments'] = x['comments']['summary']['total_count']
		y['shares'] = x['shares']['count']
		y['id'] = x['id']
		y['time'] = x['created_time']
		l.append(y)
	return l

def run_call(chunk, data_dicts):
	batched_requests = make_batch_string(chunk)
	data = graph.request("", post_args = {"batch":batched_requests})
	data_dicts.append(create_engag_dict(data))

def make_class(id):
	r = graph.get_object("%s" % id, fields='likes,talking_about_count', limit=5000)
	c = FBUser(id, r['talking_about_count'], r['likes'])
	return c

def pull_fb_data(id):
	data_dicts = []
	c = make_class(id)
	posts = get_posts(id)
	ids = make_id_list(posts)
	chunks = grouper(50, ids)
	threads = []
	for chunk in chunks:
		threads.append(gevent.spawn(run_call, chunk, data_dicts))
	gevent.joinall(threads)
	z = []
	for d in data_dicts:
		z += d
	data_dicts = z
	for d in data_dicts:
		c.add_post(likes = d['likes'], comments = d['comments'], shares = d['shares'], time = d['time'])
	return c
if __name__ == '__main__':
	c = pull_fb_data('barackobama')
