from flask import Flask
from routes.patient_routes import patient_bp
from routes.doctor_routes import doctor_bp
from routes.appointment_routes import appointment_bp
from routes.pharmacy_routes import pharmacy_bp

app = Flask(__name__)

app.register_blueprint(patient_bp)
app.register_blueprint(doctor_bp)
app.register_blueprint(appointment_bp)
app.register_blueprint(pharmacy_bp)

@app.route("/")
def home():
    return "Hospital Management System Running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)