from helpers.render import render_str
from google.appengine.ext import db
from post import Post
from user import User

class Vote(db.Model):
    post_id_fk=db.IntegerProperty(required=True)        
    username_fk=db.StringProperty(required=True)
    content = db.StringProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    
