# Third party imports
import tkinter as tk

# Local application imports
from layouttesting import Layout

class Page(tk.Tk):

    def __init__(self, title, width, height):
        """
        Constructor for the Page class.

        Parameter(s):
        - title: str
        - width: int, width of window in pixels
        - height: int, height of window in pixels
        """
        super().__init__()
        super().title(title)
        super().geometry(f"{width}x{height}")

        self.page = Layout(master=self,homepage=any, app_user=any)
        self.show_page()

    def show_page(self):
        """
        Displays the home page to make it visible in the main window.
        """
        self.page.place(relx=.5, rely=.5, anchor=tk.CENTER)

    def hide_page(self):
        """
        Hides the home page to make it invisible in the main window.
        """
        self.page.place_forget()



if __name__ == "__main__":
    # DO NOT MODIFY
    pass