from bloghandler import BlogHandler
from models.post import Post

class BlogFront(BlogHandler):
    def get(self):        
        posts = Post.all().order('-created')
        self.render('front.html', posts = posts)
