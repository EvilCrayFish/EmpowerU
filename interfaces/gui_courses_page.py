
# Third party imports
import tkinter as tk


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