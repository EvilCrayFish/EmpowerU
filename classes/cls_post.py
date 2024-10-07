"""
FIT1056 2024 Semester 2
EmpowerU Project

This file contains the class definition for the post class.
"""
import csv

class Post():

    def __init__(self, ID, title, date, time, user, text, code):
        """
        Constructor method for the Student class
        - All inputs are strings except for the ID which is an integer
        """
        self.id = int(ID)
        self.title = title
        self.user = user
        self.date = date
        self.time = time
        self.text = text
        self.code = code


# DO NOT MODIFY BEYOND THIS LINE
if __name__ == "__main__":
    pass
