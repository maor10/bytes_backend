from mongoengine import Document, StringField


class User(Document):

    first_name = StringField()
    last_name = StringField()
