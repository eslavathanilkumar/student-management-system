from flask import Blueprint, request, jsonify
from models.student_model import Student
from database import db

student_bp = Blueprint("student_bp", __name__)

# CREATE student
@student_bp.route("/students", methods=["POST"])
def add_student():
    data = request.json

    new_student = Student(
        name=data["name"],
        course=data["course"]
    )

    db.session.add(new_student)
    db.session.commit()

    return jsonify({"message": "Student added successfully"})

# GET students
@student_bp.route("/students", methods=["GET"])
def get_students():
    students = Student.query.all()

    result = []
    for s in students:
        result.append({
            "id": s.id,
            "name": s.name,
            "course": s.course
        })

    return jsonify(result)

# DELETE student
@student_bp.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    student = Student.query.get(id)

    if not student:
        return jsonify({"error": "Student not found"})

    db.session.delete(student)
    db.session.commit()

    return jsonify({"message": "Student deleted"})