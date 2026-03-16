from config import get_db_connection

class Medicine:

    def add_medicine(name,quantity,price):

        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO medicines(name,quantity,price)
        VALUES(%s,%s,%s)
        """

        cursor.execute(query,(name,quantity,price))
        conn.commit()

        cursor.close()
        conn.close()

    def get_medicines():

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM medicines")

        medicines = cursor.fetchall()

        cursor.close()
        conn.close()

        return medicines