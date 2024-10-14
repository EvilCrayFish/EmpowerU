"""
Contains class definition for the LessonPage window
"""

# Third party imports
import tkinter as tk
from tkinter import ttk

class LessonPage(tk.Frame):
    def __init__(self, master, course_name, lesson_name, homepage, app_user):
        super().__init__(master)
        self.master = master
        self.homepage = homepage
        self.course_name = course_name
        self.lesson_name = lesson_name
        self.app_user = app_user
        
        self.grid(row=0, column=0, sticky="nsew")

        self.title_label = tk.Label(self, text=f"{self.course_name} - {self.lesson_name}", font=("Arial Bold", 24))
        self.title_label.grid(row=0, column=0, padx=20, pady=20)

        # Lesson content --> display generated content from data (.txt)
        self.content_label = tk.Label(self, text="Lesson content goes here", font=("Arial", 14))
        self.content_label.grid(row=1, column=0, padx=20, pady=20)

        # Back to course page button
        self.back_button = tk.Button(self, text="Back to Courses", command=self.go_back_to_courses)
        self.back_button.grid(row=2, column=0, padx=20, pady=20)

    def go_back_to_courses(self):
        """
        Go back to the main course page.
        """
        self.grid_forget()  # Hide the lesson page
        self.homepage.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.homepage.grid(row=0, column=0, sticky="nsew")  # Show the course page

if __name__ == "__main__":
    # DO NOT MODIFY
    pass