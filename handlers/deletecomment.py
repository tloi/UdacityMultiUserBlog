from bloghandler import BlogHandler
from helpers.render import comment_exist
class DeleteComment(BlogHandler):
    def get(self, comment_id):
        if self.user:
            comment=comment_exist(comment_id)
            if comment:
                if self.user.name!=comment.created_by:
                    error = "You cannot delete other user's comment"
                    self.render("errorcomment.html", c=comment, error=error)
                else:
                    self.render("deletecomment.html", comment=comment)
            else:
                self.render("errorcomment.html",error="comment does not exist")
        else:
            self.redirect("/login")

    def post(self,comment_id):
        comment = comment_exist(comment_id)
        post_id=comment.post_fk.key().id()
        if not self.user:
            self.redirect('/blog')
        elif not comment.created_by:
            comment.delete()
            self.redirect('/blog/%s' % post_id)       
        elif self.user.name!=comment.created_by:
            self.render("deletecomment.html", comment=comment,error="You cannot delete other user's comment")
        else:        
            comment.delete()
            self.redirect('/blog/%s' % post_id)
