"""
FIT1056 2024 Semester 2
Programming Concepts Task 4

This file contains the class definition for the SearchTeachers class.
"""

# Third party imports
import tkinter as tk

class ForumPage(tk.Frame):
    def __init__(self, master, home_page, user):
        """
        Constructor for the CommunityPage class.

        Parameters:
        - master: master widget of this widget instance
        - receptionist_menu: an instance of the ReceptionistMenu class
        - receptionist_user: an instance of the ReceptionistUser class
        """
        super().__init__(master)
        self.master = master
        self.home_page = home_page
        self.user = user


        self.title = tk.Label(self, text="Forum Page")
        self.title.pack(padx=10, pady=10)

        # Return to menu button
        self.return_button = tk.Button(self, text="Return to Menu", command=self.return_to_menu)
        self.return_button.pack(padx=10, pady=10)



    def return_to_menu(self):
        """
        This method handles the GUI logic to return to the receptionist's menu.

        Parameters:
        (None)

        Returns:
        (None)
        """
        self.place_forget()
        self.home_page.place(relx=.5, rely=.5, anchor=tk.CENTER)

if __name__ == "__main__":
    # DO NOT MODIFY
    pass