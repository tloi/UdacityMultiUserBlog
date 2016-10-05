from bloghandler import BlogHandler

class UnlikePost(BlogHandler):
    def get(self, post_id):
        if self.user:
            p=post_exist(post_id)
            if p:
                if self.user.name==p.created_by:
                    error = "You cannot Unlike your own Post"
                    self.render("errorpost.html", p=p, error=error)
                else:
                    self.render("unlikepost.html", p=p)
            else:
                self.redirect("/blog")
        else:
            self.redirect("/login")

    def post(self,post_id):        
        post = post_exist(post_id)
        if post:
            if self.user.name==post.created_by:
                error = "You cannot unlike your own Post"
                self.render("errorpost.html", p=post, error=error)
            else:
                post.unlike_count+=1
                post.put()
                self.redirect('/blog/%s' % post_id)             
        else:
            self.redirect("/blog")
