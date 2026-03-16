from config import get_db_connection

class Doctor:

    def add_doctor(name,specialization):

        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO doctors(name,specialization)
        VALUES(%s,%s)
        """

        cursor.execute(query,(name,specialization))
        conn.commit()

        cursor.close()
        conn.close()

    def get_doctors():

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM doctors")

        doctors = cursor.fetchall()

        cursor.close()
        conn.close()

        return doctors