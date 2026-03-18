from flask import Flask, render_template
from routes.patient_routes import patient_bp
from routes.doctor_routes import doctor_bp
from routes.appointment_routes import appointment_bp
from routes.pharmacy_routes import pharmacy_bp

# Initialize Flask App
app = Flask(__name__)

# ------------------ REGISTER BLUEPRINTS (API / LOGIC) ------------------
app.register_blueprint(patient_bp)
app.register_blueprint(doctor_bp)
app.register_blueprint(appointment_bp)
app.register_blueprint(pharmacy_bp)

# ------------------ FRONTEND ROUTES (HTML PAGES) ------------------

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/patients")
def patients():
    return render_template("register_patient.html")


@app.route("/doctors")
def doctors():
    return render_template("doctors.html")


@app.route("/appointments")
def appointments():
    return render_template("appointments.html")


@app.route("/pharmacy")
def pharmacy():
    return render_template("pharmacy.html")


@app.route("/billing")
def billing():
    return render_template("billing.html")


# ------------------ ERROR HANDLING (OPTIONAL BUT GOOD) ------------------

@app.errorhandler(404)
def page_not_found(e):
    return render_template("index.html"), 404


# ------------------ MAIN ------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
