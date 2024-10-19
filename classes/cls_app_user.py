"""
FIT1056 2024 Semester 2
EmpowerU Project

Class definition for AppUser
AppUser are students
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
        Imports all relevant data about a user including their progress within the courses.
        
        """
        pass


    def get_name(self):
        """
        Returns the user's full name.
        """
        return f"{self._fname} {self._lname}"
    
    def update_password(self, new_password: str):
        """
        Turns the new password into a salted hash and passes to the database. 

        Arguments:
        new_password - plaintext string of the new password to set the user's password to

        Returns:
        A boolean value of whether the new pasword is set or not
        """
        pass

    @staticmethod
    def login(self, username, password):
        """
        Checks the input username and password against the username and password associated with the user. 

        Arguments:
        username - the username of the user attempting to log in
        password - the plaintext password of the user attempting to log in

        Returns:
        A boolean of whether the login was successful or not
        """
        pass

    def update_lesson_progress(self, course, progress):
        """
        Updates lesson progress, idk how yet

        Arguments:
        course - the area where progress was made
        progress - the amount of progress made
        """
        pass

    def get_lesson_progress(self, course):
        """
        Checks the amount of progress made in a course and returns the % amount

        Arguments: 
        course - which course is being reported on

        Returns:
        An integer of the amount of progress the user has made in that course
        """
        pass

    def make_post(self):
        """
        This is very underdeveloped but the idea is it compiles the post and then returns it for another object to actually store it
        """
        pass
    

if __name__ == "__main__":
    pass
