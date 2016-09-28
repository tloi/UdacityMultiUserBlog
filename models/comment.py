class Post(db.Model):
    like_count=db.IntegerProperty(default=0)
    unlike_count=db.IntegerProperty(default=0)
    subject = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    created_by = db.TextProperty()
    last_modified = db.DateTimeProperty(auto_now = True)
    
    def render(self):        
        self._render_text = self.content.replace('\n', '<br>')
        return render_str("post.html", p = self)
