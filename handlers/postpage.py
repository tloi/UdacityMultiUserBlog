import logging
from bloghandler import BlogHandler
from google.appengine.ext import db
from helpers.render import blog_key
from models.comment import Comment
from models.vote import Vote

class PostPage(BlogHandler):
    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)        
        if not post:
            self.error(404)
            return
        comments=Comment.all().filter('post_fk =',post.key()).order('-created')      
        likes=db.GqlQuery("select * from Vote where post_id_fk="+post_id+" and content='Like'")
        unlikes=db.GqlQuery("select * from Vote where post_id_fk="+post_id+" and content='Unlike'")
        likecount=str(likes.count())
        unlikecount=str(unlikes.count())
        logging.info("test: "+likecount)
        self.render("permalink.html", post = post, comments=comments,likecount=likecount,unlikecount=unlikecount)
