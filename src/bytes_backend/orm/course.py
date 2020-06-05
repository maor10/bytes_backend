from typing import List

from mongoengine import Document, StringField, ListField, ReferenceField, BooleanField

from bytes_backend.orm.step import Step
from bytes_backend.orm.user import User


class CourseType:
    PYTHON = 'python'
    LINUX = 'linux'


class Course(Document):

    name = StringField()
    author = ReferenceField(User)
    course_type = StringField(choices=[CourseType.PYTHON, CourseType.LINUX])
    steps: List[Step] = ListField(ReferenceField(Step))

    enabled = BooleanField(default=True)

    def __repr__(self):
        return f'<{self.__class__.__name__} - {self.name}>'
