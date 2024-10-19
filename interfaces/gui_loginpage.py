import tkinter as tk
from tkinter import messagebox  # For user-friendly alerts

# Local application imports
#TODO Define new page classes and change these imports
from classes.cls_app_user import AppUser
from classes.cls_mentor import Mentor

from interfaces.gui_homepage import HomePage

class LoginPage(tk.Frame):
    def __init__(self, master, image_path):
        """
        Constructor for the LoginPage class.

        Parameters:
        - master: master widget of this widget instance
        - image_path: str, path of the logo image file
        """
        super().__init__(master=master)
        self.master = master
        self.image_path = image_path

        # Configure the grid layout to center content
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # Logo Image
        self.logo_photoimage = tk.PhotoImage(master=self, file=self.image_path)
        self.logo_label = tk.Label(self, image=self.logo_photoimage)
        self.logo_label.grid(row=0, column=0, columnspan=2, pady=(10, 20))

        # Welcome Message
        self.login_title = tk.Label(self, text="Welcome to EmpowerU", font=("Arial Bold", 24), pady=10)
        self.login_title.grid(row=1, column=0, columnspan=2)

        # Username Entry
        self.username_var = tk.StringVar()
        self.username_entry = self.username_placeholder(self, self.username_var, "Enter your username")
        self.username_entry.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Password Entry with Placeholder
        self.password_var = tk.StringVar()
        self.password_entry = self.password_placeholder(
            self, self.password_var, "Enter your password")
        self.password_entry.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Login and Shutdown Buttons with Hover Effect
        self.login_button = self.create_styled_button(self, text="Login", command=self.login)
        self.login_button.grid(row=4, column=0, columnspan=2, pady=(20, 10))

        self.shutdown_button = self.create_styled_button(self, text="Shut down", command=self.master.destroy)
        self.shutdown_button.grid(row=5, column=0, columnspan=2, pady=5)

        # Alert Label
        self.alert_var = tk.StringVar()
        self.alert_label = tk.Label(self, textvariable=self.alert_var, fg="red", pady=5)
        self.alert_label.grid(row=6, column=0, columnspan=2)

    def username_placeholder(self, parent: tk.Frame, var: tk.StringVar, placeholder: str, show=None):
        """
        Generates the username entry box

        Parameters:
            parent - the LoginPage frame the box will sit in
            var - the text which occupies the text box once user enters text
            placeholder - the text which occupies the box before being edited (text cleared on interaction)
        
        Returns:
            entry - a tk.Entry widget which is added to the screen and serves as the username entry
        """
        entry = tk.Entry(parent, textvariable=var, show=show, fg="grey", font=("Arial", 14), width=25)

        def on_focus_in(event): #clear the default text when user clicks the box
            if var.get() == placeholder:
                var.set("")

        def on_focus_out(event): #add the default text when user clicks off an empty box
            if not var.get():
                var.set(placeholder)

        var.set(placeholder) #Set text to default
        entry.bind("<FocusIn>", on_focus_in) #check for on_focus_in - user clicks on box
        entry.bind("<FocusOut>", on_focus_out) #check for on_focus_out - user clicks off box
        return entry
    
    def password_placeholder(self, parent, var, placeholder):
        """
        Generates the password entry box

        Parameters:
            parent - the LoginPage frame the box will sit in
            var - the text which occupies the text box once user enters text
            placeholder - the text which occupies the box before being edited (text cleared on interaction)
        
        Returns:
            entry - a tk.Entry widget which is added to the screen and serves as the password entry
        """
        entry = tk.Entry(parent, textvariable=var, fg="grey", font=("Arial", 14), width=25)

        def on_focus_in(event):
            if var.get() == placeholder:
                entry.config(show="●")  # Show password when focused
                var.set("")

        def on_focus_out(event):
            if not var.get():
                entry.config(show="")  # Remove masking for the placeholder
                var.set(placeholder)

        var.set(placeholder) #Set text to default
        entry.bind("<FocusIn>", on_focus_in) #check for on_focus_in - user clicks on box
        entry.bind("<FocusOut>", on_focus_out) #check for on_focus_out - user clicks off box
        return entry

    def create_styled_button(self, parent, text, command):
        """
        Create a button with consistent styling and hover effect.

        Parameters:
        - parent: The parent widget for the button.
        - text: The text on the button.
        - command: The function to call on click.

        Returns:
        - Styled Button widget.
        """
        button = tk.Button(parent, text=text, font=("Arial", 14), width=15, command=command)

        def on_enter(event): #Style on hover
            button.config(relief="raised", background="#d1e0e0")

        def on_leave(event): #Style  not on hover
            button.config(relief="flat", background="SystemButtonFace")

        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
        return button

    def login(self):
        """
        Handle login button click. Authenticate user and show alerts if necessary.
        """
        username = self.username_var.get()
        password = self.password_var.get()

        app_user = AppUser.authenticate(username, password)
        mentor = Mentor.authenticate(username, password)

        if isinstance(app_user, AppUser): #Was student login successful?
            user = app_user
            self.master.hide_loginpage()
            home_page = HomePage(self.master, user)
            home_page.show_menu()
            self.alert_var.set("")
        elif isinstance(mentor, Mentor): #Was teacher login successful?
            user = mentor
            self.master.hide_loginpage()
            home_page = HomePage(self.master, user)
            home_page.show_menu()
            self.alert_var.set("")
        else: #Username/password incorrect
            self.alert_var.set("Login Unsuccessful.")
            messagebox.showerror("Login Error", "Invalid username or password. Please try again.")

        # Clear the input fields
        self.username_var.set("")
        self.password_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Login Page")
    root.geometry("400x500")  # Window size
    LoginPage(root, "logo.png").grid(sticky="nsew")  # Adjust with your logo path
    root.mainloop()



