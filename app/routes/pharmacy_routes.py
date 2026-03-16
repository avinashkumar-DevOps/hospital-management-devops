from flask import Blueprint, request, render_template, jsonify
from models.medicine import Medicine

pharmacy_bp = Blueprint("pharmacy", __name__)


# View medicines
@pharmacy_bp.route("/pharmacy", methods=["GET"])
def pharmacy():

    medicines = Medicine.get_medicines()

    return render_template(
        "pharmacy.html",
        medicines=medicines
    )


# Add medicine
@pharmacy_bp.route("/medicine/add", methods=["POST"])
def add_medicine():

    name = request.form.get("name")
    quantity = request.form.get("quantity")
    price = request.form.get("price")

    Medicine.add_medicine(
        name,
        quantity,
        price
    )

    return jsonify({
        "message": "Medicine added successfully"
    })