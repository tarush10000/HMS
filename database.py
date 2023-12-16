import mysql.connector
import sys, os

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class Database:
    def __init__(self):
        # Replace the following with your actual database connection details
        self.connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='Tarush@10000',
            database='hosp'
        )
        self.cursor = self.connection.cursor()

    def validate_login(self, username, password):
        query = "SELECT role FROM users WHERE username = %s AND password = %s"
        self.cursor.execute(query, (username, password))
        result = self.cursor.fetchone()

        if result:
            return result[0]  # Return the user role (Doctor or Receptionist)
        else:
            return None  # Return None if credentials are invalid

    def get_doctor_name(self):
        # Implement logic to retrieve the doctor's name from the database
        pass

    def get_receptionist_name(self):
        # Implement logic to retrieve the receptionist's name from the database
        pass

    # Add more database-related functions for managing patient records, medicine lists, etc.

    def __del__(self):
        self.cursor.close()
        self.connection.close()
