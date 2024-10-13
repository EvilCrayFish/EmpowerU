"""
THIS IS THE ONLY FILE YOU SHOULD CHANGE

Change the init section to create the page.
"""

# Third party imports
import tkinter as tk
from tkinter import ttk

class Layout(tk.Frame):
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
        self.image_path = "./images/logo.png"

        self.grid(row=0, column=0, sticky="nsew")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)

        # Top Frame (titleframe)
        self.titleframe = tk.Frame(self, bd=5, relief="groove", width=1280)
        self.titleframe.grid(row=0, column=0, sticky="nsew", columnspan=2)

        self.logo_photoimage = tk.PhotoImage(master=self, file=self.image_path)
        self.logo_label = tk.Label(master=self.titleframe, image=self.logo_photoimage, width=128, height=128)
        self.logo_label.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)

        self.login_title = tk.Label(master=self.titleframe, text="EMPOWERU", font=("Arial Bold", 30))
        self.login_title.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)
    
        self.course_label = tk.Label(master=self.titleframe, text="Courses Page", font=("Arial", 10))
        self.course_label.grid(row=0, column=2, padx=10, pady=(10, 10), sticky=tk.W)  # Adjust pady to position it below the title
        
        # Home button to return to the homepage
        self.home_button = tk.Button(master=self.titleframe, text="Home", command=self.return_to_menu)
        self.home_button.grid(row=0, column=3, padx=10, pady=10, sticky=tk.E)  # Sticks to the right side of column 3

        # Make the titleframe expand and occupy available space
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=10)  #notebook
        
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
        tk.Label(self.PY_tab, text="Python Programming", font=('Arial', 14)).grid(row=0, column=0, pady=10)
        tk.Label(self.PY_tab, text="Mentor: James V", font=('Arial', 12)).grid(row=1, column=0, pady=10)

        # Lesson modules
        tk.Button(self.PY_tab, text="Lesson 1", font=('Arial', 14)).grid(row=2, column=0, pady=10)
        tk.Button(self.PY_tab, text="Lesson 2", font=('Arial', 14)).grid(row=3, column=0, pady=10)
        tk.Button(self.PY_tab, text="Lesson 3", font=('Arial', 14)).grid(row=4, column=0, pady=10)

    def AI_tab_content(self):
        tk.Label(self.AI_tab, text="Artificial Intelligence", font=('Arial', 14)).grid(row=0, column=0, pady=10)
        tk.Label(self.AI_tab, text="Mentor: James V", font=('Arial', 12)).grid(row=1, column=0, pady=10)

        tk.Button(self.AI_tab, text="Lesson 1", font=('Arial', 14)).grid(row=2, column=0, pady=10)
        tk.Button(self.AI_tab, text="Lesson 2", font=('Arial', 14)).grid(row=3, column=0, pady=10)
        tk.Button(self.AI_tab, text="Lesson 3", font=('Arial', 14)).grid(row=4, column=0, pady=10)

    def IS_tab_content(self):
        tk.Label(self.IS_tab, text="Information Security", font=('Arial', 14)).grid(row=0, column=0, pady=10)
        tk.Label(self.IS_tab, text="Mentor: James V", font=('Arial', 12)).grid(row=1, column=0, pady=10)

        tk.Button(self.IS_tab, text="Lesson 1", font=('Arial', 14)).grid(row=2, column=0, pady=10)
        tk.Button(self.IS_tab, text="Lesson 2", font=('Arial', 14)).grid(row=3, column=0, pady=10)
        tk.Button(self.IS_tab, text="Lesson 3", font=('Arial', 14)).grid(row=4, column=0, pady=10)

if __name__ == "__main__":
    # DO NOT MODIFY
    pass