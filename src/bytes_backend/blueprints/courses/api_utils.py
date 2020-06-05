from mongoengine import DoesNotExist

from bytes_backend.orm.course import Course
from bytes_backend.orm.step import Step
from bytes_backend.orm.user import User
from bytes_backend.orm.user_course_step import UserCourseStep, UserCourseStepStatus


def serialize_step(step: Step, course: Course, user: User):
    try:
        user_course_step = UserCourseStep.objects.get(step=step, course=course, user=user)
        user_status = user_course_step.status
    except DoesNotExist:
        user_status = UserCourseStepStatus.DID_NOT_START

    return {
        'id': str(step.id),
        'name': step.name,
        'type': step.STEP_TYPE,
        'user_status': user_status
    }
