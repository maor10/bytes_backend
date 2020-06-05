from mongoengine import connect


def connect_to_db():
    connect('bytes')
