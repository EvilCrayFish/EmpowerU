"""
#TODO File header pls
"""

# Third party imports
import tkinter as tk

# Local application imports
from interfaces.gui_loginpage import LoginPage

class EmpowerU(tk.Tk):

    def __init__(self, title, width, height):
        """
        Constructor for the EmpowerU class.

        Parameter(s):
        - title: str
        - width: int, width of window in pixels
        - height: int, height of window in pixels
        """
        super().__init__()
        super().title(title)
        super().geometry(f"{width}x{height}")

        #TODO Change Image
        self.loginpage = LoginPage(master=self, image_path="./images/logo.png")
        self.show_loginpage()

    def show_loginpage(self):
        """
        Displays the home page to make it visible in the main window.
        """
        self.loginpage.place(relx=.5, rely=.5, anchor=tk.CENTER)

    def hide_loginpage(self):
        """
        Hides the home page to make it invisible in the main window.
        """
        self.loginpage.place_forget()



if __name__ == "__main__":
    # DO NOT MODIFY
    pass