"""
FIT1056 2024 Semester 2
Programming Concepts Task 4

This file contains the class definition for the SearchTeachers class.
"""

# Third party imports
import tkinter as tk

class CommunityPage(tk.Frame):
    def __init__(self, master, receptionist_menu, receptionist_user):
        """
        Constructor for the CommunityPage class.

        Parameters:
        - master: master widget of this widget instance
        - receptionist_menu: an instance of the ReceptionistMenu class
        - receptionist_user: an instance of the ReceptionistUser class
        """
        super().__init__(master)
        self.master = master
        self.receptionist_menu = receptionist_menu
        self.receptionist_user = receptionist_user


        self.title = tk.Label(self, text="Search Teacher By Instrument")
        self.title.pack(padx=10, pady=10)

        self.instrument_name = tk.StringVar(master=self)
        self.instrument_entry = tk.Entry(master=self, textvariable=self.instrument_name)
        self.instrument_entry.pack(padx=10, pady=10)

        # Return to menu button
        self.search_button = tk.Button(self, text="Search", command=self.search_teachers_by_instrument)
        self.return_button = tk.Button(self, text="Return to Menu", command=self.return_to_menu)
        self.search_button.pack(padx=10, pady=10)
        self.return_button.pack(padx=10, pady=10)


        self.results_var = tk.StringVar(master=self)
        self.result_label = tk.Label(master=self, textvariable=self.results_var)
        self.result_label.pack(padx=10, pady=10)


    def search_teachers_by_instrument(self):
        """
        This method handles the GUI logic to search teachers by instrument, 
        and display the full names of the teachers that teach the searched 
        instrument name.
        
        Parameters:
        (None)

        Returns:
        (None)
        """
        teachers = self.receptionist_user.list_teachers_by_instrument(self.instrument_name.get())
        teacher_names = ""
        for teacher in teachers:
            teacher_names = teacher_names + teacher.first_name + " " + teacher.last_name+ "\n"
        if teacher_names == "":
            self.results_var.set("No teachers teach this instrument.")
        else:
            self.results_var.set(teacher_names)

        pass


    def return_to_menu(self):
        """
        This method handles the GUI logic to return to the receptionist's menu.

        Parameters:
        (None)

        Returns:
        (None)
        """
        self.place_forget()
        self.receptionist_menu.place(relx=.5, rely=.5, anchor=tk.CENTER)

if __name__ == "__main__":
    # DO NOT MODIFY
    pass