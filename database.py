import mysql.connector
import json
import sys, os

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class Database:
    def __init__(self):

        with open(resource_path('design/serverinfo.json'), 'r') as file:
            details = json.load(file)
        
        self.connection = mysql.connector.connect(
            host=details["host"],
            user=details["user"],
            password=details["password"],
            database=details["database"]
        )
        self.cursor = self.connection.cursor()

    def server_connect(self):
        with open(resource_path('design/serverinfo.json'), 'r') as file:
            details = json.load(file)
        
        self.connection = mysql.connector.connect(
            host=details["host"],
            user=details["user"],
            password=details["password"],
            database=details["database"]
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def validate_login(self, username, password):
        self.cursor = self.server_connect()
        global logged_user
        logged_user = username
        query = "SELECT role FROM users WHERE username = %s AND password = %s"
        self.cursor.execute(query, (username, password), multi=False)
        result = self.cursor.fetchone()

        if result:
            return result[0]  # Return the user role (Doctor or Receptionist)
        else:
            return None  # Return None if credentials are invalid

    def get_username(self):
        return logged_user
    
    def table_filtered_data(self, filter_parameter):
        self.cursor = self.server_connect()
        if filter_parameter == "All Patients":
            query = "SELECT idpatients, first_name, guardian, phone_num1 FROM patients_basic ORDER BY idpatients ASC"
        elif filter_parameter == "This Month":
            query = "SELECT idpatients, first_name, guardian, phone_num1 FROM patients_basic WHERE MONTH(last_visit) = MONTH(CURRENT_DATE()) AND YEAR(last_visit) = YEAR(CURRENT_DATE()) ORDER BY idpatients ASC"
        elif filter_parameter == "This Week":
            query = "SELECT idpatients, first_name, guardian, phone_num1 FROM patients_basic WHERE YEARWEEK(last_visit, 1) = YEARWEEK(CURRENT_DATE(), 1) ORDER BY idpatients ASC"
        elif filter_parameter == "Today":
            query = "SELECT idpatients, first_name, guardian, phone_num1 FROM patients_basic WHERE DATE(last_visit) = DATE(NOW()) ORDER BY idpatients ASC"
        else:
            query = "SELECT idpatients, first_name, guardian, phone_num1 FROM patients_basic ORDER BY idpatients ASC"
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        return data

    # Add more database-related functions for managing patient records, medicine lists, etc.

    def __del__(self):
        self.cursor.close()
        self.connection.close()
