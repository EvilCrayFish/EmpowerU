
"""
FIT1056 2024 Semester 2
EmpowerU Project

This file contains the class definition for the comment class.
"""

from classes.cls_post import Post

class Comment(Post):
    def __init__(self, ID, author, date, time, text, code):
        """
        Constructor method for the Comment class.
        - Inherits from Post class but does not use title (replaced with author).
        - All inputs are strings, except comments, which is a list of strings.
        """
        # Initialize the parent class with an empty title (since comments don't have titles)
        super().__init__(ID, "", date, time, author, text, code)


    def __str__(self):
        """
        String representation for printing comments easily.
        """
        return f"Comment by {self.user} on {self.date} at {self.time}: {self.text}"
        

# DO NOT MODIFY BEYOND THIS LINE
if __name__ == "__main__":
    pass
