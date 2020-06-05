from bson import ObjectId
from flask import Blueprint

from bytes_backend.blueprints.courses.api_utils import serialize_step
from bytes_backend.decorators import bytes_response
from bytes_backend.orm.course import Course

courses_blueprint = Blueprint('courses', __name__)


@courses_blueprint.route('/')
@bytes_response(load_user=False)
def get_courses():
    return [{
        'id': str(course.id),
        'name': course.name
    } for course in Course.objects(enabled=True)]


@courses_blueprint.route('/<string:course_id>')
@bytes_response()
def get_course(user, course_id):
    course: Course = Course.objects.get(id=ObjectId(course_id))
    return {
        'id': str(course.id),
        'name': course.name,
        'steps': [
            serialize_step(step, course, user) for step in course.steps
        ]
    }
