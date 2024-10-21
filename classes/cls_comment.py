
"""
FIT1056 2024 Semester 2
EmpowerU Project
Team G08

This file contains the class definition for the comment class.
"""

import os

class Comment:
    def __init__(self, parent_post, ID, author, date, time, text): 
        """
        Constructor method for the Comment class.
        Parameters:
        - parent_post: object - The parent post 
        - ID: string - the parent post's ID
        - author: string - name of the user who made the comment
        - date: string - the date in dd/mm/yyyy format
        - time: string - the time in hh:mm format
        - text: string - the main text in the comment
        """
        self.parent_post = parent_post 
        self.id = ID                    
        self.author = author          
        self.date = date                
        self.time = time                
        self.text = text                

    def load_code(self, forumDir):
        """
        Load the code associated with the comment from a text file named postID_commentID_code.txt.

        Parameter(s):
        - forumDir: string - the directory where the code is stored.

        Returns:
        - code: string - the code attatched to the comment.

        """
        code = None
        # Directory where code files are stored
        code_dir = f'./data/forum/{forumDir}/code/'

        # Construct the expected filename based on the parent post ID and comment ID
        expected_filename = f"{self.parent_post.id}_{self.id}_code.txt"

        # Check if the file exists and has the correct naming convention
        if os.path.isfile(os.path.join(code_dir, expected_filename)):
            # Read the code from the file
            with open(os.path.join(code_dir, expected_filename), 'r', encoding='utf-8') as code_file:
                code = code_file.read()

        return code
    

# DO NOT MODIFY BEYOND THIS LINE
if __name__ == "__main__":
    pass
