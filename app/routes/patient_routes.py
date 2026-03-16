from flask import Blueprint, request, jsonify
from models.patient import Patient

patient_bp = Blueprint("patients",__name__)

@patient_bp.route("/patients",methods=["GET"])
def get_patients():

    patients = Patient.get_all_patients()

    return jsonify(patients)


@patient_bp.route("/patients/register",methods=["POST"])
def register():

    data = request.json

    Patient.register_patient(
        data["name"],
        data["age"],
        data["gender"],
        data["contact"]
    )

    return {"message":"Patient registered"}