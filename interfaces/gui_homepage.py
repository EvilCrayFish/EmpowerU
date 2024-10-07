"""
#TODO File header pls
"""


# Third party imports
import tkinter as tk

# Local application imports

from interfaces.gui_forum_page import ForumPage
from interfaces.gui_progress_tracker import ProgressTracker
from interfaces.gui_courses_page import CoursesPage
from classes.cls_app_user import AppUser
from classes.cls_mentor import Mentor

class HomePage(tk.Frame):

    def __init__(self, master, user):
        """
        Constructor for the ReceptionistMenu

        Parameter(s):
        - master: master widget of this widget instance
        - user: an instance of the ReceptionistUser class
                             representing the receptionist that has 
                             successfully logged in
        """
        super().__init__(master=master)
        self.master = master
        self.user = user
        
        if isinstance(user, AppUser): #User Homepage
            self.welcome_label = tk.Label(self, text=f"Welcome in USER, {user.first_name}!")
            self.welcome_label.pack(padx=10, pady=10)

            self.label1 = tk.Label(self, text="Choose one of the following:")
            self.label1.pack(padx=10, pady=10)

            self.courses_btn = tk.Button(self, text="Courses", command=self.show_courses_page)
            self.courses_btn.pack(padx=10, pady=10)

            self.fourm_btn = tk.Button(self, text="Forum", command=self.show_forum_page)
            self.fourm_btn.pack(padx=10, pady=10)

            self.progress_tracker_btn = tk.Button(self, text="Progress Tracker", command=self.show_progress_tracker)
            self.progress_tracker_btn.pack(padx=10, pady=10)

            self.options_btn = tk.Button(self, text="Settings")
            self.progress_tracker_btn.pack(padx=10, pady=10)

            self.logout_btn = tk.Button(self, text="Log out", command=self.logout)
            self.logout_btn.pack(padx=10, pady=10)
        
        else: #Teacher Homepage
            #TODO Navigation for Teacher
            self.welcome_label = tk.Label(self, text=f"Welcome in TEACHER, {user.first_name}!")
            self.welcome_label.pack(padx=10, pady=10)

            self.label1 = tk.Label(self, text="Choose one of the following:")
            self.label1.pack(padx=10, pady=10)

            self.register_btn = tk.Button(self, text="Register a student")
            self.register_btn.pack(padx=10, pady=10)

            self.search_btn = tk.Button(self, text="Search teachers by instrument", command=self.show_search_teachers_frame)
            self.search_btn.pack(padx=10, pady=10)

            self.class_btn = tk.Button(self, text="Create a weekly scheduled class")
            self.class_btn.pack(padx=10, pady=10)

            self.logout_btn = tk.Button(self, text="Log out", command=self.logout)
            self.logout_btn.pack(padx=10, pady=10)

    def show_progress_tracker(self):
        """
        Method to handle the search teachers functionality upon button click.
        """
        progress_page = ProgressTracker(self.master, self, self.user)
        progress_page.place(relx=.5, rely=.5, anchor=tk.CENTER)
        self.hide_menu()
        
    def show_courses_page(self):
        """
        Method to handle the search teachers functionality upon button click.
        """
        courses_page = CoursesPage(self.master, self, self.user)
        courses_page.place(relx=.5, rely=.5, anchor=tk.CENTER)
        self.hide_menu()


    def show_search_teachers_frame(self):
        """
        Method to handle the search teachers functionality upon button click.
        """
        #search_teachers = SearchTeachers(self.master, self, self.user)
        #search_teachers.place(relx=.5, rely=.5, anchor=tk.CENTER)
        self.hide_menu()

    def show_forum_page(self):
        """
        Method to handle the search teachers functionality upon button click.
        """
        forum_page = ForumPage(self.master, self, self.user)
        forum_page.place(relx=.5, rely=.5, anchor=tk.CENTER)
        self.hide_menu()


    def logout(self):
        """
        Method to handle the logout upon button click.

        Parameter(s):
        (None)

        Return(s):
        (None)
        """
        self.hide_menu()
        self.master.show_loginpage()

    def show_menu(self):
        """
        Method to show the receptionist menu in the main window.
        """
        self.place(relx=.5, rely=.5, anchor=tk.CENTER)

    def hide_menu(self):
        """
        Method to hide the receptionist menu frame.
        """
        self.place_forget()


if __name__ == "__main__":
    # DO NOT MODIFY
    pass
