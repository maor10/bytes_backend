from mongoengine import Document, StringField, BooleanField


class User(Document):

    first_name = StringField()
    last_name = StringField()
    anonymous = BooleanField(default=True)
