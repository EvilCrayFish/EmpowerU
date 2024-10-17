import tkinter as tk

class TestWindow(tk.Tk):
    def __init__(self, title):
        super().__init__()
        super().title(title)
        self.geometry("720x480")

        self.assignment_page = AssignmentsPage(self, "user123")
        self.show_assignments()


    def show_assignments(self):
        self.assignment_page.place(relx=.5, rely=.5, anchor=tk.CENTER)
    

    def hide_assignments(self):
        self.assignment_page.place_forget()



class AssignmentsPage(tk.Frame):
    def __init__(self, master, homepage, user):
        super().__init__(master=master)
        self.master = master
        self.homepage = homepage
        self.user = user

        self.return_button = tk.Button(self, text="Return to homepage", command=self.show_homepage)
        self.return_button.pack()

        self.title = tk.Label(self, text="Assignments", font=("Arial Bold", 20))
        self.title.pack()

        #The last index in self.courses must be the index which shows all assignments,
        #and the first index in self.courses must be the one which clears assignments
        #all other index can be changed
        self.courses = ["None", "Programming", "AI", "Information Security", "Show all assignments"]
        self.selected_course = tk.StringVar()
        self.selected_course.set(self.courses[0])

        self.course_dropdown = tk.OptionMenu(self, self.selected_course, *self.courses)
        self.course_dropdown.pack()

        self.select_course_button = tk.Button(self, text="Select course", command=self.update_assignment_list)
        self.select_course_button.pack()

        #Each of these index should map to the index in self.courses
        self.assignment_lists = ["No text to display", \
                                ["Programming Assignment 1", "Programming Assignment 2"], \
                                ["AI Assignment 1", "AI Assignment 2"], \
                                ["IT Assignment 1", "IT Assignment 2"]]
        
        self.assignments_on_screen = []

        self.assignment_list_str = tk.StringVar()
        self.update_assignment_list()

        self.assignment_list = tk.Label(self, textvariable=self.assignment_list_str)
        self.assignment_list.pack()


    def update_assignment_list(self):
        for assignment in self.assignments_on_screen:
            assignment.destroy()

        if self.selected_course.get() == self.courses[0]: #If no course is selected, show that no course is selected on screen, then exit the function
            assignment = tk.Label(self, text=self.assignment_lists[0])
            assignment.pack()
            self.assignments_on_screen.append(assignment)
            return
        
        if self.selected_course.get() == self.courses[-1]:
            assignments = []
            for i in self.assignment_lists[1:]:
                assignments = assignments + i
        else:
            index = self.courses.index(self.selected_course.get())
            assignments = self.assignment_lists[index]
        
        for assignment in assignments:
            #The next line is very, very buggy
            assignment_widget = tk.Button(self, text=assignment, fg="blue", cursor="hand2", command=lambda : self.redirect_to_assignment(assignment))
            assignment_widget.pack()
            self.assignments_on_screen.append(assignment_widget)


    def show_homepage(self):
        self.place_forget()
        self.homepage.show_menu()


    def redirect_to_assignment(self, assignment):
        assignment_page = AssignmentPage(self.master, self.user, self.selected_course.get(), assignment)
        assignment_page.place(relx=.5, rely=.5, anchor=tk.CENTER)
        self.master.hide_assignments()



class AssignmentPage(tk.Frame):
    def __init__(self, master, user, course, assignment):
        super().__init__(master=master)
        self.master = master
        self.user = user
        self.course = course
        self.assignment_name = assignment

        self.return_button = tk.Button(self, text="Return to assignments", command=self.return_to_assignments)
        self.return_button.pack()

        self.assignment_title = tk.Label(self, text=f"Assignment {self.assignment_name}", font=("Arial Bold", 20))
        self.assignment_title.pack()

        self.course_label = tk.Label(self, text=self.course)
        self.course_label.pack()

        self.assignment_status_label = tk.Label(self, text=f"Assignment status: Incomplete")
        self.assignment_status_label.pack()
        
        self.upload_button = tk.Button(self, text="Upload")


    def return_to_assignments(self):
        """
        Method to handle the return to assignments page upon button click.

        Parameter(s):
        (None)

        Return(s):
        (None)
        """
        self.place_forget()
        self.master.show_assignments()



if __name__ == "__main__":
    app = TestWindow("EmpowerU Assignments")
    app.mainloop()