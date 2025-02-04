"""
FIT1056 2024 Semester 2
EmpowerU Project
Team G08

This file contains the class definition for the staff class.
"""
from classes.cls_user import User
import os


class Staff(User):
    def __init__(self, uid, first_name, last_name, contact_num, email, role):
        """
        Constructor method for the Staff class which inherits from the user class.

        Parameter(s):
        - uid: string - unique identifier for the Staff
        - first_name: string - first name of the Staff
        - last_name: string - last name of the Staff
        - contact_num: string - contact number of the Staff
        - username: string - username for the Staff
        - password: string - password for the Staff

        Returns:
        (None)
        """
        super().__init__(uid, first_name, last_name, contact_num)
        self.email = email
        self.role = role

    @staticmethod
    def authenticate(input_username, input_password):
        """
        Method to authenticate a Staff user.

        Parameter(s):
        - input_username: str
        - input_password: str

        Returns:
        - an instance of Staff corresponding to the username if successful,
          None otherwise
        """
        recept_path = "./data/staff.txt"
        if os.path.exists(recept_path):
            with open(recept_path, "r", encoding="utf8") as rf:
                lines = rf.readlines()
            for line in lines:
                # Sequence unpacking: 
                # https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
                uid, first_name, last_name, contact_num, email, role, username, password = line.strip("\n").split(",")
                
                if input_username == username:
                    if input_password == password:
                        return Staff(uid, first_name, last_name, contact_num, email, role)
                    else:
                        return None # or return, or break
        else:
            print(f"Please check subdirectory and file {recept_path} exists.")


if __name__ == "__main__":
    pass