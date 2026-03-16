from flask import Blueprint, request, render_template, jsonify
from models.appointment import Appointment
from models.patient import Patient
from models.doctor import Doctor

appointment_bp = Blueprint("appointment", __name__)


# View appointments
@appointment_bp.route("/appointments", methods=["GET"])
def appointments():

    appointments = Appointment.get_appointments()
    patients = Patient.get_all_patients()
    doctors = Doctor.get_doctors()

    return render_template(
        "appointments.html",
        appointments=appointments,
        patients=patients,
        doctors=doctors
    )


# Book appointment
@appointment_bp.route("/appointments/book", methods=["POST"])
def book_appointment():

    patient_id = request.form.get("patient_id")
    doctor_id = request.form.get("doctor_id")
    date = request.form.get("date")

    Appointment.book_appointment(
        patient_id,
        doctor_id,
        date
    )

    return jsonify({
        "message": "Appointment booked successfully"
    })