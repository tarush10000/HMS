import mysql.connector

class UserRole:
    DOCTOR = 'Doctor'
    RECEPTIONIST = 'Receptionist'

class Database:
    def __init__(self):
        # Replace the following with your actual database connection details
        self.connection = mysql.connector.connect(
            host='your_mysql_host',
            user='your_mysql_user',
            password='your_mysql_password',
            database='your_database_name'
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
