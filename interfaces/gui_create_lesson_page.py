import tkinter as tk
import os
from tkinter import messagebox

class CreateLessonPage(tk.Frame):
    def __init__(self, master, homepage, app_user):
        super().__init__(master)
        self.master = master
        self.homepage = homepage
        self.app_user = app_user

        self.return_button = tk.Button(self, text="Return to homepage", command=self.show_homepage)
        self.return_button.pack()

        self.page_title = tk.Label(self, text="Lesson Creation", font=("Arial Bold", 20))
        self.page_title.pack()

        self.categories = ["PY", "AI", "IS"]
        self.category_label = tk.Label(self, text="Lesson category: ")
        self.category_label.pack()
        self.category_var = tk.StringVar(self)
        self.category_var.set(self.categories[0])
        self.category_entry = tk.OptionMenu(self, self.category_var, *self.categories)
        self.category_entry.pack()

        self.title_label = tk.Label(self, text="Lesson title: ")
        self.title_label.pack()
        self.title_var = tk.StringVar(self)
        self.title_entry = tk.Entry(self, textvariable=self.title_var)
        self.title_entry.pack()

        self.content_label = tk.Label(self, text="Lesson content: ")
        self.content_label.pack()

        self.content_entry = tk.Text(self, height=10, width=50)
        self.content_entry.pack(pady=10)

        self.create_lesson_btn = tk.Button(self, text="Create lesson", command=lambda: self.create_lesson(False))
        self.create_lesson_btn.pack()
        self.add_attachments_btn = tk.Button(self, text="Create lesson and add attachments", command=lambda: self.create_lesson(True))
        self.add_attachments_btn.pack()

    def create_lesson(self, add_attachments):
        """
        Appends lesson to lessons.txt

        Parameters:
            add_attachments - whether the function will open the attachments folder for the lesson at the end
        """
        self.content_var = self.content_entry.get("1.0", tk.END).strip() #The new contents

        #Make sure user hasn't typed unsupported characters ; or *
        #If user has entered ; or * anywhere, end the function
        if ";" in (self.title_var.get() + self.content_var):
            messagebox.showerror("; detected", "You may not have the ; character in any field.")
            return
        elif "*" in (self.title_var.get() + self.content_var):
            messagebox.showerror("Asterisk detected", "You may not have the * character in any field.")
            return
        
        self.content_var = self.content_var.replace("\n", "*") #Formatting newlines to be represented by asterisks

        file_path = "data\\lessons.txt"

        #The line to write into lessons.txt
        lesson_info = f"{self.category_var.get()};{self.title_var.get()};{self.content_var};Incomplete\n"
        
        with open(file_path, "r") as filer: #Make sure lesson isn't already in lessons.txt
            all_lines = filer.readlines()
            for line in all_lines: 
                line_information = line.split(";")
                print(line)
                print(line_information[0], self.category_var.get())
                print(line_information[1], self.title_var.get())
                if line_information[0] == self.category_var.get() and line_information[1] == self.title_var.get():
                    messagebox.showerror("Lesson Already Exists", "Attempted to add lesson, but the lesson already exists.")
                    return 

        with open(file_path, "a") as filer: #Adds lesson to the text file
            filer.write(lesson_info)
            messagebox.showinfo("Lesson created", "Lesson has been successfuly added")
            
        if add_attachments: #Opens lesson attachments folder
            attachments_path = f"data\\LessonAttachments\\{self.category_var.get()}_{self.title_entry.get()}"
            try:
                os.mkdir(attachments_path)
            except FileExistsError:
                messagebox.showerror("FileExistsError", "Attempted to make lesson attachments folder, but the folder already exists. Opening the folder now.")
            finally:
                path = os.path.realpath(attachments_path)
                os.startfile(path)

        self.show_homepage()



    def show_homepage(self):
        self.place_forget()
        self.homepage.show_menu()