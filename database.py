from peewee import *

db = SqliteDatabase('blog.db')


class User(Model):
    username = CharField()
    firstname = CharField()
    lastname = CharField()
    email = CharField()

    class Meta:
        database = db


class Post(Model):
    title = CharField()
    body = CharField()
    published_date = DateField()
    user = ForeignKeyField(User, backref='posts')

    class Meta:
        database = db

db.connect()
db.create_tables([User, Post])