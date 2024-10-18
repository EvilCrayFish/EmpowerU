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

        self.lesson_information = self.get_lesson_line()
        self.lesson_contents = self.lesson_information[2]
        self.lesson_status = self.lesson_information[3]
        
        self.grid(row=0, column=0, sticky="nsew")
        self.title_label = tk.Label(self, text=f"{self.course_name} - {self.lesson_name}", font=("Arial Bold", 24))
        self.title_label.grid(row=0, column=0, padx=20, pady=20)

        self.status_label = tk.Label(self, text=self.lesson_status)
        self.status_label.grid(row=0,column=3, padx=20, pady=20)

        # Lesson content --> display generated content from data (.txt)
        self.content_label = tk.Label(self, text=self.lesson_contents, font=("Arial", 14))
        self.content_label.grid(row=1, column=0, padx=20, pady=20)

        self.mark_complete_btn = tk.Button(self, text="Mark lesson complete", command=self.mark_complete)
        self.mark_complete_btn.grid(row=0, column=4, padx=20, pady=20)

        # Back to course page button
        self.back_button = tk.Button(self, text="Back to Courses", command=self.go_back_to_courses)
        self.back_button.grid(row=2, column=0, padx=20, pady=20)
        

    def mark_complete(self):
        new_line = []
        other_lines = []
        with open("data\\lessons.txt", "r") as filer:
            for line in filer.readlines():
                line_information = line.strip().split(";")
                if self.course_name == line_information[0] and self.lesson_name == line_information[1]:
                    new_line = f"{self.course_name};{self.lesson_name};{self.lesson_contents};Complete\n"
                else:
                    other_lines.append(line)
        
        with open("data\\lessons.txt", "w") as filer:
            for line in other_lines:
                filer.write(line)
            filer.write(new_line)
        
        self.go_back_to_courses()


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


    def go_back_to_courses(self):
        """
        Go back to the main course page.
        """
        self.place_forget()
        self.grid_forget()  # Hide the lesson page
        self.homepage.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        #self.homepage.grid(row=0, column=0, sticky="nsew")  # Show the course page

if __name__ == "__main__":
    # DO NOT MODIFY
    pass