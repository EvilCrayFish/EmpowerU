"""
Contains class definition for the ForumPage window
"""

# Third party imports
import tkinter as tk
import csv
from classes.cls_post import Post
from classes.cls_comment import Comment  # Assuming a Comment class exists in a similar manner to Post


class ForumPage(tk.Frame):
    def __init__(self, master, homepage, user):
        """
        Constructor for the ForumPage class.

        Parameters:
        - master: master widget of this widget instance
        - homepage: an instance of the homepage class
        - user: an instance of the user class
        """
        super().__init__(master)

        self.master = master
        self.homepage = homepage
        self.image_path = "./images/logo.png"
        self.user = user

        # Make the main frame fill the entire window
        self.grid(row=0, column=0, sticky="nsew")

        # Configure grid layout for responsiveness
        self.grid_columnconfigure(0, weight=1)  # Column 0 can expand
        self.grid_rowconfigure(0, weight=0)     # Row 0 does not expand, it will hold the title frame
        #self.grid_rowconfigure(1, weight=1)     # Row 1 can expand

        # Top Frame (titleframe) aligned to top-left
        self.titleframe = tk.Frame(self, padx=10, bd=5, relief="groove", width=1280)
        self.titleframe.grid(row=0, column=0, sticky="nsew", columnspan=2)

        self.logo_photoimage = tk.PhotoImage(master=self, file=self.image_path)
        self.logo_label = tk.Label(master=self.titleframe, image=self.logo_photoimage, width=128, height=128)
        self.logo_label.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)

        # Welcome heading
        self.login_title = tk.Label(master=self.titleframe, text="EMPOWERU", font=("Arial Bold", 30))
        self.login_title.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        # Search bar
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(master=self.titleframe, textvariable=self.search_var, width=30)
        self.search_entry.grid(row=0, column=2, padx=10, pady=10)

        self.search_button = tk.Button(master=self.titleframe, text="Search", command=self.search_posts)
        self.search_button.grid(row=0, column=3, padx=10, pady=10)

        # Bottom left Frame (postframe) aligned to top-left, with fixed 200px width
        self.postframe = tk.Frame(self, bd=5, relief="groove", width=200)
        self.postframe.grid(row=1, column=0, sticky="nsew")

        # Make the postframe stick to the left and allow for vertical expansion
        self.grid_rowconfigure(1, weight=1)     # Row 1 expands vertically

        # Right side frame (post_window) to display the selected post
        self.post_window = tk.Canvas(self, bd=5, relief="groove", width=800, height=600)
        self.post_window.grid(row=1, column=1, sticky="nsew")

        # Create the scrollable post buttons inside the postframe
        self.create_scrollable_posts()

    def create_scrollable_posts(self):
        """
        Create a scrollable frame for displaying post titles as clickable buttons.
        Post titles will be limited to 30 characters, with "..." appended if necessary.
        """
        # Create a Canvas widget inside postframe
        canvas = tk.Canvas(self.postframe, width=200, height=400)
        canvas.grid(row=0, column=0, sticky=tk.NW)

        # Add a vertical scrollbar to the canvas
        scrollbar = tk.Scrollbar(self.postframe, orient="vertical", command=canvas.yview)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)

        # Configure the canvas to use the scrollbar
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Create a frame inside the canvas that will hold the buttons
        button_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=button_frame, anchor='nw')

        # Load posts and create buttons
        self.posts = self.load_posts()
        for idx, post in enumerate(self.posts):
            # Limit title length to 30 characters
            title_display = post.title if len(post.title) <= 30 else post.title[:27] + "..."

            # Add author to the button text
            button_text = f"{title_display}\nAuthor: {post.user}"

            # Create a button with groove relief and bolded title
            post_button = tk.Button(button_frame, text=button_text, width=40, relief="groove", anchor='w',
                                    font=("Arial", 10, "bold"), command=lambda p=post: self.view_post(p))
            post_button.grid(row=idx, column=0, padx=5, pady=5, sticky=tk.W)

    def load_posts(self):
        """
        Load posts from a CSV file and return them as a list of Post objects.
        """
        posts = []
        # Open and read the CSV file
        with open('./data/posts.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            # Loop through each row in the CSV file
            for row in reader:
                while len(row) < 6:
                    row.append("")
                post = Post(row[0], row[1], row[2], row[3], row[4], row[5])  # Added row[5] for the new parameter
                posts.append(post)
        return posts

    def view_post(self, post):
        """
        Display the full content of a post in the post window when its title is clicked.
        """
        # Clear the previous post display
        self.post_window.delete("all")

        # Display post title (3 times bigger than text)
        title_font = ("Arial", 30, "bold")
        self.post_window.create_text(20, 20, anchor="nw", text=post.title, font=title_font, fill="black")

        # Display author (same size as the post text, gray color)
        text_font = ("Arial", 10)
        self.post_window.create_text(20, 80, anchor="nw", text=f"Author: {post.user}", font=text_font, fill="gray")

        # Display post text (regular size)
        self.post_window.create_text(20, 100, anchor="nw", text=post.text, font=text_font, fill="black")

        # If the post contains code, display it in a separate frame
        if post.code:
            code_frame = tk.Frame(self.post_window, bg="black")
            self.post_window.create_window(20, 140, anchor="nw", window=code_frame)

            code_label = tk.Label(code_frame, text=post.code, font=("Courier", 10), fg="white", bg="black", padx=10, pady=10)
            code_label.pack()

        # Load and display the comments for the post
        comments = self.load_comments(post.post_id)
        comment_y_position = 200  # Start displaying comments below post content
        for comment in comments:
            self.post_window.create_text(20, comment_y_position, anchor="nw", text=f"{comment.author} ({comment.date} {comment.time}):", font=text_font, fill="blue")
            comment_y_position += 20
            self.post_window.create_text(20, comment_y_position, anchor="nw", text=comment.text, font=text_font, fill="black")
            comment_y_position += 40

    def load_comments(self, post_id):
        """
        Load comments from a CSV file for the given post ID.

        Parameters:
        - post_id: ID of the post whose comments are to be loaded.

        Returns:
        - List of Comment objects.
        """
        comments = []
        comment_file = f'./data/{post_id}_comments.csv'
        try:
            with open(comment_file, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    while len(row) < 6:
                        row.append("")
                    comment = Comment(row[0], row[1], row[2], row[3], row[4], row[5])
                    comments.append(comment)
        except FileNotFoundError:
            print(f"No comments file found for post ID {post_id}.")
        return comments

    def search_posts(self):
        """
        Filter posts based on a search term entered by the user.
        """
        search_term = self.search_var.get().lower()
        matching_posts = [post for post in self.posts if search_term in post.title.lower() or search_term in post.text.lower()]

        # Clear the current post buttons and display the filtered ones
        for widget in self.postframe.winfo_children():
            widget.destroy()
        self.posts = matching_posts
        self.create_scrollable_posts()

    def return_to_menu(self):
        """
        This method handles the GUI logic to return to the receptionist's menu.

        Parameters:
        (None)

        Returns:
        (None)
        """
        self.place_forget()
        self.homepage.place(relx=.5, rely=.5, anchor=tk.CENTER)


if __name__ == "__main__":
    # DO NOT MODIFY
    pass
