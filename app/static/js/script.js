// Hospital Management System JavaScript

document.addEventListener("DOMContentLoaded", function () {

    console.log("Hospital Dashboard Loaded");

    loadDashboardStats();

});


/* ==============================
   Dashboard Statistics
================================ */

function loadDashboardStats() {

    fetch("/patients")
        .then(response => response.json())
        .then(data => {

            if (document.getElementById("patientCount")) {
                document.getElementById("patientCount").innerText = data.length;
            }

        })
        .catch(error => console.error("Error loading patients:", error));

}



/* ==============================
   Form Validation
================================ */

function validatePatientForm() {

    let name = document.querySelector("input[name='name']").value;
    let age = document.querySelector("input[name='age']").value;
    let contact = document.querySelector("input[name='contact']").value;

    if (name === "" || age === "" || contact === "") {

        alert("Please fill all patient fields");
        return false;

    }

    if (contact.length < 10) {

        alert("Invalid phone number");
        return false;

    }

    return true;
}



/* ==============================
   Add Doctor AJAX
================================ */

function addDoctor() {

    let name = document.querySelector("input[name='name']").value;
    let specialization = document.querySelector("input[name='specialization']").value;

    fetch("/doctors/add", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            name: name,
            specialization: specialization
        })

    })
        .then(res => res.json())
        .then(data => {

            alert(data.message);
            location.reload();

        })
        .catch(err => console.error(err));

}



/* ==============================
   Book Appointment
================================ */

function bookAppointment() {

    let patient = document.querySelector("select[name='patient_id']").value;
    let doctor = document.querySelector("select[name='doctor_id']").value;
    let date = document.querySelector("input[name='date']").value;

    fetch("/appointments/book", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            patient_id: patient,
            doctor_id: doctor,
            date: date
        })

    })
        .then(res => res.json())
        .then(data => {

            alert(data.message);
            location.reload();

        })
        .catch(err => console.error(err));

}



/* ==============================
   Add Medicine
================================ */

function addMedicine() {

    let name = document.querySelector("input[name='name']").value;
    let quantity = document.querySelector("input[name='quantity']").value;
    let price = document.querySelector("input[name='price']").value;

    fetch("/medicine/add", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            name: name,
            quantity: quantity,
            price: price
        })

    })
        .then(res => res.json())
        .then(data => {

            alert(data.message);
            location.reload();

        })
        .catch(err => console.error(err));

}



/* ==============================
   Search Patient
================================ */

function searchPatient() {

    let input = document.getElementById("searchPatient").value.toLowerCase();
    let rows = document.querySelectorAll("table tr");

    rows.forEach((row, index) => {

        if (index === 0) return;

        let name = row.cells[1].innerText.toLowerCase();

        if (name.includes(input)) {
            row.style.display = "";
        } else {
            row.style.display = "none";
        }

    });

}



/* ==============================
   Dark Mode Toggle
================================ */

function toggleDarkMode() {

    document.body.classList.toggle("dark-mode");

}



/* ==============================
   Simple Notification
================================ */

function showNotification(message) {

    let notification = document.createElement("div");

    notification.className = "notification";
    notification.innerText = message;

    document.body.appendChild(notification);

    setTimeout(() => {

        notification.remove();

    }, 3000);

}



/* ==============================
   Confirm Delete
================================ */

function confirmDelete() {

    return confirm("Are you sure you want to delete this record?");

}