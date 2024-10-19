"""FIT1056 2024 Semester 2
EmpowerU Project
Team G08
Contains class definition for the LessonPage window.
"""

# Imports
import os
import tkinter as tk
from tkinter import ttk
from classes.cls_mentor import Mentor
from classes.cls_staff import Staff
from interfaces.gui_edit_lesson_page import EditLessonPage

class LessonPage(tk.Frame):
    def __init__(self, master, course_name, lesson_name, homepage, app_user):
        """
        Constructor for the LessonPage class.
        
        Parameters:
        - master: master widget of this widget instance
        - course_name: name of the course
        - lesson_name: name of the lesson
        - homepage: an instance of the HomePage class
        - app_user: an instance of the app user

        Returns:
        (None)
        """
        super().__init__(master)
        self.master = master
        self.homepage = homepage
        self.course_name = course_name
        self.lesson_name = lesson_name
        self.app_user = app_user
        self.image_path = "./images/logo.png"
        self.lesson_information = self.get_lesson_line()
        self.lesson_contents = self.lesson_information[2].replace("*", "\n")
        self.lesson_status = self.lesson_information[3]
        self.grid(row=0, column=0, sticky="nsew")

        # Top Frame 
        self.titleframe = tk.Frame(self, bd=5, relief="groove", width=1280)
        self.titleframe.grid(row=0, column=0, sticky="nsew", columnspan=2)
        self.titleframe.grid_columnconfigure(0, weight=0)
        self.titleframe.grid_columnconfigure(1, weight=0)
        self.titleframe.grid_columnconfigure(2, weight=0)
        
        self.logo_photoimage = tk.PhotoImage(master=self, file=self.image_path)
        self.logo_label = tk.Label(master=self.titleframe, image=self.logo_photoimage, width=128, height=128)
        self.logo_label.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)
        self.login_title = tk.Label(master=self.titleframe, text="EMPOWERU", font=("Arial Bold", 30))
        self.login_title.grid(row=0, column=1, sticky=tk.W)
        self.course_label = tk.Label(master=self.titleframe, text="Lessons Page", font=("Arial", 10))
        self.course_label.grid(row=0, column=2, padx=10, pady=(10, 10), sticky=tk.W)  # Adjust pady to position it below the title
        self.title_label = tk.Label(self, text=f"{self.course_name} - {self.lesson_name}", font=("Arial Bold", 24))
        self.title_label.grid(row=1, column=0, padx=20, pady=20)
        self.status_label = tk.Label(self, text=f"Lesson status: {self.lesson_status}")
        self.status_label.grid(row=2, column=0, padx=20, pady=20)

        # Return to courses page
        self.back_to_courses_btn = tk.Button(master=self.titleframe, text="Return to Courses", command=self.go_back_to_courses)
        self.back_to_courses_btn.grid(row=0, column=3, padx=10, pady=10, sticky=tk.E)

        # Lesson content
        self.content_label = tk.Label(self, text=self.lesson_contents, font=("Arial", 14))
        self.content_label.grid(row=3, column=0, padx=20, pady=20)

        # Complete button
        self.mark_complete_btn = tk.Button(self, text="Mark lesson complete", command=self.mark_complete)
        self.mark_complete_btn.grid(row=4, column=0, padx=20, pady=20)
        if type(self.app_user) in [Mentor, Staff]:
            self.edit_lesson_btn = tk.Button(master=self.titleframe, text="Edit lesson", command=self.show_edit_lesson_page)
            self.edit_lesson_btn.grid(row=0, column=4, padx=20, pady=20, sticky=tk.E)

    def mark_complete(self):
        """
        Marks the lesson as complete by rewriting the text file,
        with the change of the effected lesson being marked as complete.
        
        Parameters:
        (None)

        Returns:
        (None)
        """
        lines = []
        with open("data\\lessons.txt", "r") as filer:
            for line in filer.readlines():
                line_information = line.strip().split(";")
                if self.course_name == line_information[0] and self.lesson_name == line_information[1]:
                    new_line = f"{self.course_name};{self.lesson_name};{self.lesson_contents};Complete\n"
                    lines.append(new_line)
                else:
                    lines.append(line)
        with open("data\\lessons.txt", "w") as filer:
            for line in lines:
                filer.write(line)
        self.go_back_to_courses()

    def get_lesson_line(self):
        """
        Reads lessons.txt to find all stored information about the lesson
        
        Returns:
        - a list of strings containing lesson details
        """
        with open("data\\lessons.txt", "r") as filer:
            for line in filer.readlines():
                line_information = line.strip().split(";")
                if self.course_name == line_information[0] and self.lesson_name == line_information[1]:
                    return line_information
        return ["Error: lesson information not found"] * 4

    def show_edit_lesson_page(self):
        """
        Display the edit lesson page.
        
        Parameters:
        (None)

        Returns:
        (None)
        """
        self.place_forget()
        self.grid_forget()
        edit_lesson_page = EditLessonPage(self.master, self.course_name, self.lesson_name, self.homepage, self.app_user)
        edit_lesson_page.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def go_back_to_courses(self):
        """
        Go back to the main course page.
        
        Parameters:
        (None)

        Returns:
        (None)
        """
        self.place_forget()
        self.grid_forget()  # Hide the lesson page
        self.homepage.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

if __name__ == "__main__":
    # DO NOT MODIFY
    pass
