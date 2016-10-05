from helpers.render import render_str
from google.appengine.ext import db
from models.post import Post

class Comment(db.Model):
    post_fk=db.ReferenceProperty(Post, collection_name='comments')        
    content = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    created_by = db.TextProperty()
    last_modified = db.DateTimeProperty(auto_now = True)
    
    def render(self):        
        self._render_text = self.content.replace('\n', '<br>')
        return render_str("comment.html", p = self)
