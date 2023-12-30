import mysql.connector
import json
import sys, os

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class Database:
    def __init__(self):
        pass

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
    
    #get patient details
    
    def get_firstName(self , id):
        self.cursor = self.server_connect()
        query = "SELECT first_name FROM patients_basic WHERE idpatients = %s"
        self.cursor.execute(query, (id,), multi=False)
        result = self.cursor.fetchone()
        return result[0] if result else None
    
    def get_middleName(self, id):
        self.cursor = self.server_connect()
        query = "SELECT middle_name FROM patients_basic WHERE idpatients = %s"
        self.cursor.execute(query, (id,), multi=False)
        result = self.cursor.fetchone()
        return result[0] if result else None

    def get_lastName(self, id):
        self.cursor = self.server_connect()
        query = "SELECT last_name FROM patients_basic WHERE idpatients = %s"
        self.cursor.execute(query, (id,), multi=False)
        result = self.cursor.fetchone()
        return result[0] if result else None

    def get_guardian(self, id):
        self.cursor = self.server_connect()
        query = "SELECT guardian FROM patients_basic WHERE idpatients = %s"
        self.cursor.execute(query, (id,), multi=False)
        result = self.cursor.fetchone()
        return result[0] if result else None

    def get_occupation(self, id):
        self.cursor = self.server_connect()
        query = "SELECT occupation FROM patients_basic WHERE idpatients = %s"
        self.cursor.execute(query, (id,), multi=False)
        result = self.cursor.fetchone()
        return result[0] if result else None

    def get_phoneNum1(self, id):
        self.cursor = self.server_connect()
        query = "SELECT phone_num1 FROM patients_basic WHERE idpatients = %s"
        self.cursor.execute(query, (id,), multi=False)
        result = self.cursor.fetchone()
        return result[0] if result else None

    def get_phoneNum2(self, id):
        self.cursor = self.server_connect()
        query = "SELECT phone_num2 FROM patients_basic WHERE idpatients = %s"
        self.cursor.execute(query, (id,), multi=False)
        result = self.cursor.fetchone()
        return result[0] if result else None

    def get_sex(self, id):
        self.cursor = self.server_connect()
        query = "SELECT sex FROM patients_basic WHERE idpatients = %s"
        self.cursor.execute(query, (id,), multi=False)
        result = self.cursor.fetchone()
        return result[0] if result else None

    def get_address1(self, id):
        self.cursor = self.server_connect()
        query = "SELECT address1 FROM patients_basic WHERE idpatients = %s"
        self.cursor.execute(query, (id,), multi=False)
        result = self.cursor.fetchone()
        return result[0] if result else None

    def get_address2(self, id):
        self.cursor = self.server_connect()
        query = "SELECT address2 FROM patients_basic WHERE idpatients = %s"
        self.cursor.execute(query, (id,), multi=False)
        result = self.cursor.fetchone()
        return result[0] if result else None

    def get_dob(self, id):
        self.cursor = self.server_connect()
        query = "SELECT dob FROM patients_basic WHERE idpatients = %s"
        self.cursor.execute(query, (id,), multi=False)
        result = self.cursor.fetchone()
        return result[0] if result else None

    def get_age(self, id):
        self.cursor = self.server_connect()
        query = "SELECT age FROM patients_basic WHERE idpatients = %s"
        self.cursor.execute(query, (id,), multi=False)
        result = self.cursor.fetchone()
        return result[0] if result else None

    def get_bloodGroup(self, id):
        self.cursor = self.server_connect()
        query = "SELECT blood_group FROM patients_basic WHERE idpatients = %s"
        self.cursor.execute(query, (id,), multi=False)
        result = self.cursor.fetchone()
        return result[0] if result else None

    def get_obstetricHis(self, id):
        self.cursor = self.server_connect()
        query = "SELECT obstretic_his FROM patients_basic WHERE idpatients = %s"
        self.cursor.execute(query, (id,), multi=False)
        result = self.cursor.fetchone()
        return result[0] if result else None

    def get_familyHis(self, id):
        self.cursor = self.server_connect()
        query = "SELECT family_his FROM patients_basic WHERE idpatients = %s"
        self.cursor.execute(query, (id,), multi=False)
        result = self.cursor.fetchone()
        return result[0] if result else None

    def get_pastHis(self, id):
        self.cursor = self.server_connect()
        query = "SELECT past_his FROM patients_basic WHERE idpatients = %s"
        self.cursor.execute(query, (id,), multi=False)
        result = self.cursor.fetchone()
        return result[0] if result else None

    def get_notes(self, id):
        self.cursor = self.server_connect()
        query = "SELECT notes FROM patients_basic WHERE idpatients = %s"
        self.cursor.execute(query, (id,), multi=False)
        result = self.cursor.fetchone()
        return result[0] if result else None

    # Add more database-related functions for managing patient records, medicine lists, etc.

    def __del__(self):
        self.cursor.close()
        self.connection.close()
