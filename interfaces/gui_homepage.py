"""
FIT1056 2024 Semester 2
EmpowerU Project
Team G08

Contains the HomePage Class defintion and GUI layout
"""

# Third party imports
import tkinter as tk
from tkinter import messagebox
from interfaces.gui_forum_page import ForumPage
from interfaces.gui_progress_tracker import ProgressTracker
from interfaces.gui_courses_page import CoursesPage
from interfaces.gui_assignments import AssignmentsPage
from interfaces.gui_create_lesson_page import CreateLessonPage
from classes.cls_app_user import AppUser
from classes.cls_mentor import Mentor

class HomePage(tk.Frame):
    def __init__(self, master, user):
        """
        Constructor for the HomePage class.

        Parameters:
        - master: object - The main application window.
        - user: object - An instance representing the logged-in user (AppUser or Mentor).

        Returns:
        (None)
        """
        super().__init__(master=master)
        self.master = master
        self.user = user
        self.grid_columnconfigure(0, weight=1)  # Center content horizontally
        self.grid_rowconfigure(0, weight=1)
        # Dynamic welcome message
        self.welcome_label = tk.Label(
            self, text=f"Welcome, {user.first_name}!",
            font=("Arial Bold", 24), pady=10
        )
        self.welcome_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        # Navigation Label
        self.label1 = tk.Label(
            self, text="Please choose one of the following:",
            font=("Arial", 16), pady=10
        )
        self.label1.grid(row=1, column=0, columnspan=2)
        # Buttons for User or Teacher
        if isinstance(user, AppUser):
            self.create_user_buttons()
        else:
            self.create_teacher_buttons()
        # Footer with settings and logout buttons
        self.footer_frame = tk.Frame(self)
        self.footer_frame.grid(row=99, column=0, columnspan=2, pady=(30, 0))
        self.options_btn = self.create_styled_button("Settings", command=self.open_settings)
        self.options_btn.grid(row=2, column=0, padx=5)
        self.logout_btn = self.create_styled_button("Log out", command=self.logout)
        self.logout_btn.grid(row=2, column=1, padx=5)

    def create_user_buttons(self):
        """
        Create navigation buttons for AppUser.

        Parameters:
        (None)

        Returns:
        (None)
        """
        self.courses_btn = self.create_styled_button("Courses", command=self.show_courses_page)
        self.courses_btn.grid(row=3, column=0, pady=10, sticky="ew")
        self.forum_btn = self.create_styled_button("Forum", command=self.show_forum_page)
        self.forum_btn.grid(row=3, column=1, pady=10, sticky="ew")
        self.assignments_btn = self.create_styled_button(
            "Assignments", command=self.show_assignments_page
        )
        self.assignments_btn.grid(row=4, column=0, pady=10, sticky="ew")
        self.progress_tracker_btn = self.create_styled_button(
            "Progress Tracker", command=self.show_progress_tracker
        )
        self.progress_tracker_btn.grid(row=4, column=1, pady=10, sticky="ew")

    def create_teacher_buttons(self):
        """
        Create navigation buttons for Mentor.

        Parameters:
        (None)

        Returns:
        (None)
        """
        self.courses_btn = self.create_styled_button("Courses", command=self.show_courses_page)
        self.courses_btn.grid(row=3, column=0, pady=10, sticky="ew")
        self.forum_btn = self.create_styled_button("Forum", command=self.show_forum_page)
        self.forum_btn.grid(row=3, column=1, pady=10, sticky="ew")
        self.assignments_btn = self.create_styled_button(
            "Assignments", command=self.show_assignments_page
        )
        self.assignments_btn.grid(row=4, column=0, pady=10, sticky="ew")
        self.create_lesson_btn = self.create_styled_button(
            "Create Lesson", command=self.show_create_lesson_page
        )
        self.create_lesson_btn.grid(row=4, column=1, pady=10, sticky="ew")

    def create_styled_button(self, text, command=None):
        """
        Create a styled button with consistent hover effects.

        Parameters:
        - text: string - The text to display on the button.
        - command: string - The function to call when the button is clicked.

        Returns:
        - A styled Tkinter
        """
        button = tk.Button(
            self, text=text, font=("Arial", 14), width=25, command=command
        )

        def on_enter(event): #When button is hovered
            button.config(relief="raised", bg="#e0e0e0")

        def on_leave(event): #When button isn't hovered
            button.config(relief="flat", bg="SystemButtonFace")

        button.bind("<Enter>", on_enter) #When button is hovered, trigger on_enter()
        button.bind("<Leave>", on_leave) #When button ceases being hovered, trigger on_leave()

        return button

    def show_progress_tracker(self):
        """
        Navigate to the Progress Tracker page.

        Parameters:
        (None)

        Returns:
        (None)
        """
        progress_page = ProgressTracker(self.master, self, self.user)
        progress_page.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.hide_menu()

    def show_courses_page(self):
        """
        Navigate to the Courses page.

        Parameters:
        (None)

        Returns:
        (None)
        """
        courses_page = CoursesPage(self.master, self, self.user)
        courses_page.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.hide_menu()

    def show_forum_page(self):
        """
        Navigate to the Forum page.

        Parameters:
        (None)

        Returns:
        (None)
        """
        forum_page = ForumPage(self.master, self, self.user)
        forum_page.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.hide_menu()

    def show_assignments_page(self):
        """
        Navigate to the Assignments page.

        Parameters:
        (None)

        Returns:
        (None)
        """
        assignment_page = AssignmentsPage(self.master, self, self.user)
        assignment_page.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.hide_menu()

    def show_create_lesson_page(self):
        """
        Navigate to the Create Lesson page.

        Parameters:
        (None)

        Returns:
        (None)
        """
        create_lesson_page = CreateLessonPage(self.master, self, self.user)
        create_lesson_page.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.hide_menu()

    def show_search_teachers_frame(self):
        """
        Navigate to the Search Teachers page.

        Parameters:
        (None)

        Returns:
        (None)
        """
        # search_teachers = SearchTeachers(self.master, self, self.user)
        # search_teachers.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.hide_menu()

    def logout(self):
        """
        Log out the current user and show the login page.

        Parameters:
        (None)

        Returns:
        (None)
        """
        self.hide_menu()
        self.master.show_loginpage()

    def open_settings(self):
        """
        Open the settings page (currently placeholder).

        Parameters:
        (None)

        Returns:
        (None)
        """
        messagebox.showinfo("Settings", "Settings page is under development.")

    def show_menu(self):
        """
        Display the HomePage frame.

        Parameters:
        (None)

        Returns:
        (None)
        """
        self.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def hide_menu(self):
        """
        Hide the HomePage frame.

        Parameters:
        (None)

        Returns:
        (None)
        """
        self.place_forget()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Home Page")
    root.geometry("500x600")  # Adjust window size as needed
    user = AppUser("John", "Doe")  # Example user object
    HomePage(root, user).grid(sticky="nsew")
    root.mainloop()




