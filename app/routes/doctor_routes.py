from flask import Blueprint, request, jsonify, render_template
from models.doctor import Doctor

doctor_bp = Blueprint("doctor", __name__)


# View doctor list
@doctor_bp.route("/doctors", methods=["GET"])
def get_doctors():

    doctors = Doctor.get_doctors()

    return render_template("doctors.html", doctors=doctors)


# Add doctor
@doctor_bp.route("/doctors/add", methods=["POST"])
def add_doctor():

    name = request.form.get("name")
    specialization = request.form.get("specialization")

    Doctor.add_doctor(name, specialization)

    return jsonify({
        "message": "Doctor added successfully"
    })