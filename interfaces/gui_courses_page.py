
# Third party imports
import tkinter as tk
from tkinter import ttk

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

        self.title = tk.Label(self, text="Courses Page")
        self.title.pack(padx=10, pady=10)
        
        # Return to menu button
        self.return_button = tk.Button(self, text="Return to Menu", command=self.return_to_menu)
        self.return_button.pack(padx=10, pady=10)
        
        #Courses notebook
        courses_notebook = ttk.Notebook(self)
        self.PY_tab = ttk.Frame(courses_notebook)  
        self.AI_tab = ttk.Frame(courses_notebook) 
        self.IS_tab = ttk.Frame(courses_notebook)  
        courses_notebook.add(self.PY_tab, text="Python Programming")
        courses_notebook.add(self.AI_tab, text="Artificial Intelligence")
        courses_notebook.add(self.IS_tab, text="Information Security")   
        courses_notebook.pack(expand=True, fill="both", padx=10, pady=10)
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
        tk.Label(self.PY_tab, text="Python Programming", font=('Arial', 14)).pack(pady=20)
        tk.Label(self.PY_tab, text="Mentor: James V", font=('Arial', 12)).pack(pady=20)

        #Lesson modules
        tk.Button(self.PY_tab, text="Lesson 1", font=('Arial', 14)).pack(pady=20)
        tk.Button(self.PY_tab, text="Lesson 2", font=('Arial', 14)).pack(pady=20)
        tk.Button(self.PY_tab, text="Lesson 3", font=('Arial', 14)).pack(pady=20)

    def AI_tab_content(self):
        tk.Button(self.AI_tab, text="Lesson 1", font=('Arial', 14)).pack(pady=20)
    
    def IS_tab_content(self):
        tk.Button(self.IS_tab, text="Lesson 1", font=('Arial', 14)).pack(pady=20)
        

        

if __name__ == "__main__":
    # DO NOT MODIFY
    pass