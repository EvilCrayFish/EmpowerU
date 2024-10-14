
# Third party imports
import tkinter as tk
from tkinter import ttk
from gui_lesson_page import LessonPage

class CoursesPage(tk.Frame):
    def __init__(self, master, homepage, app_user):
        """
        Constructor for the CommunityPage class.

        Parameters:
        - master: master widget of this widget instance
        - receptionist_menu: an instance of the ReceptionistMenu class
        - receptionist_user: an instance of the ReceptionistUser class
        """
        #TODO FIX GUI layout
        #needs to get the progress information from the user profile then visualise it.
        super().__init__(master)
        self.master = master
        self.homepage = homepage
        self.app_user = app_user

        self.grid(row=0, column=0, sticky="nsew")
        self.grid_columnconfigure(0, weight=0)
        self.grid_rowconfigure(0, weight=0)

        # Top Frame (titleframe)
        self.titleframe = tk.Frame(self, bd=5, relief="groove", width=1280)
        self.titleframe.grid(row=0, column=0, sticky="nsew", columnspan=2)
        self.titleframe.grid_columnconfigure(0, weight=0)
        self.titleframe.grid_columnconfigure(1, weight=0)
        self.titleframe.grid_columnconfigure(2, weight=1)

        self.login_title = tk.Label(master=self.titleframe, text="EMPOWERU", font=("Arial Bold", 30))
        self.login_title.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)
    
        self.course_label = tk.Label(master=self.titleframe, text="Courses Page", font=("Arial", 10))
        self.course_label.grid(row=0, column=2, padx=10, pady=(10, 10), sticky=tk.W)  # Adjust pady to position it below the title
        
        # Home button to return to the homepage
        self.home_button = tk.Button(master=self.titleframe, text="Home", command=self.return_to_menu)
        self.home_button.grid(row=0, column=3, padx=10, pady=10, sticky=tk.E)  # Sticks to the right side of column 3

        # Make the titleframe expand and occupy available space
        self.grid_columnconfigure(0, weight=0)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=1)  #notebook
        
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
        This method handles the GUI logic to return to the receptionist's menu.

        Parameters:
        (None)

        Returns:
        (None)
        """
        self.place_forget()
        self.homepage.place(relx=.5, rely=.5, anchor=tk.CENTER)

    def PY_tab_content(self):
        self.create_course_label(self.PY_tab, "Python Programming", "James V")

        # Lesson modules
        tk.Button(self.PY_tab, text="Lesson 1", font=('Arial', 14), 
                  command=lambda: self.open_lesson("Python Programming", "Lesson 1")).grid(row=2, column=0, pady=10, padx=10)
        tk.Button(self.PY_tab, text="Lesson 2", font=('Arial', 14)).grid(row=2, column=1, padx=10,  pady=10)
        tk.Button(self.PY_tab, text="Lesson 3", font=('Arial', 14)).grid(row=2, column=2, padx=10,  pady=10)

    def AI_tab_content(self):
        self.create_course_label(self.AI_tab, "Artificial Intelligence", "James V")

        tk.Button(self.AI_tab, text="Lesson 1", font=('Arial', 14)).grid(row=2, column=0, pady=10)
        tk.Button(self.AI_tab, text="Lesson 2", font=('Arial', 14)).grid(row=2, column=1, padx=10, pady=10)
        tk.Button(self.AI_tab, text="Lesson 3", font=('Arial', 14)).grid(row=2, column=2, padx=10, pady=10)

    def IS_tab_content(self):
        self.create_course_label(self.IS_tab, "Information Security", "James V")

        tk.Button(self.IS_tab, text="Lesson 1", font=('Arial', 14)).grid(row=2, column=0, pady=10)
        tk.Button(self.IS_tab, text="Lesson 2", font=('Arial', 14)).grid(row=2, column=1, padx=10, pady=10)
        tk.Button(self.IS_tab, text="Lesson 3", font=('Arial', 14)).grid(row=2, column=2, padx=10, pady=10)

    def create_course_label(self, parent, course_name, mentor_name):
        tk.Label(parent, text=course_name, font=('Arial', 14)).grid(row=0, column=0, pady=10)
        tk.Label(parent, text=f"Mentor: {mentor_name}", font=('Arial', 12)).grid(row=1, column=0, pady=10)

    def open_lesson(self, course_name, lesson_name):
        lesson_page = self.LessonPage(self.master, course_name, lesson_name, self)
        self.grid_forget() 
        lesson_page.grid(row=0, column=0, sticky="nsew")

if __name__ == "__main__":
    # DO NOT MODIFY
    pass