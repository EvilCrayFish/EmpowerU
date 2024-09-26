"""
THIS IS THE ONLY FILE YOU SHOULD CHANGE

Change the init section to create the page.
"""

# Third party imports
import tkinter as tk


class Layout(tk.Frame):

    def __init__(self, master):
        """
        Constructor for the LoginPage class.

        Parameter(s):
        - master: master widget of this widget instance
        - image_path: str, path of the logo image file
        """
        super().__init__(master=master)
        self.master = master # Hint: a very useful instance variable

        # Logo image
        #TODO Change Layout of this

        # Welcome heading
        self.login_title = tk.Label(master=self, \
            text="Welcome to Music School Management System", \
            font=("Arial Bold", 20))
        self.login_title.grid(row=1, columnspan=2, padx=10, pady=10)

        # Username label widget
        self.username_label = tk.Label(master=self, text="Username:")
        self.username_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)

        # Username variable and entry widget
        self.username_var = tk.StringVar(master=self)
        self.username_entry = tk.Entry(master=self, textvariable=self.username_var)
        self.username_entry.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

        # Password label widget
        self.password_label = tk.Label(master=self, text="Password:")
        self.password_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.E)

        # Password variable and entry widget
        self.password_var = tk.StringVar(master=self)
        self.password_entry = tk.Entry(master=self, textvariable=self.password_var, show="●")
        self.password_entry.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)

        # Alert variable and label widget - displays alert messages where necessary
        self.alert_var = tk.StringVar(master=self)
        self.alert_label = tk.Label(master=self, textvariable=self.alert_var)
        self.alert_label.grid(row=4, columnspan=2, padx=10, pady=10)

        # Button to login
        self.login_button = tk.Button(master=self, text="Login")
        self.login_button.grid(row=5, columnspan=2, padx=10, pady=10)

        # Button to shut down
        self.shutdown_button = tk.Button(master=self, text="Shut down")
        self.shutdown_button.grid(row=6, columnspan=2, padx=10, pady=10)
		

if __name__ == "__main__":
    # DO NOT MODIFY
    pass