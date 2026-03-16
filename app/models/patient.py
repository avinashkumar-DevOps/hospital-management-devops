from config import get_db_connection

class Patient:

    def register_patient(name, age, gender, contact):

        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO patients(name, age, gender, contact)
        VALUES(%s,%s,%s,%s)
        """

        cursor.execute(query,(name,age,gender,contact))
        conn.commit()

        cursor.close()
        conn.close()

    def get_all_patients():

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM patients")

        patients = cursor.fetchall()

        cursor.close()
        conn.close()

        return patients