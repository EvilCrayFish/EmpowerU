"""
FIT1056 2024 Semester 2
EmpowerU Project
Team G08

Class definition for the Mentor
Mentor are teachers
"""

# Standard library imports
import os

# Local application imports
from classes.cls_user import User

class Mentor(User):

    @staticmethod
    def authenticate(input_username, input_password):
        """
        Method to authenticate a Mentor user, used on the login page to let users log in. 

        Parameter(s):
        - input_username: string - the username which the user entered
        - input_password: string - 

        Returns:
        - an instance of Mentor corresponding to the username if successful,
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
        Constructor method for the ReceptionistUser class.

        Parameters:
        - uid: string - unique identifier for the user
        - first_name: string - first name of the user
        - last_name: string - last name of the user
        - contact_num: string - contact number of the user
        - username: string - username for the user
        - password: string - password for the user

        Returns:
        (None)
        """
        super().__init__(uid, first_name, last_name, contact_num)
        self.username = username
        self.password = password
        self.import_all_data()


    
if __name__ == "__main__":
    pass
