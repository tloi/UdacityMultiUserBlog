import os
import jinja2
import re
from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), '../templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

secret = 'fart'

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

def make_secure_val(val):
    return '%s|%s' % (val, hmac.new(secret, val).hexdigest())

def check_secure_val(secure_val):
    val = secure_val.split('|')[0]
    if secure_val == make_secure_val(val):
        return val


USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE  = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    return not email or EMAIL_RE.match(email)

def blog_key(name = 'default'):
    return db.Key.from_path('blogs', name)

def comment_exist(comment_id):
    key = db.Key.from_path('Comment', int(comment_id), parent=blog_key())
    if key:
        comment = db.get(key)
        return comment
    else:
        return None    

def post_exist(post_id):
    key = db.Key.from_path('Post', int(post_id), parent=blog_key())
    if key:
        post = db.get(key)
        return post
    else:
        return None

def vote_exist(post_id, username):
    vote=db.GqlQuery("Select * from Vote where post_id_fk="+post_id+" and username_fk='"+username+"'")
    if vote:       
        return vote
    else:
        return None
