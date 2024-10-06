"""
#TODO
"""

# Standard library imports
import os

# Local application imports
from classes.cls_user import User
# from app.pst4_app_student import StudentUser
#from app.pst4_app_teacher import TeacherUser

class Mentor(User):

    @staticmethod
    def authenticate(input_username, input_password):
        """
        Method to authenticate a ReceptionistUser user.

        Parameter(s):
        - input_username: str
        - input_password: str

        Returns:
        - an instance of ReceptionistUser corresponding to the username if successful,
          None otherwise
        """
        recept_path = "./data/mentors.txt"
        if os.path.exists(recept_path):
            with open(recept_path, "r", encoding="utf8") as rf:
                lines = rf.readlines()
            for line in lines:
                # Sequence unpacking: 
                # https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
                recept_id, first_name, last_name, contact_num, username, password = line.strip("\n").split(",")
                
                if input_username == username:
                    if input_password == password:
                        return Mentor(recept_id, first_name, last_name, contact_num, input_username, input_password)
                    else:
                        return None # or return, or break
        else:
            print(f"Please check subdirectory and file {recept_path} exists.")
        

    def __init__(self, uid, first_name, last_name, contact_num, username, password):
        """
        Constructor method for the ReceptionistUser class
        """
        super().__init__(uid, first_name, last_name, contact_num)
        self.username = username
        self.password = password
        self.import_all_data()

    def import_all_data(self):
        """
        Method to read all data by calling methods to read teachers data and students data.

        Parameter(s):
        (None)

        Returns:
        (None)
        """
        self.import_teachers_data()
        # self.import_students_data()
    
    def import_teachers_data(self):
        pass

    
if __name__ == "__main__":
    pass
