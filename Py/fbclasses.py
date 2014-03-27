class FBUser:

	def __init__(self, id = "default", pta = 0, likes = 0):
		self.id = id
		self.pta = pta
		self.likes = likes
		self.posts = []

class FBPost:

	def __init__(self, text = "default text", comments = 0, likes = 0):
		self.text = text
		self.comments = comments
		self.likes = likes

def main():
	post = FBPost("some text", 4, 6)
	print post.text
	print post.comments
	print post.likes

if __name__ == '__main__':
	main()