"""
FIT1056 2024 Semester 2
EmpowerU Project
Team G08

This file contains the class definition for the post class.
"""
import csv
import os

class Post:

    def __init__(self, ID, title, date, time, user, text, forum): 
        """
        Constructor method for the Post class.
        - All inputs are strings except for the ID which is an integer.
        """
        self.id = int(ID)
        self.title = title
        self.user = user
        self.date = date
        self.time = time
        self.text = text
        self.forum = forum
        self.comments = self.load_comments()
        self.code = self.load_code()          # Load the code associated with the post

    def load_comments(self):
        """
        Load comments for this post from the corresponding CSV files in the specified directory.
        Each comment file should follow the naming format: postid_commentid_comment.csv.
        """
        comments = []
        # Directory where comment files are stored
        comment_dir = f'./data/forum/{self.forum}/comments/'

        # Iterate through files in the directory
        for filename in os.listdir(comment_dir):
            if filename.startswith(f"{self.id}_") and filename.endswith("_comments.csv"):
                # Construct the full path to the comment file
                file_path = os.path.join(comment_dir, filename)

                # Read the comment file
                with open(file_path, newline='', encoding='utf-8') as csvfile:
                    reader = csv.reader(csvfile)
                    # Read the header
                    header = next(reader)

                    # Read the date, time, author from the header
                    date = header[0]
                    time = header[1]
                    author = header[2]

                    # Read the remaining lines as comment text
                    text = ""
                    for row in reader:
                        text += " ".join(row) + " "  # Join all lines into a single text

                    # Create a Comment object and add it to the list
                    comment = self.create_comment(filename.split('_')[1], author, date, time, text.strip())
                    comments.append(comment)

        return comments

    def create_comment(self, ID, author, date, time, text):
        """
        Factory method to create a Comment object.
        This method allows importing Comment without circular dependencies.
        """
        from classes.cls_comment import Comment  # Importing here avoids circular imports
        return Comment(self, ID, author, date, time, text)

    def load_code(self):
        """
        Load the code associated with the post from a text file named postid_code.txt.
        Only files with a single number at the beginning (e.g., '1_code.txt') are considered.
        """
        code = None
        # Directory where code files are stored
        code_dir = f'./data/forum/{self.forum}/code/'

        # Construct the expected filename based on the post ID
        expected_filename = f"{self.id}_code.txt"

        # Check if the file exists and has the correct naming convention
        if os.path.isfile(os.path.join(code_dir, expected_filename)):
            # Read the code from the file
            with open(os.path.join(code_dir, expected_filename), 'r', encoding='utf-8') as code_file:
                code = code_file.read()

        return code

# DO NOT MODIFY BEYOND THIS LINE
if __name__ == "__main__":
    pass
