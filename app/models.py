import datetime
from app import db

class Verb(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    body = db.StringField(required=True, unique=True)

    meta = {
            'allow_inheritance': True,
            'indexes': ['-created_at'],
            'ordering': ['-created_at']
    }

class Noun(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    body = db.StringField(required=True, unique=True)

    meta = {
            'allow_inheritance': True,
            'indexes': ['-created_at'],
            'ordering': ['-created_at']
    }

class Adjective(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    body = db.StringField(required=True, unique=True)

    meta = {
            'allow_inheritance': True,
            'indexes': ['-created_at'],
            'ordering': ['-created_at']
    }

class Adverb(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    body = db.StringField(required=True, unique=True)

    meta = {
            'allow_inheritance': True,
            'indexes': ['-created_at'],
            'ordering': ['-created_at']
    }
