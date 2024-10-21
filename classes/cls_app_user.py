"""FIT1056 2024 Semester 2
EmpowerU Project
Team G08
Class definition for AppUser which represents an adult learner
"""

# Standard library imports
import os

# Local application imports
from classes.cls_user import User

class AppUser(User):
    @staticmethod
    def authenticate(input_username, input_password):
        """
        Method to authenticate an AppUser user.

        Parameter(s):
        - input_username: str
        - input_password: str

        Returns:
        - an instance of AppUser corresponding to the username if successful,
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
                        return None  # or return, or break
        else:
            print(f"Please check subdirectory and file {recept_path} exists.")

    def __init__(self, uid, first_name, last_name, contact_num, username, password):
        """
        Constructor method for the ReceptionistUser class.

        Parameter(s):
        - uid: unique identifier for the user
        - first_name: first name of the user
        - last_name: last name of the user
        - contact_num: contact number of the user
        - username: username for the user
        - password: password for the user

        Returns:
        (None)
        """
        super().__init__(uid, first_name, last_name, contact_num)
        self.username = username
        self.password = password
        self.import_all_data()

        """
        This is very underdeveloped but the idea is it compiles the post and then returns it for another object to actually store it.

        Parameters:
        (None)

        Returns:
        (None)
        """
        pass

if __name__ == "__main__":
    pass
