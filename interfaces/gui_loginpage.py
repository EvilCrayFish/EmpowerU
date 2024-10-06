"""
#TODO file header pls
"""

# Third party imports
import tkinter as tk

# Local application imports
#TODO Define new page classes and change these imports
from classes.cls_app_user import AppUser
from classes.cls_mentor import Mentor

from interfaces.gui_appuser_homepage import AppUserHomePage
from interfaces.gui_teacher_homepage import TeacherHomePage


class LoginPage(tk.Frame):

    def __init__(self, master, image_path):
        """
        Constructor for the LoginPage class.

        Parameter(s):
        - master: master widget of this widget instance
        - image_path: str, path of the logo image file
        """
        super().__init__(master=master)
        self.master = master # Hint: a very useful instance variable
        self.image_path = image_path

        # Image obtained from: 
        # https://pngtree.com/freepng/red-blue-separation-line-musical-music-logo_6244544.html


        # Logo image
        #TODO Change Layout of Login Page
        self.logo_photoimage = tk.PhotoImage(master=self, file=self.image_path)
        self.logo_label = tk.Label(master=self, image=self.logo_photoimage, width=128, height=128)
        self.logo_label.grid(row=0, columnspan=2, sticky=tk.S, padx=10, pady=10)

        # Welcome heading
        self.login_title = tk.Label(master=self, \
            text="Welcome to Music School Management System", \
            font=("Arial Bold", 20))
        self.login_title.grid(row=1, columnspan=2, padx=10, pady=10)

        # Username label widget
        self.username_label = tk.Label(master=self, text="Username:")
        self.username_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)

        # Username variable and entry widget
        self.username_var = tk.StringVar(master=self)
        self.username_entry = tk.Entry(master=self, textvariable=self.username_var)
        self.username_entry.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

        # Password label widget
        self.password_label = tk.Label(master=self, text="Password:")
        self.password_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.E)

        # Password variable and entry widget
        self.password_var = tk.StringVar(master=self)
        self.password_entry = tk.Entry(master=self, textvariable=self.password_var, show="●")
        self.password_entry.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)

        # Alert variable and label widget - displays alert messages where necessary
        self.alert_var = tk.StringVar(master=self)
        self.alert_label = tk.Label(master=self, textvariable=self.alert_var)
        self.alert_label.grid(row=4, columnspan=2, padx=10, pady=10)

        # Button to login
        self.login_button = tk.Button(master=self, text="Login", command=self.login)
        self.login_button.grid(row=5, columnspan=2, padx=10, pady=10)

        # Button to shut down
        self.shutdown_button = tk.Button(master=self, text="Shut down", command=master.destroy)
        self.shutdown_button.grid(row=6, columnspan=2, padx=10, pady=10)

    def login(self):
        """
        Method to handle the login upon button click.

        Parameter(s):
        (None)

        Return(s):
        (None)
        """

        app_user = AppUser.authenticate(self.username_var.get(), self.password_var.get())
        mentor = Mentor.authenticate(self.username_var.get(), self.password_var.get())
        # Checks if receptionist_user is an instance of the User class (i.e. authentication is successful)
        # https://docs.python.org/3/library/functions.html#isinstance
        if isinstance(app_user, AppUser):
            self.master.hide_loginpage()
            self.app_user_home_page = AppUserHomePage(self.master, app_user)
            self.app_user_home_page.show_menu()

        elif isinstance(mentor, Mentor):
            self.master.hide_loginpage()
            self.teacher_home_page = TeacherHomePage(self.master, mentor)
            self.teacher_home_page.show_menu()


        else:
            self.alert_var.set("Login Unsuccessful.")
        self.password_var.set("")
        self.username_var.set("")
        
		

if __name__ == "__main__":
    # DO NOT MODIFY
    pass