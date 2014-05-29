import json

def createjson_fbpost_commentsvslikes(user):
	j = {}
	for post in user.posts:
		j['className'] = ".posts"
		j['data'] = []
		d = j['data']
		d.append({"x":post.likes, "y":post.comments})
	return j

def createjson_fbpost_likessvstime(user):
	j = {}
	for post in user.posts:
		j['className'] = ".posts"
		j['data'] = []
		d = j['data']
		d.append({"x":post.time, "y":post.likes})
	return json.dumps([].append(j))