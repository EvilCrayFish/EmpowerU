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

         Parameter(s):
        - ID: 
        - title: string - the title of the post
        - date: string - the date which the post was made in dd/mm/yy format
        - time: string - the time which the post was bade in hh:mm format 
        - user: string - the name of the user who made the post
        - text: string - the main body text of the post
        - forum: string - the forum which the post belongs to

        Returns:
        (None)

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

        Parameter(s):
        (None)

        Returns:
        - code: string - the code attatched to the comment.

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
        
        Parameter(s):
        - ID: string - the Post's ID 
        - Author: string - the name of the person who wrote the Post.
        - date: string - the date which the comment was made in dd/mm/yy format
        - time: string - the time which the comment was made in hh:mm format 
        - text: string - the main text in the comment's body

        Returns:
        - object - an instace of the Post class.

        """
        from classes.cls_comment import Comment
        return Comment(self, ID, author, date, time, text)

    def load_code(self):
        """
        Load the code associated with the Post from a text file named postID_commentID_code.txt.

        Parameter(s):
        - forumDir: string - the directory where the code is stored.

        Returns:
        - code: string - the code attatched to the post.
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
    

    # FOR TESTING

    def __eq__(self, other):
        if not isinstance(other, Post):
            return False
        
        if self.id != other.id:
            print(f"ID mismatch: {self.id} != {other.id}")
        if self.title != other.title:
            print(f"Title mismatch: {self.title} != {other.title}")
        if self.user != other.user:
            print(f"User mismatch: {self.user} != {other.user}")
        if self.date != other.date:
            print(f"Date mismatch: {self.date} != {other.date}")
        if self.time != other.time:
            print(f"Time mismatch: {self.time} != {other.time}")
        if self.text != other.text:
            print(f"Text mismatch: {self.text} != {other.text}")
        if self.forum != other.forum:
            print(f"Forum mismatch: {self.forum} != {other.forum}")
            
        return (
            self.id == other.id and 
            self.title == other.title and 
            self.user == other.user and 
            self.date == other.date and 
            self.time == other.time and 
            self.text == other.text and 
            self.forum == other.forum
        )

# DO NOT MODIFY BEYOND THIS LINE
if __name__ == "__main__":
    pass
