from bloghandler import BlogHandler
from helpers.render import post_exist
from helpers.render import vote_exist
from google.appengine.ext import db
from models.vote import Vote

class LikePost(BlogHandler):
    def get(self, post_id):
        if self.user:
            p=post_exist(post_id)
            v=vote_exist(post_id,self.user.name)
            if p:
                if self.user.name==p.created_by:
                    error = "You cannot Like your own Post"
                    self.render("errorpost.html", p=p, error=error)
                elif v:
                    error = "You have already voted"
                    self.render("errorpost.html", p=p, error=error)
                else:
                    self.render("likepost.html", p=p)
            else:
                self.redirect("/blog")
        else:
            self.redirect("/login")

    def post(self,post_id):
        post=post_exist(post_id)
        v=vote_exist(post_id,self.user.name)
        if post:
            if self.user.name==post.created_by:
                error = "You cannot Like your own Post"
                self.render("errorpost.html", p=post, error=error)
            elif v:
                error = "You have already voted"
                self.render("errorpost.html", p=p, error=error)
            else:
                v = Vote(parent = blog_key(), user_fk = user, post_fk=post, content="Like")
                v.put()
                self.redirect('/blog/%s' % post_id)
        else:
            self.redirect("/blog")
