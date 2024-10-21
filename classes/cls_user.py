"""
FIT1056 2024 Semester 2
EmpowerU Project
Team G08

Class definition for User
Users are the parent class for all other users
"""

class User:

    def __init__(self, uid, first_name, last_name, contact_num):
        """
        Constructor method for the Staff class which inherits from the user class.

        Parameter(s):
        - uid: string - unique identifier for the User
        - first_name: string - first name of the User
        - last_name: string - last name of the User
        - contact_num: string - contact number of the User
        - username: string - username for the User
        - password: string - password for the User

        Returns:
        (None)
        """
        self.uid = uid
        self.first_name = first_name
        self.last_name = last_name
        self.contact_num = contact_num

if __name__ == "__main__":
    pass