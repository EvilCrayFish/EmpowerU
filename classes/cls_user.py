"""
FIT1056 2024 Semester 2
EmpowerU Project

Class definition for User
Users are the parent class for all other users
"""

class User:

    def __init__(self, uid, first_name, last_name, contact_num):
        """
        Constructor for the User class.
        """
        self.uid = uid #User ID
        self.first_name = first_name
        self.last_name = last_name
        self.contact_num = contact_num

if __name__ == "__main__":
    pass