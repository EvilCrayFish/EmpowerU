"""
Contains class definition for the ForumPage window
"""

# Third party imports
import tkinter as tk
import os
import csv
from classes.cls_post import Post
from classes.cls_comment import Comment

global forumDir
forumDir = "python_forum"

class PyForumPage(tk.Frame):
    def __init__(self, master, homepage, user):
        super().__init__(master)
        self.master = master
        self.homepage = homepage
        self.image_path = "./images/logo.png"
        self.user = user

        self.grid(row=0, column=0, sticky="nsew")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)

        # Top Frame (titleframe)
        self.titleframe = tk.Frame(self, padx=10, bd=5, relief="groove", width=1280)
        self.titleframe.grid(row=0, column=0, sticky="nsew", columnspan=2)

        self.logo_photoimage = tk.PhotoImage(master=self, file=self.image_path)
        self.logo_label = tk.Label(master=self.titleframe, image=self.logo_photoimage, width=128, height=128)
        self.logo_label.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)

        self.login_title = tk.Label(master=self.titleframe, text="EMPOWERU", font=("Arial Bold", 30))
        self.login_title.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        # New label for "Python Course Forum"
        self.course_label = tk.Label(master=self.titleframe, text="Python Course Forum", font=("Arial", 10))
        self.course_label.grid(row=0, column=2, padx=10, pady=(10, 10), sticky=tk.W)

        # Home button to return to the homepage
        self.home_button = tk.Button(master=self.titleframe, text="Home", command=self.return_to_menu)
        self.home_button.grid(row=0, column=3, padx=10, pady=10, sticky=tk.E)

        # Make the titleframe expand and occupy available space
        self.titleframe.grid_columnconfigure(0, weight=0)  
        self.titleframe.grid_columnconfigure(1, weight=0)
        self.titleframe.grid_columnconfigure(2, weight=1)  
        self.titleframe.grid_columnconfigure(3, weight=0)  

        # Bottom left Frame (postframe) for listing posts
        self.postframe = tk.Frame(self, bd=5, relief="groove", width=200)
        self.postframe.grid(row=1, column=0, sticky="nsew")

        # Search bar
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(master=self.postframe, textvariable=self.search_var, width=30)
        self.search_entry.grid(row=0, column=0, padx=10, pady=10)
        self.search_entry.bind("<Return>", lambda event: self.search_button.invoke())

        self.search_button = tk.Button(master=self.postframe, text="Search", command=self.search_posts)
        self.search_button.grid(row=0, column=1, padx=10, pady=10)

        # Right side frame (post_window) to display the selected post
        self.post_canvas = tk.Canvas(self, bd=5, relief="groove", width=800, height=600)
        self.post_canvas.grid(row=1, column=1, sticky="nsew")

        # Right scrollbar for the post window
        self.post_scrollbar = tk.Scrollbar(self, orient="vertical", command=self.post_canvas.yview)
        self.post_scrollbar.grid(row=1, column=2, sticky="ns")

        self.post_canvas.configure(yscrollcommand=self.post_scrollbar.set)

        # Create post_window inside the canvas for post content
        self.post_window = tk.Frame(self.post_canvas)
        self.post_canvas.create_window((0, 0), window=self.post_window, anchor="nw", width=800)
        self.post_window.bind("<Configure>", lambda e: self.post_canvas.configure(scrollregion=self.post_canvas.bbox("all")))

        # Load posts and create the list
        self.posts = self.load_posts()
        self.create_scrollable_posts()

    def create_scrollable_posts(self, posts=None):
        """
        Create scrollable buttons representing posts in the postframe.
        """
        if posts is None:
            posts = self.posts

        # Clear existing content in the postframe except search widgets
        for widget in self.postframe.winfo_children():
            if widget not in [self.search_entry, self.search_button]:
                widget.destroy()

        # Create a canvas for scrolling the posts
        self.post_canvas_list = tk.Canvas(self.postframe, width=200, height=400)
        self.post_canvas_list.grid(row=1, column=0, sticky=tk.NW)

        # Create a frame inside the canvas where post buttons will be placed
        self.button_frame = tk.Frame(self.post_canvas_list)
        self.post_canvas_list.create_window((0, 0), window=self.button_frame, anchor='nw')

        # Create post buttons inside button_frame
        for idx, post in enumerate(posts):
            title_display = post.title if len(post.title) <= 30 else post.title[:27] + "..."
            button_text = f"{title_display}\nAuthor: {post.user}"
            post_button = tk.Button(self.button_frame, text=button_text, width=35, relief="groove", anchor='w',
                                    font=("Arial", 10, "bold"), command=lambda p=post: self.view_post(p))
            post_button.grid(row=idx, column=0, padx=5, pady=5, sticky=tk.W)

        # Set up scrollbar for the post list
        self.scrollbar_list = tk.Scrollbar(self.postframe, orient="vertical", command=self.post_canvas_list.yview)
        self.scrollbar_list.grid(row=1, column=1, sticky=tk.NS)

        # Configure canvas to use the scrollbar
        self.post_canvas_list.configure(yscrollcommand=self.scrollbar_list.set)

        # Bind canvas resizing to update its scrollable region
        self.button_frame.bind("<Configure>", lambda event: self.post_canvas_list.configure(scrollregion=self.post_canvas_list.bbox("all")))
        
        # Create New Post button at the bottom of the postframe
        self.new_post_button = tk.Button(self.postframe, text="Create New Post", command=self.create_new_post_popup)
        self.new_post_button.grid(row=2, column=0, padx=10, pady=10)

    def load_posts(self):
        posts = []
        posts_dir = f'./data/forum/{forumDir}/posts/'

        for filename in os.listdir(posts_dir):
            if filename.endswith('_post.csv'):
                post_id = filename.split('_')[0]

                file_path = os.path.join(posts_dir, filename)
                with open(file_path, newline='', encoding='utf-8') as csvfile:
                    reader = csv.reader(csvfile)

                    header = next(reader)  # Get the first line
                    title = header[0]      # Title
                    date = header[1]       # Date
                    time = header[2]       # Time
                    user = header[3]       # Author

                    text_lines = [row[0] for row in reader]
                    text = "\n".join(text_lines).strip()

                    post = Post(post_id, title, date, time, user, text, forumDir)
                    posts.append(post)

        return posts

    def view_post(self, post):
        """
        View the selected post in the post_window (which is scrollable).
        """
        # Clear previous post content
        for widget in self.post_window.winfo_children():
            widget.destroy()

        # Title (wrap at 40 characters, 10px padding on the left)
        title_font = ("Arial", 30, "bold")
        wrapped_title = self.wrap_text(post.title, 30)
        title_id = tk.Label(self.post_window, text=wrapped_title, font=title_font, anchor="nw")
        title_id.pack(anchor="nw", pady=(20, 10), padx=10)

        # Author, date, and time (place dynamically below title, with 10px padding on the left)
        meta_font = ("Arial", 12, "italic")
        meta_info = f"Author: {post.user} | {post.date}, {post.time}"
        meta_label = tk.Label(self.post_window, text=meta_info, font=meta_font, anchor="nw", fg="gray")
        meta_label.pack(anchor="nw", padx=10)

        # Post text (wrap at 110 characters, with 10px padding on the left)
        text_font = ("Arial", 12)
        wrapped_text = self.wrap_text(post.text, 90)
        text_label = tk.Label(self.post_window, text=wrapped_text, font=text_font, anchor="nw", justify="left")
        text_label.pack(anchor="nw", pady=10, padx=10)

        # Code block (restored functionality, 10px padding on the left)
        if post.code:
            code_frame = tk.Frame(self.post_window, bg="black")
            code_frame.pack(fill=tk.X, padx=10, pady=(0, 20))

            code_label = tk.Label(code_frame, text=post.code, font=("Courier", 10), fg="white", bg="black", padx=10, pady=10, anchor="nw")
            code_label.pack(anchor="nw", fill=tk.X)

        # Display Comments
        self.display_comments(post)

        # Update the scroll region for post content
        self.post_canvas.update_idletasks()
        self.post_canvas.configure(scrollregion=self.post_canvas.bbox("all"))


    def display_comments(self, post):
        """
        Display comments related to the post. Wrapped at 140 characters.
        """
        comments_label = tk.Label(self.post_window, text="Comments", font=("Arial Bold", 14), anchor="nw")
        comments_label.pack(anchor="nw", pady=10, padx=10)

        for comment in reversed(post.comments):  # Show latest comment first
            # Author and meta (10px padding on the left)
            author_label = tk.Label(self.post_window, text=comment.author, font=("Arial", 10, "bold"), anchor="nw")
            author_label.pack(anchor="nw", padx=50)

            meta_label = tk.Label(self.post_window, text=f"{comment.date} {comment.time}", font=("Arial", 8), anchor="nw", fg="gray")
            meta_label.pack(anchor="nw", padx=50, pady=(0, 5))

            # Wrap comment text at 140 characters, 10px padding on the left
            wrapped_comment = self.wrap_text(comment.text, 100)
            comment_label = tk.Label(self.post_window, text=wrapped_comment, font=("Arial", 10), anchor="nw", justify="left")
            comment_label.pack(anchor="nw", padx=50, pady=(0, 20))

            # Display code associated with the comment (if available)
            comment_code = comment.load_code()
            if comment_code:
                code_frame = tk.Frame(self.post_window, bg="black")
                code_frame.pack(fill=tk.X, padx=50, pady=(0, 20))

                code_label = tk.Label(code_frame, text=comment_code, font=("Courier", 10), fg="white", bg="black", padx=10, pady=10, anchor="nw")
                code_label.pack(anchor="nw", fill=tk.X)

        # Update the scroll region after adding all comments
        self.post_canvas.update_idletasks()
        self.post_canvas.configure(scrollregion=self.post_canvas.bbox("all"))

    def create_new_post_popup(self):
        """
        Open a popup window for creating a new post.
        """
        self.popup = tk.Toplevel(self)
        self.popup.title("Create New Post")

        # Post Title Entry
        tk.Label(self.popup, text="Title:").grid(row=0, column=0, padx=10, pady=10)
        self.title_entry = tk.Entry(self.popup, width=50)
        self.title_entry.grid(row=0, column=1, padx=10, pady=10)

        # Post Content Textbox
        tk.Label(self.popup, text="Content:").grid(row=1, column=0, padx=10, pady=10)
        self.content_text = tk.Text(self.popup, width=50, height=10)
        self.content_text.grid(row=1, column=1, padx=10, pady=10)

        # Code Entry (optional)
        tk.Label(self.popup, text="Code (optional):").grid(row=2, column=0, padx=10, pady=10)
        self.code_text = tk.Text(self.popup, width=50, height=5)
        self.code_text.grid(row=2, column=1, padx=10, pady=10)

        # Publish and Cancel Buttons
        self.publish_button = tk.Button(self.popup, text="Publish", command=self.publish_post)
        self.publish_button.grid(row=3, column=1, padx=10, pady=10, sticky=tk.E)

        self.cancel_button = tk.Button(self.popup, text="Cancel", command=self.popup.destroy)
        self.cancel_button.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
    
    def publish_post(self):
        """
        Save the new post to a CSV file and code to a text file.
        """
        import time
        title = self.title_entry.get()
        content = self.content_text.get("1.0", tk.END).strip()
        code = self.code_text.get("1.0", tk.END).strip()
        date = time.strftime("%d/%m/%Y")  # Placeholder, replace with current date
        time = time.strftime("%H:%M")        # Placeholder, replace with current time
        user = f"{self.user.first_name} {self.user.last_name}"    

        if not title or not content:
            return  # Don't allow publishing of empty posts

        # Determine next available post ID
        posts_dir = f'./data/forum/{forumDir}/posts/'
        post_files = [f for f in os.listdir(posts_dir) if f.endswith('_post.csv')]
        next_post_id = len(post_files) + 1

        # Save post to CSV file
        post_filename = f"{next_post_id}_post.csv"
        with open(os.path.join(posts_dir, post_filename), 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([title, date, time, user])
            writer.writerow([content])

        # Save code to text file (if any)
        if code:
            code_dir = f'./data/forum/{forumDir}/code/'
            code_filename = f"{next_post_id}_code.txt"
            with open(os.path.join(code_dir, code_filename), 'w', encoding='utf-8') as codefile:
                codefile.write(code)

        # Close popup and refresh posts
        self.popup.destroy()
        self.posts = self.load_posts()
        self.create_scrollable_posts()

    def wrap_text(self, text, line_length):
        """
        Utility function to wrap text at word boundaries without exceeding the specified line_length.
        """
        words = text.split()
        wrapped_lines = []
        current_line = ""

        for word in words:
            if len(current_line) + len(word) + 1 > line_length:
                wrapped_lines.append(current_line)
                current_line = word
            else:
                if current_line:
                    current_line += " " + word
                else:
                    current_line = word

        wrapped_lines.append(current_line)
        return "\n".join(wrapped_lines)

    def search_posts(self):
        """
        Filter posts based on a search term entered by the user. Only display posts where the search term is found in the title.
        """
        search_term = self.search_var.get().lower()

        # If the search term is empty, show all posts
        if not search_term:
            matching_posts = self.posts
        else:
            matching_posts = [post for post in self.posts if search_term in post.title.lower()]

        # Create new scrollable posts based on the search result
        self.create_scrollable_posts(matching_posts)

    def return_to_menu(self):
        """
        Return to the homepage.
        """
        self.place_forget()
        self.homepage.place(relx=.5, rely=.5, anchor=tk.CENTER)




if __name__ == "__main__":
    # DO NOT MODIFY
    pass
