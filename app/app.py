from flask import Flask, render_template
from routes.patient_routes import patient_bp
from routes.doctor_routes import doctor_bp
from routes.appointment_routes import appointment_bp
from routes.pharmacy_routes import pharmacy_bp

# ✅ Initialize Flask app with proper folders
app = Flask(__name__, template_folder='templates', static_folder='static')

# ✅ Register Blueprints
app.register_blueprint(patient_bp)
app.register_blueprint(doctor_bp)
app.register_blueprint(appointment_bp)
app.register_blueprint(pharmacy_bp)

# ✅ Home Route (Loads Frontend UI)
@app.route("/")
def home():
    return render_template("index.html")

# ✅ Health Check Route (useful for DevOps / monitoring)
@app.route("/health")
def health():
    return {"status": "running"}, 200

# ✅ Run Application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
