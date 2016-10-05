from bloghandler import BlogHandler
from helpers.render import post_exist

class DeletePost(BlogHandler):
    def get(self, post_id):
        if self.user:
            post=post_exist(post_id)
            if post:
                if self.user.name!=post.created_by:
                    error = "You cannot delete other user's Post"
                    self.render("errorpost.html", p=post, error=error)
                else:
                    self.render("deletepost.html", post=post)
            else:
                self.redirect("/blog")
        else:
            self.redirect("/login")

    def post(self,post_id):
        post = post_exist(post_id)
        if not self.user:
            self.redirect('/blog')
        elif not post.created_by:
            post.delete()
            self.redirect('/blog')       
        elif self.user.name!=post.created_by:
            self.render("deletepost.html", post=post,error="You cannot delete other user's post")
        else:        
            post.delete()
            self.redirect('/blog')
