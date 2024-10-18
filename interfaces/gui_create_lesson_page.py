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

        self.page_title = tk.Label(self, text="Assignments", font=("Arial Bold", 20))
        self.page_title.pack()

        self.categories = ["Programming", "AI", "Information Security"]
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
        self.content_var = tk.StringVar(self)
        self.content_entry = tk.Entry(self, textvariable=self.content_var)
        self.content_entry.pack()

        self.create_lesson_btn = tk.Button(self, text="Create lesson", command=lambda: self.create_lesson(False))
        self.create_lesson_btn.pack()
        self.add_attachments_btn = tk.Button(self, text="Create lesson and add attachments", command=lambda: self.create_lesson(True))
        self.add_attachments_btn.pack()

    def create_lesson(self, add_attachments):
        #Make sure user hasn't typed unsupported character ; 
        #If user has entered ; anywhere, end the function
        if ";" in (self.title_var.get() + self.content_var.get()):
            messagebox.showerror("; detected", "You may not have the ; character in any field.")
            return

        file_path = "data\\lessons.txt"

        #The line to write into lessons.txt
        lesson_info = f"{self.category_var.get()};{self.title_var.get()};{self.content_var.get()};Incomplete\n"

        with open(file_path, "a+") as filer:
            #TODO: fix the if condition so that it only checks for title and category, not the whole line
            if lesson_info not in filer.readlines():
                filer.write(lesson_info)
                messagebox.showinfo("Lesson created", "Lesson has been successfuly added")
            else:
                messagebox.showerror("Lesson Already Exists", "Attempted to add lesson, but the lesson already exists.")
        
        if add_attachments:
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