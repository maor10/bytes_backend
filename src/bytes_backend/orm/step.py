from mongoengine import Document, StringField, ReferenceField

from bytes_backend.orm.user import User


class Step(Document):

    meta = {
        'allow_inheritance': True
    }

    STEP_TYPE = None

    name = StringField()
    author = ReferenceField(User)

    def __repr__(self):
        return f'<{self.__class__.__name__} - {self.name}>'


class VideoStep(Step):

    STEP_TYPE = 'video'

    url = StringField()


class ExerciseStep(Step):

    STEP_TYPE = 'exercise'
