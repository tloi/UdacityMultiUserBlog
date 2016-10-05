from bloghandler import BlogHandler
from helpers.render import post_exist

class NewComment(BlogHandler):
    def get(self,post_id):
        if self.user:
            post=post_exist(post_id)
            if post:
                self.render("newcomment.html", p=post)
            else:
                self.render("errorpost.html", error="Post does not exist")
        else:
            self.redirect("/login")

    def post(self,post_id):
        if not self.user:
            self.redirect('/blog')

        post=post_exist(post_id)
        if post:
            content = self.request.get('content')
            if content:
                c = Comment(parent = blog_key(), post_fk = post, content = content, created_by=self.user.name)
                c.put()
                self.redirect('/blog/%s' % str(post_id))
            else:
                error = "comment, please!"
                self.render("newcomment.html", p=post, error=error)
        else:
            self.render("errorpost.html", error="Post does not exist")
