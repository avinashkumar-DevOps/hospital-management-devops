from flask import Flask

# Import blueprints
from .routes.patient_routes import patient_bp
from .routes.doctor_routes import doctor_bp
from .routes.appointment_routes import appointment_bp
from .routes.pharmacy_routes import pharmacy_bp


def create_app():

    app = Flask(__name__)

    # Configuration
    app.config['SECRET_KEY'] = 'hospital-secret-key'


    # Register Blueprints
    app.register_blueprint(patient_bp)
    app.register_blueprint(doctor_bp)
    app.register_blueprint(appointment_bp)
    app.register_blueprint(pharmacy_bp)


    @app.route("/")
    def home():
        return "Hospital Management System Running"


    return app