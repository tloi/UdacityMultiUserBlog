from bloghandler import BlogHandler
from helpers.render import post_exist

class EditPost(BlogHandler):
    def get(self, post_id):
        if self.user:
            post= post_exist(post_id)            
            if post:
                if self.user.name!=post.created_by:
                    error = "You cannot edit other user's Post"
                    self.render("errorpost.html", p=post, error=error)
                else:
                    self.render("editpost.html", post=post)
            else:
                self.render("/blog")
        else:
            self.redirect("/login")

    def post(self,post_id):
        post= post_exist(post_id)       
        if not self.user:
            self.redirect('/blog')
        elif self.user.name!=post.created_by:
            error = "You cannot edit other user's Post"
            self.render("editpost.html", post=post, error=error)
        else:
            post.subject = self.request.get('subject')
            post.content = self.request.get('content')
        
            if post.subject and post.content:            
                post.put()
                self.redirect('/blog/%s' % post_id)
            else:
                error = "subject and content, please!"
                self.render("editpost.html", post=post, error=error)
