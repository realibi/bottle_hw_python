from bottle import request, route, run, template
from database import User, Post
import datetime


@route('/')
def index():
    return template('users', users = User.select())


@route('/createPost')
def createPost_view():
    return template('createPost')


@route('/blog')
def blog_view():
    return template('blog', posts = Post.select())  


@route('/createPost', method='post')
def createPost():
    nTitle = request.forms.get('title')
    nBody = request.forms.get('body')
    nDateTime = datetime.datetime.now()

    author = User.get(User.firstname == 'alibi')
    post = Post(title = nTitle, body = nBody, published_date = nDateTime, user = author)
    post.save()
    return template('blog', posts = Post.select())


@route('/signin', method="post")
def registration():
    nUsername = request.forms.get('username')
    nFirstname = request.forms.get('firstname')
    nLastname = request.forms.get('lastname')
    nEmail = request.forms.get('email')

    user = User(username = nUsername, firstname = nFirstname, lastname = nLastname, email = nEmail)
    user.save()


@route('/users')
def users_view():
    return template('users', users = User.select())


@route('/signin')
def registration_view():
    return template('register')


run(host='localhost', port=8080, debug=True)