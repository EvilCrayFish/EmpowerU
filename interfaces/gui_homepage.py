import tkinter as tk
from tkinter import messagebox

from interfaces.gui_forum_page import ForumPage
from interfaces.gui_progress_tracker import ProgressTracker
from interfaces.gui_courses_page import CoursesPage
from classes.cls_app_user import AppUser
from classes.cls_mentor import Mentor

class HomePage(tk.Frame):
    def __init__(self, master, user):
        """
        Constructor for the HomePage class.

        Parameters:
        - master: The main application window.
        - user: An instance representing the logged-in user (AppUser or Mentor).
        """
        super().__init__(master=master)
        self.master = master
        self.user = user

        self.grid_columnconfigure(0, weight=1)  # Center content horizontally
        self.grid_rowconfigure(0, weight=1)

        # Main container frame with padding
        self.main_frame = tk.Frame(self, padx=30, pady=30)
        self.main_frame.grid(row=0, column=0, sticky="nsew")

        # Dynamic welcome message
        user_type = "USER" if isinstance(user, AppUser) else "TEACHER"
        self.welcome_label = tk.Label(
            self.main_frame, text=f"Welcome, {user.first_name}!", 
            font=("Arial Bold", 24), pady=10
        )
        self.welcome_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Navigation Label
        self.label1 = tk.Label(
            self.main_frame, text="Please choose one of the following:", 
            font=("Arial", 16), pady=10
        )
        self.label1.grid(row=1, column=0, columnspan=2)

        # Buttons for User or Teacher
        if isinstance(user, AppUser):
            self.create_user_buttons()
        else:
            self.create_teacher_buttons()

        # Footer with settings and logout buttons
        self.footer_frame = tk.Frame(self.main_frame)
        self.footer_frame.grid(row=99, column=0, columnspan=2, pady=(30, 0))

        self.options_btn = self.create_styled_button("Settings", command=self.open_settings)
        self.options_btn.grid(row=2, column=0, padx=5)

        self.logout_btn = self.create_styled_button("Log out", command=self.logout)
        self.logout_btn.grid(row=2, column=1, padx=5)

    def create_user_buttons(self):
        """
        Create navigation buttons for AppUser.
        """
        self.courses_btn = self.create_styled_button("Courses", command=self.show_courses_page)
        self.courses_btn.grid(row=3, column=0, pady=10, sticky="ew")

        self.forum_btn = self.create_styled_button("Forum", command=self.show_forum_page)
        self.forum_btn.grid(row=3, column=1, pady=10, sticky="ew")

        self.progress_tracker_btn = self.create_styled_button(
            "Progress Tracker", command=self.show_progress_tracker
        )
        self.progress_tracker_btn.grid(row=4, column=0, pady=10, sticky="ew")

    def create_teacher_buttons(self):
        """
        Create navigation buttons for Mentor.
        """
        self.register_btn = self.create_styled_button("Register a Student")
        self.register_btn.grid(row=3, column=0, pady=10, sticky="ew")

        self.search_btn = self.create_styled_button(
            "Search Teachers by Instrument", command=self.show_search_teachers_frame
        )
        self.search_btn.grid(row=4, column=0, pady=10, sticky="ew")

        self.class_btn = self.create_styled_button("Create Scheduled Class")
        self.class_btn.grid(row=5, column=0, pady=10, sticky="ew")

    def create_styled_button(self, text, command=None):
        """
        Create a styled button with consistent hover effects.

        Parameters:
        - text: The text to display on the button.
        - command: The function to call when the button is clicked.

        Returns:
        - A styled Tkinter button.
        """
        button = tk.Button(
            self.main_frame, text=text, font=("Arial", 14), width=25, command=command
        )

        def on_enter(event):
            button.config(relief="raised", bg="#e0e0e0")

        def on_leave(event):
            button.config(relief="flat", bg="SystemButtonFace")

        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)

        return button

    def show_progress_tracker(self):
        """
        Navigate to the Progress Tracker page.
        """
        progress_page = ProgressTracker(self.master, self, self.user)
        progress_page.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.hide_menu()

    def show_courses_page(self):
        """
        Navigate to the Courses page.
        """
        courses_page = CoursesPage(self.master, self, self.user)
        courses_page.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.hide_menu()

    def show_forum_page(self):
        """
        Navigate to the Forum page.
        """
        forum_page = ForumPage(self.master, self, self.user)
        forum_page.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.hide_menu()

    def show_search_teachers_frame(self):
        """
        Navigate to the Search Teachers page.
        """
        # search_teachers = SearchTeachers(self.master, self, self.user)
        # search_teachers.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.hide_menu()

    def logout(self):
        """
        Log out the current user and show the login page.
        """
        self.hide_menu()
        self.master.show_loginpage()

    def open_settings(self):
        """
        Open the settings page (currently placeholder).
        """
        messagebox.showinfo("Settings", "Settings page is under development.")

    def show_menu(self):
        """
        Display the HomePage frame.
        """
        self.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def hide_menu(self):
        """
        Hide the HomePage frame.
        """
        self.place_forget()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Home Page")
    root.geometry("500x600")  # Adjust window size as needed
    user = AppUser("John", "Doe")  # Example user object
    HomePage(root, user).grid(sticky="nsew")
    root.mainloop()






