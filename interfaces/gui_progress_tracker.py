# Third party imports
import tkinter as tk

class ProgressTracker(tk.Frame):
    def __init__(self, master, homepage, app_user):
        """
        Constructor for the ProgressTracker class.
        
        Parameters:
        - master: master widget of this widget instance
        - homepage: an instance of the HomePage class
        - app_user: an instance of the User class

        Returns:
        (None)
        """
        super().__init__(master)
        self.master = master
        self.homepage = homepage
        self.app_user = app_user
        self.title = tk.Label(self, text="Progress Tracker", font=("Arial Bold", 20))
        self.title.pack(padx=10, pady=10)
        # Return to menu button
        self.return_button = tk.Button(self, text="Return to Menu", command=self.return_to_menu)
        self.return_button.pack(padx=10, pady=10)

        self.programming_title = tk.Label(self, text="Python Programming")
        self.programming_title.pack()
        programming_lessons_data = self.measure_lesson_progress("PY")
        self.programming_lessons = tk.Label(self, text=f"{programming_lessons_data[0]}/{programming_lessons_data[1]}")
        self.programming_lessons.pack()
        self.programming_percent = tk.Label(self, text=f"{programming_lessons_data[2]}%\n")
        self.programming_percent.pack()

        self.ai_title = tk.Label(self, text="Artificial Intelligence")
        self.ai_title.pack()
        ai_lessons_data = self.measure_lesson_progress("AI")
        self.ai_lessons = tk.Label(self, text=f"{ai_lessons_data[0]}/{ai_lessons_data[1]}")
        self.ai_lessons.pack()
        self.ai_percent = tk.Label(self, text=f"{ai_lessons_data[2]}%\n")
        self.ai_percent.pack()
        
        self.is_title = tk.Label(self, text="Information Security")
        self.is_title.pack()
        is_lessons_data = self.measure_lesson_progress("IS")
        self.is_lessons = tk.Label(self, text=f"{is_lessons_data[0]}/{is_lessons_data[1]}")
        self.is_lessons.pack()
        self.is_percent = tk.Label(self, text=f"{is_lessons_data[2]}%\n")
        self.is_percent.pack()

    def measure_lesson_progress(self, course):
        """
        Reads lessons.txt to find number of complete lessons and number of total lessons in a course.
        
        Parameters:
        - course: the course being searched for
        
        Returns:
        - list: number of completed lessons in the course, number of lessons in course.
        """
        lessons = 0
        completed_lessons = 0
        with open("data\\lessons.txt", "r") as filer:
            for line in filer.readlines():
                line_information = line.strip().split(";")
                if course == line_information[0]:
                    lessons += 1
                    if line_information[3] == "Complete":
                        completed_lessons += 1
        try:
            percent = completed_lessons / lessons * 100
        except ZeroDivisionError:
            percent = 100.0
        return [completed_lessons, lessons, percent]

    def return_to_menu(self):
        """
        This method handles the GUI logic to return to the receptionist's menu.
        
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
