"""
#TODO
"""

# Standard library imports
import os

# Local application imports
from classes.cls_user import User
# from app.pst4_app_student import StudentUser
#from app.pst4_app_teacher import TeacherUser

class AppUser(User):

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
        recept_path = "./data/users.txt"
        if os.path.exists(recept_path):
            with open(recept_path, "r", encoding="utf8") as rf:
                lines = rf.readlines()
            for line in lines:
                # Sequence unpacking: 
                # https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
                uid, first_name, last_name, contact_num, username, password = line.strip("\n").split(",")
                
                if input_username == username:
                    if input_password == password:
                        return AppUser(uid, first_name, last_name, contact_num, input_username, input_password)
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

    def import_data():
        """
        Imports all relevant data about a user including their progress within the courses.
        
        """
        pass

if __name__ == "__main__":
    pass