# """
# #TODO File header pls
# """


# # Third party imports
# import tkinter as tk

# # Local application imports

# from interfaces.gui_forum_page import ForumPage
# from interfaces.gui_progress_tracker import ProgressTracker
# from interfaces.gui_courses_page import CoursesPage
# from classes.cls_app_user import AppUser
# from classes.cls_mentor import Mentor

# class HomePage(tk.Frame):

#     def __init__(self, master, user):
#         """
#         Constructor for the ReceptionistMenu

#         Parameter(s):
#         - master: master widget of this widget instance
#         - user: an instance of the ReceptionistUser class
#                              representing the receptionist that has 
#                              successfully logged in
#         """
#         super().__init__(master=master)
#         self.master = master
#         self.user = user
        
#         if isinstance(user, AppUser): #User Homepage
#             self.welcome_label = tk.Label(self, text=f"Welcome in USER, {user.first_name}!")
#             self.welcome_label.pack(padx=10, pady=10)

#             self.label1 = tk.Label(self, text="Choose one of the following:")
#             self.label1.pack(padx=10, pady=10)

#             self.courses_btn = tk.Button(self, text="Courses", command=self.show_courses_page)
#             self.courses_btn.pack(padx=10, pady=10)

#             self.fourm_btn = tk.Button(self, text="Forum", command=self.show_forum_page)
#             self.fourm_btn.pack(padx=10, pady=10)

#             self.progress_tracker_btn = tk.Button(self, text="Progress Tracker", command=self.show_progress_tracker)
#             self.progress_tracker_btn.pack(padx=10, pady=10)

#             self.options_btn = tk.Button(self, text="Settings")
#             self.progress_tracker_btn.pack(padx=10, pady=10)

#             self.logout_btn = tk.Button(self, text="Log out", command=self.logout)
#             self.logout_btn.pack(padx=10, pady=10)
        
#         else: #Teacher Homepage
#             #TODO Navigation for Teacher
#             self.welcome_label = tk.Label(self, text=f"Welcome in TEACHER, {user.first_name}!")
#             self.welcome_label.pack(padx=10, pady=10)

#             self.label1 = tk.Label(self, text="Choose one of the following:")
#             self.label1.pack(padx=10, pady=10)

#             self.register_btn = tk.Button(self, text="Register a student")
#             self.register_btn.pack(padx=10, pady=10)

#             self.search_btn = tk.Button(self, text="Search teachers by instrument", command=self.show_search_teachers_frame)
#             self.search_btn.pack(padx=10, pady=10)

#             self.class_btn = tk.Button(self, text="Create a weekly scheduled class")
#             self.class_btn.pack(padx=10, pady=10)

#             self.logout_btn = tk.Button(self, text="Log out", command=self.logout)
#             self.logout_btn.pack(padx=10, pady=10)

#     def show_progress_tracker(self):
#         """
#         Method to handle the search teachers functionality upon button click.
#         """
#         progress_page = ProgressTracker(self.master, self, self.user)
#         progress_page.place(relx=.5, rely=.5, anchor=tk.CENTER)
#         self.hide_menu()
        
#     def show_courses_page(self):
#         """
#         Method to handle the search teachers functionality upon button click.
#         """
#         courses_page = CoursesPage(self.master, self, self.user)
#         courses_page.place(relx=.5, rely=.5, anchor=tk.CENTER)
#         self.hide_menu()


#     def show_search_teachers_frame(self):
#         """
#         Method to handle the search teachers functionality upon button click.
#         """
#         #search_teachers = SearchTeachers(self.master, self, self.user)
#         #search_teachers.place(relx=.5, rely=.5, anchor=tk.CENTER)
#         self.hide_menu()

#     def show_forum_page(self):
#         """
#         Method to handle the search teachers functionality upon button click.
#         """
#         forum_page = ForumPage(self.master, self, self.user)
#         forum_page.place(relx=.5, rely=.5, anchor=tk.CENTER)
#         self.hide_menu()


#     def logout(self):
#         """
#         Method to handle the logout upon button click.

#         Parameter(s):
#         (None)

#         Return(s):
#         (None)
#         """
#         self.hide_menu()
#         self.master.show_loginpage()

#     def show_menu(self):
#         """
#         Method to show the receptionist menu in the main window.
#         """
#         self.place(relx=.5, rely=.5, anchor=tk.CENTER)

#     def hide_menu(self):
#         """
#         Method to hide the receptionist menu frame.
#         """
#         self.place_forget()


# if __name__ == "__main__":
#     # DO NOT MODIFY
#     pass
