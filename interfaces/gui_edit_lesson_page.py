"""
Contains class definition for the EditLessonPage window
"""

# Third party imports
import tkinter as tk
from tkinter import ttk
from classes.cls_mentor import Mentor
from classes.cls_staff import Staff

class EditLessonPage(tk.Frame):
    def __init__(self, master, course_name, lesson_name, homepage, app_user):
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
        self.lesson_contents_var = tk.StringVar()
        self.lesson_contents_var.set(self.lesson_contents)
        self.content_entry = tk.Entry(self, textvariable=self.lesson_contents_var)
        self.content_entry.grid(row=1, column=0)

        self.content_btn = tk.Button(self, text="Update lesson contents", command=self.update_content)
        self.content_btn.grid(row=1, column=1)

        self.delete_btn = tk.Button(self, text="Delete lesson", command=self.delete_lesson)
        self.delete_btn.grid(row=2, column=0, padx=20, pady=20)

        # Back to course page button
        self.back_button = tk.Button(self, text="Back to home", command=self.go_back_to_home)
        self.back_button.grid(row=0, column=0, padx=20, pady=20)


    def update_content(self):
        new_line = []
        other_lines = []
        with open("data\\lessons.txt", "r") as filer:
            for line in filer.readlines():
                line_information = line.strip().split(";")
                if self.course_name == line_information[0] and self.lesson_name == line_information[1]:
                    new_line = f"{self.course_name};{self.lesson_name};{self.lesson_contents_var.get()};{line_information[3]}\n"
                else:
                    other_lines.append(line)
        
        with open("data\\lessons.txt", "w") as filer:
            for line in other_lines:
                filer.write(line)
            filer.write(new_line)


    def delete_lesson(self):
        other_lines = []
        with open("data\\lessons.txt", "r") as filer:
            for line in filer.readlines():
                line_information = line.strip().split(";")
                if (self.course_name == line_information[0] and self.lesson_name == line_information[1]) == False:
                    other_lines.append(line)
        
        with open("data\\lessons.txt", "w") as filer:
            for line in other_lines:
                filer.write(line)

        self.go_back_to_home()


    def get_lesson_line(self):
        """
        Reads lessons.txt to find all stored information about the lesson

        Returns a list of strings - 
        lesson_information[0] = course name
        lesson_information[1] = lesson name
        lesson_information[2] = lesson text contents
        lesson_information[3] = lesson status
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
        """
        self.place_forget()
        self.grid_forget()  # Hide the edit lesson page
        self.homepage.homepage.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        #self.homepage.grid(row=0, column=0, sticky="nsew")  # Show the course page

if __name__ == "__main__":
    # DO NOT MODIFY
    pass