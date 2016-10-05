from bloghandler import BlogHandler
from helpers.render import comment_exist

class EditComment(BlogHandler):
    def get(self, comment_id):
        if self.user:
            comment= comment_exist(comment_id)            
            if comment:
                if self.user.name!=comment.created_by:
                    error = "You cannot edit other user's comment"
                    self.render("errorcomment.html", c=comment, error=error)
                else:
                    self.render("editcomment.html", comment=comment)
            else:
                self.render("/blog")
        else:
            self.redirect("/login")

    def post(self,comment_id):
        comment= comment_exist(comment_id)       
        if not self.user:
            self.redirect('/blog')
        elif self.user.name!=comment.created_by:
            error = "You cannot edit other user's comment"
            self.render("editpost.html", comment=comment, error=error)
        else:
            post_id=comment.post_fk.key().id()
            comment.content = self.request.get('content')
        
            if comment.content:            
                comment.put()
                self.redirect('/blog/%s' % post_id)
            else:
                error = "comment, please!"
                self.render("editcomment.html", comment=comment, error=error)
