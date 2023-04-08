from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment

from .schema import AssignmentSchema, AssignmentGradeSchema

teacher_assignments_resources = Blueprint('teacher_assignments_resources', __name__)

@teacher_assignments_resources.route('/assignments', methods=['GET'], strict_slashes=False)
@decorators.auth_principal
def list_assignments(p):
    """Returns list of assignments"""
    teachers_assignments = Assignment.get_assignments_by_teacher(p.teacher_id)
    teachers_assignments_dump = AssignmentSchema().dump(teachers_assignments, many=True)
    return APIResponse.respond(data=teachers_assignments_dump)

@teacher_assignments_resources.route('/assignments/grade', methods=['POST'], strict_slashes=False)
@decorators.accept_payload
@decorators.auth_principal
def grade_assignment(p, incoming_payload):
    """grade an assignment"""
    graded_assignment_payload = AssignmentGradeSchema().load(incoming_payload)
    graded_assignment = Assignment.grader(
        _id=graded_assignment_payload.id,
        grade=graded_assignment_payload.grade,
        principal=p
    )
    db.session.commit()
    grade_assignment_dump = AssignmentSchema().dump(grade_assignment)
    return APIResponse.respond(data=grade_assignment_dump)
