import logging
import os


import jinja2

import time
from string import letters
import webapp2

from handlers.blogfront import BlogFront
from handlers.editpost import EditPost
from handlers.signup import Signup
from handlers.mainpage import MainPage
from handlers.postpage import PostPage
from handlers.newpost import NewPost
from handlers.newcomment import NewComment
from handlers.editcomment import EditComment
from handlers.deletecomment import DeleteComment
from handlers.deletepost import DeletePost
from handlers.votepost import VotePost
from handlers.login import Login
from handlers.logout import Logout
from models.user import User
        
class Register(Signup):
    def done(self):
        #make sure the user doesn't already exist
        u = User.by_name(self.username)
        if u:
            msg = 'That user already exists.'
            self.render('signup-form.html', error_username = msg)
        else:
            u = User.register(self.username, self.password, self.email)
            u.put()

            self.login(u)
            self.redirect('/blog')



app = webapp2.WSGIApplication([('/', MainPage),
                               ('/blog/?', BlogFront),
                               ('/blog/([0-9]+)', PostPage),
                               ('/blog/newpost', NewPost),
                               ('/blog/newcomment/([0-9]+)', NewComment),
                               ('/blog/editcomment/([0-9]+)', EditComment),
                               ('/blog/deletecomment/([0-9]+)', DeleteComment),
                               ('/blog/editpost/([0-9]+)', EditPost),
                               ('/blog/deletepost/([0-9]+)', DeletePost),
                               ('/blog/vote/([0-9]+)/([a-z]*)', VotePost),
                               ('/blog/vote/([0-9]+)', VotePost),
                               ('/signup', Register),
                               ('/login', Login),
                               ('/logout', Logout)
                               ],
                              debug=True)
