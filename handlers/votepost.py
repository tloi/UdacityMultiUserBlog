import logging
from bloghandler import BlogHandler
from helpers.render import post_exist, blog_key
from helpers.render import vote_exist
from google.appengine.ext import db
from models.vote import Vote

class VotePost(BlogHandler):
    def get(self, post_id,vote_default):
        if not vote_default:
            vote_default="votepost"
        if self.user:
            p=post_exist(post_id)
            v=vote_exist(post_id,self.user.name)
            if p:
                if self.user.name==p.created_by:
                    error = "You cannot Like your own Post"
                    self.render("errorpost.html", p=p, error=error)
                elif v.count()>0:                                        
                    error = "You have already voted" 
                    self.render("errorpost.html", p=p, error=error)
                else:
                    self.render(vote_default+".html", p=p)
            else:
                self.redirect("/blog")
        else:
            self.redirect("/login")

    def post(self,post_id,vote_default):
        post=post_exist(post_id)
        v=vote_exist(post_id,self.user.name)
        voteresult=self.request.get('voteresult')
        if not vote_default:
            vote_default="votepost"
        if post:
            if self.user.name==post.created_by:
                error = "You cannot Like your own Post"
                self.render("errorpost.html", p=post, error=error)
            elif v.count()>0:
                error = "You have already voted"
                self.render("errorpost.html", p=post, error=error)
            elif not voteresult:
                error = "You did not vote"+voteresult
                self.render(vote_default+".html", p=post, error=error)
            else:
                v = Vote(parent = blog_key(), username_fk = self.user.name, post_id_fk=int(post_id), content= voteresult)
                v.put()
                self.redirect('/blog/%s' % post_id)
        else:
            self.redirect("/blog")
