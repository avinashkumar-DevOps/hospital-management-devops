from config import get_db_connection

class Billing:

    def create_bill(patient_id,total_amount):

        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO billing(patient_id,total_amount)
        VALUES(%s,%s)
        """

        cursor.execute(query,(patient_id,total_amount))
        conn.commit()

        cursor.close()
        conn.close()

    def get_bills():

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM billing")

        bills = cursor.fetchall()

        cursor.close()
        conn.close()

        return bills