class FBUser:

	def __init__(self, id = "default", pta = 0, likes = 0):
		self.id = id
		self.pta = pta
		self.likes = likes
		self.posts = []

	def add_post(self, post):
		self.posts.append(post)

	def avg_viral_reach(self):
		sum([(post.comments + post.likes + post.shares) / self.likes for post in self.posts])/float(len(self.posts))

class FBPost:

	def __init__(self, text = "No Text", comments = 0, likes = 0, shares = 0, picture = None, video = None, link = None):
		self.text = text
		self.comments = comments
		self.likes = likes
		self.shares = shares
		self.picture = picture
		self.video = video
		self.link = link

	def typeofpost(self):
		if self.picture:
			return "picture"
		elif self.video:
			return "video"
		elif self.link:
			return "link"
		else:
			return "text"


'''
	Test functions
'''
def main():
	post = FBPost("some text", 4, 6)
	print post.text
	print post.comments
	print post.likes

if __name__ == '__main__':
	main()