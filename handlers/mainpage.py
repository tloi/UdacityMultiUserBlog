from bloghandler import BlogHandler

class MainPage(BlogHandler):
  def get(self):
      self.redirect('blog')
