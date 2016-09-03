from mongoengine import *

# Create your models here.

class Event(Document):
    name = StringField(max_length=500)
    meta = {
        'indexes': [
            'name'
        ]
    }