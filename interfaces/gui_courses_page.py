
# Third party imports
import tkinter as tk
from tkinter import ttk
from interfaces.gui_lesson_page import LessonPage


class CoursesPage(tk.Frame):
    def __init__(self, master, homepage, app_user):
        super().__init__(master)
        self.master = master
        self.homepage = homepage
        self.app_user = app_user
        self.image_path = "./images/logo.png"

        self.grid(row=0, column=0, sticky="nsew")

        # Top Frame (titleframe)
        self.titleframe = tk.Frame(self, bd=5, relief="groove", width=1280)
        self.titleframe.grid(row=0, column=0, sticky="nsew", columnspan=4)
        self.titleframe.grid_columnconfigure(0, weight=0)
        self.titleframe.grid_columnconfigure(1, weight=0)
        self.titleframe.grid_columnconfigure(2, weight=0)
        
        self.logo_photoimage = tk.PhotoImage(master=self, file=self.image_path)
        self.logo_label = tk.Label(master=self.titleframe, image=self.logo_photoimage, width=128, height=128)
        self.logo_label.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)

        self.login_title = tk.Label(master=self.titleframe, text="EMPOWERU", font=("Arial Bold", 30))
        self.login_title.grid(row=0, column=1, sticky=tk.W)
    
        self.course_label = tk.Label(master=self.titleframe, text="Courses Page", font=("Arial", 10))
        self.course_label.grid(row=0, column=2, padx=10, pady=(10, 10), sticky=tk.W)  # Adjust pady to position it below the title
        
        # Home button to return to the homepage
        self.home_button = tk.Button(master=self.titleframe, text="Home", command=self.return_to_menu)
        self.home_button.grid(row=0, column=3, padx=10, pady=10, sticky=tk.E)
        
        #Courses notebook
        courses_notebook = ttk.Notebook(self)
        self.PY_tab = ttk.Frame(courses_notebook)  
        self.AI_tab = ttk.Frame(courses_notebook) 
        self.IS_tab = ttk.Frame(courses_notebook)  
        courses_notebook.add(self.PY_tab, text="Python Programming")
        courses_notebook.add(self.AI_tab, text="Artificial Intelligence")
        courses_notebook.add(self.IS_tab, text="Information Security")   
        courses_notebook.grid(row=1, column=0, columnspan=2, sticky="nsew")
        self.PY_tab_content()
        self.AI_tab_content()
        self.IS_tab_content()

    def return_to_menu(self):
        """
        Return to the homepage.
        """
        self.place_forget()
        self.grid_forget()
        self.homepage.place(relx=.5, rely=.5, anchor=tk.CENTER)

    def PY_tab_content(self):
        self.create_course_label(self.PY_tab, "Python Programming", "James V")

        # Lesson modules
        lessons = self.read_lessons("PY")
        for i in range(len(lessons)):
            tk.Button(self.PY_tab, text=lessons[i], font=('Arial', 14), 
                  command=lambda lesson_name=lessons[i]: self.show_lesson_page("PY", lesson_name)).grid(row=2, column=i, pady=10, padx=10)
            
        # tk.Button(self.PY_tab, text="Lesson 1", font=('Arial', 14), 
        #           command=lambda: self.show_lesson_page("Programming", "Lesson 1")).grid(row=2, column=0, pady=10, padx=10)
        # tk.Button(self.PY_tab, text="Lesson 2", font=('Arial', 14),
        #           command=lambda: self.show_lesson_page("Programming", "Lesson 2")).grid(row=2, column=1, pady=10, padx=10)
        # tk.Button(self.PY_tab, text="Lesson 3", font=('Arial', 14),
        #           command=lambda: self.show_lesson_page("Programming", "Lesson 3")).grid(row=2, column=2, pady=10, padx=10)

    def AI_tab_content(self):
        self.create_course_label(self.AI_tab, "Artificial Intelligence", "James V")

        lessons = self.read_lessons("AI")
        for i in range(len(lessons)):
            tk.Button(self.AI_tab, text=lessons[i], font=('Arial', 14), 
                  command=lambda lesson_name=lessons[i]: self.show_lesson_page("AI", lesson_name)).grid(row=2, column=i, pady=10, padx=10)

    def IS_tab_content(self):
        self.create_course_label(self.IS_tab, "Information Security", "James V")

        lessons = self.read_lessons("IS")
        for i in range(len(lessons)):
            tk.Button(self.IS_tab, text=lessons[i], font=('Arial', 14), 
                  command=lambda lesson_name=lessons[i]: self.show_lesson_page("IS", lesson_name)).grid(row=2, column=i, pady=10, padx=10)

    def create_course_label(self, parent, course_name, mentor_name):
        tk.Label(parent, text=course_name, font=('Arial', 14)).grid(row=0, column=0, pady=10)
        tk.Label(parent, text=f"Mentor: {mentor_name}", font=('Arial', 10)).grid(row=0, column=1, pady=10)

    def show_lesson_page(self, course_name, lesson_name):
        lesson_page = LessonPage(self.master, course_name, lesson_name, self, app_user=self.app_user)
        self.place_forget() 
        lesson_page.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        #lesson_page.grid(row=0, column=0, sticky="nsew")

    def read_lessons(self, course):
        """
        Reads lessons.txt to find all stored information about all lessons

        Parameters:
        course - the course being searched for

        Returns:
        res - list of lesson names part of the course specfied in the parameter
        """
        res = []

        with open("data\\lessons.txt", "r") as filer:
            for line in filer.readlines():
                line_information = line.strip().split(";")
                if course == line_information[0]:
                    res.append(line_information[1])

        return res
                    

if __name__ == "__main__":
    # DO NOT MODIFY
    pass