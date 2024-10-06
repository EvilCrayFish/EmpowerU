"""
FIT1056 2024 Semester 2
EmpowerU Project

This file contains the class definition for the post class.
"""
import csv

class Post():

    def __init__(self, title, text, code):
        """
        Constructor method for the Student class
        - All inputs are strings except for comments which is a list of strings
        """
        self.title = title
        self.text = text
        self.code = code
        # Initialize an empty list to store the comments
        self.comments = []

        # Open and read the CSV file
        with open('./data/comments.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            # Loop through each row in the CSV file
            for row in reader:
                # Append each row (post) as a list in the 'posts' list
                self.comments.append(row)


        
        
        

    def addComment(self, text):
        
        self.comments.append(text)
        
        pass
    def updateVersion():
        
        pass
    def viewUsers():
        #TODO Write method
        pass

# DO NOT MODIFY BEYOND THIS LINE
if __name__ == "__main__":
    pass
