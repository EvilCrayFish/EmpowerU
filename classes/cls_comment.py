
"""
FIT1056 2024 Semester 2
EmpowerU Project

This file contains the class definition for the comment class.
"""

import os

class Comment:
    def __init__(self, parent_post, ID, author, date, time, text): 
        """
        Constructor method for the Comment class.
        - Represents a comment on a post, without inheriting from Post.
        - All inputs are strings.
        """
        self.parent_post = parent_post  # Reference to the parent post
        self.id = ID                    # Unique ID for the comment
        self.author = author            # Author of the comment
        self.date = date                # Date the comment was made
        self.time = time                # Time the comment was made
        self.text = text                # The comment text

    def load_code(self):
        """
        Load the code associated with the comment from a text file named postID_commentID_code.txt.
        """
        code = None
        # Directory where code files are stored
        code_dir = './data/forum/python_forum/code/'

        # Construct the expected filename based on the parent post ID and comment ID
        expected_filename = f"{self.parent_post.id}_{self.id}_code.txt"

        # Check if the file exists and has the correct naming convention
        if os.path.isfile(os.path.join(code_dir, expected_filename)):
            # Read the code from the file
            with open(os.path.join(code_dir, expected_filename), 'r', encoding='utf-8') as code_file:
                code = code_file.read()

        return code
    
    def __str__(self):
        """
        String representation for printing comments easily.
        """
        return f"Comment by {self.author} on {self.date} at {self.time}: {self.text}"

# DO NOT MODIFY BEYOND THIS LINE
if __name__ == "__main__":
    pass
