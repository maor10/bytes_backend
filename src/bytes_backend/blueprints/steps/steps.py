from bson import ObjectId
from flask import Blueprint
from mongoengine import DoesNotExist

from bytes_backend.decorators import bytes_response
from bytes_backend.orm.course import Course
from bytes_backend.orm.step import Step
from bytes_backend.orm.user_course_step import UserCourseStep

steps_blueprint = Blueprint('steps', __name__)


@steps_blueprint.route('/<string:course_id>/<string:step_id>/complete', methods=['POST'])
@bytes_response()
def complete_video_step(user, course_id, step_id):
    course = Course.objects.get(id=ObjectId(course_id))
    step = Step.objects.get(id=ObjectId(step_id))
    try:
        user_course_step = UserCourseStep.objects.get(user=user, course=course, step=step)
    except DoesNotExist:
        user_course_step = UserCourseStep(user=user, course=course, step=step).save()
    return str(user_course_step.id)
