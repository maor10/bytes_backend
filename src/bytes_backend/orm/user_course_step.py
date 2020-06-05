from mongoengine import Document, ReferenceField, StringField

from bytes_backend.orm.course import Course
from bytes_backend.orm.step import Step
from bytes_backend.orm.user import User


class UserCourseStepStatus:
    DID_NOT_START = 'did_not_start'
    STARTED = "started"
    COMPLETE = "complete"
    INCOMPLETE = 'incomplete'


class UserCourseStep(Document):

    meta = {
        'allow_inheritance': True
    }

    user = ReferenceField(User)
    course = ReferenceField(Course)
    step = ReferenceField(Step)
    status = StringField(choices=[UserCourseStepStatus.STARTED, UserCourseStepStatus.COMPLETE,
                                  UserCourseStepStatus.INCOMPLETE])
