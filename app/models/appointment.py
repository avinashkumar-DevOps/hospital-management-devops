from config import get_db_connection

class Appointment:

    def book_appointment(patient_id,doctor_id,date):

        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO appointments(patient_id,doctor_id,date)
        VALUES(%s,%s,%s)
        """

        cursor.execute(query,(patient_id,doctor_id,date))
        conn.commit()

        cursor.close()
        conn.close()

    def get_appointments():

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM appointments")

        appointments = cursor.fetchall()

        cursor.close()
        conn.close()

        return appointments