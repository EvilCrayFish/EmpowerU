"""
FIT1056 2024 Semester 2
EmpowerU Project
Team G08

Contains class definition for the EditLessonPage window
"""


# Third party imports
import tkinter as tk
from tkinter import ttk
from classes.cls_mentor import Mentor
from classes.cls_staff import Staff

class EditLessonPage(tk.Frame):
    def __init__(self, master, course_name, lesson_name, homepage, app_user):
        """
        Constructor for the EditLessonPage class.

        Parameters:
        - master: master widget of this widget instance
        - course_name: name of the course
        - lesson_name: name of the lesson
        - homepage: an instance of the homepage
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
        self.lesson_information = self.get_lesson_line()
        self.lesson_contents = self.lesson_information[2]
        self.lesson_status = self.lesson_information[3]
        
        self.grid(row=0, column=0, sticky="nsew")
        self.title_label = tk.Label(self, text=f"{self.course_name} - {self.lesson_name}", font=("Arial Bold", 24))
        self.title_label.grid(row=0, column=1, padx=20, pady=20)
        # Lesson content --> display generated content from data (.txt)
        self.content_entry = tk.Text(self, height=10, width=50)
        self.content_entry.insert(tk.END, self.lesson_contents.replace("*", "\n"))
        self.content_entry.grid(row=1, column=0)
        self.content_btn = tk.Button(self, text="Update lesson contents", command=self.update_content)
        self.content_btn.grid(row=1, column=1)
        self.delete_btn = tk.Button(self, text="Delete lesson", command=self.delete_lesson)
        self.delete_btn.grid(row=2, column=0, padx=20, pady=20)
        # Back to course page button
        self.back_button = tk.Button(self, text="Back to home", command=self.go_back_to_home)
        self.back_button.grid(row=0, column=0, padx=20, pady=20)

    def update_content(self):
        """
        Reads lessons.txt into a list, but appends the edited lesson with the modified contents.
        Clears lessons.txt, and then adds all the lessons into lessons.txt from the list.

        Parameters:
        (None)

        Returns:
        (None)
        """
        self.content_var = self.content_entry.get("1.0", tk.END).strip()
        self.content_var = self.content_var.replace("\n", "*")
        lines = []
        with open("data\\lessons.txt", "r") as filer:
            for line in filer.readlines():
                line_information = line.strip().split(";")
                if self.course_name == line_information[0] and self.lesson_name == line_information[1]:
                    new_line = f"{self.course_name};{self.lesson_name};{self.content_var};{line_information[3]}\n"
                    lines.append(new_line)
                else:
                    lines.append(line)
        with open("data\\lessons.txt", "w") as filer:
            for line in lines:
                filer.write(line)

    def delete_lesson(self):
        """
        Stores every line of lessons.txt in an array except for the current lesson,
        and then adds those lessons back into lessons.txt after clearing the document.

        Parameters:
        (None)

        Returns:
        (None)
        """
        other_lines = []
        with open("data\\lessons.txt", "r") as filer:  # Reads lines
            for line in filer.readlines():
                line_information = line.strip().split(";")
                if (self.course_name == line_information[0] and self.lesson_name == line_information[1]) == False:
                    other_lines.append(line)
        with open("data\\lessons.txt", "w") as filer:  # Clears lines and adds back
            for line in other_lines:
                filer.write(line)
        self.go_back_to_home()

    def get_lesson_line(self):
        """
        Reads lessons.txt to find all stored information about the lesson

        Returns a list of strings:
        - lesson_information[0] = course name
        - lesson_information[1] = lesson name
        - lesson_information[2] = lesson text contents
        - lesson_information[3] = lesson status

        Parameters:
        (None)

        Returns:
        - list: A list of lesson information strings
        """
        with open("data\\lessons.txt", "r") as filer:
            for line in filer.readlines():
                line_information = line.strip().split(";")
                if self.course_name == line_information[0] and self.lesson_name == line_information[1]:
                    return line_information
        return ["Error: lesson information not found"] * 4

    def go_back_to_home(self):
        """
        Go back to the homepage.

        Parameters:
        (None)

        Returns:
        (None)
        """
        self.place_forget()
        self.grid_forget()  # Hide the edit lesson page
        self.homepage.homepage.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        # self.homepage.grid(row=0, column=0, sticky="nsew")  # Show the course page

if __name__ == "__main__":
    # DO NOT MODIFY
    pass
