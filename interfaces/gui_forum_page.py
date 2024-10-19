"""
FIT1056 2024 Semester 2
EmpowerU Project
Team G08

Contains class definition for the ForumPage window which is the navigation page to the different forums.
"""

# Third party imports
import tkinter as tk
import os
import csv
from classes.cls_post import Post
from classes.cls_comment import Comment
from interfaces.gui_ai_forum_page import AiForumPage
from interfaces.gui_python_forum_page import PyForumPage
from interfaces.gui_security_forum_page import SecurityForumPage

class ForumPage(tk.Frame):
    def __init__(self, master, homepage, user):
        """
        Constructor for the ForumPage class.
        
        Parameters:
        - master: master widget of this widget instance
        - homepage: an instance of the HomePage Window
        - user: an instance of the User class

        Returns:
        (None)
        """
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

        self.course_label = tk.Label(master=self.titleframe, text="Forums", font=("Arial", 10))
        self.course_label.grid(row=0, column=2, padx=10, pady=(10, 10), sticky=tk.W)

        # Home button to return to the homepage
        self.home_button = tk.Button(master=self.titleframe, text="Home", command=self.return_to_menu)
        self.home_button.grid(row=0, column=3, padx=10, pady=10, sticky=tk.E)

        self.titleframe.grid_columnconfigure(0, weight=0)
        self.titleframe.grid_columnconfigure(1, weight=0)
        self.titleframe.grid_columnconfigure(2, weight=1)
        self.titleframe.grid_columnconfigure(3, weight=0)

        self.label1 = tk.Label(self, text="Select forum:", font=("Arial Bold", 15))
        self.label1.grid(row=1, column=0, padx=10, pady=10, sticky=tk.S)

        self.py_forum_btn = tk.Button(self, text="Python", command=self.show_python_forum)
        self.py_forum_btn.grid(row=2, column=0, padx=10, pady=10, sticky=tk.S)

        self.info_security_forum_btn = tk.Button(self, text="Information Security", command=self.show_security_forum)
        self.info_security_forum_btn.grid(row=3, column=0, padx=10, pady=10, sticky=tk.S)

        self.ai_forum_btn = tk.Button(self, text="Artificial Intelligence", command=self.show_ai_forum)
        self.ai_forum_btn.grid(row=4, column=0, padx=10, pady=10, sticky=tk.S)

    def show_ai_forum(self):
        """
        Handles the GUI logic for showing the AI forum page.
        
        Parameters:
        (None)
        
        Returns:
        (None)
        """
        ai_forum_page = AiForumPage(self.master, self, self.user)
        ai_forum_page.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.return_to_menu()

    def show_security_forum(self):
        """
        Handles the GUI logic for showing the security forum page.
        
        Parameters:
        (None)
        
        Returns:
        (None)
        """
        security_forum_page = SecurityForumPage(self.master, self, self.user)
        security_forum_page.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.return_to_menu()

    def show_python_forum(self):
        """
        Handles the GUI logic for showing the Python forum page.
        
        Parameters:
        (None)
        
        Returns:
        (None)
        """
        py_forum_page = PyForumPage(self.master, self, self.user)
        py_forum_page.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.return_to_menu()

    def return_to_menu(self):
        """
        Handles the GUI logic for returning to the home page
        
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
