import tkinter as tk
import os 
from classes.cls_assignment import Assignment
from classes.cls_mentor import Mentor
from classes.cls_staff import Staff


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
        
        self.assignments_on_screen = []

        self.assignment_list_str = tk.StringVar()
        self.update_assignment_list()

        self.assignment_list = tk.Label(self, textvariable=self.assignment_list_str)
        self.assignment_list.pack()


    def update_assignment_list(self):
        for assignment in self.assignments_on_screen:
            assignment.destroy()

        if self.selected_course.get() == self.courses[0]: #If no course is selected, show that no course is selected on screen, then exit the function
            assignment = tk.Label(self, text="No assignment to display")
            assignment.pack()
            self.assignments_on_screen.append(assignment)
            return
        
        if self.selected_course.get() == self.courses[-1]:
            assignments = self.read_assignments()
        else:
            index = self.courses.index(self.selected_course.get())
            assignments = self.read_assignments(searched_course=self.courses[index])
        
        for assignment in assignments:
            assignment_widget = tk.Button(self, text=assignment.name, fg="blue", cursor="hand2", command=lambda assignment=assignment : self.redirect_to_assignment(assignment))
            assignment_widget.pack()
            self.assignments_on_screen.append(assignment_widget)


    def show_homepage(self):
        self.place_forget()
        self.homepage.show_menu()

    
    def read_assignments(self, searched_course=None, searched_name=None) -> list:
        """
        Reads the assignments in a txt file,
        turns the assignments into Assignment objects,
        and then returns all objects as part of a list

        Parameters:
            searched_course = the course filter
                If none: search for all assignments
                If not none: only return assignments that are part of a particular course
            searched_name = the name filter
                If none: add assignment to list
                If not none: return assignment

        Returns:
            assignments = list of Assignment objects in assignments.txt which are part of searched_course 
        """
        assignments = []
        assignments_dir = f'./data/assignments.txt'

        with open(assignments_dir, "r") as assignments_txt:
            assignments_lines = assignments_txt.readlines()

            for line in assignments_lines:
                name, course, status = line.split(",")

                if name == searched_name:
                    return Assignment(name, course, status)
                elif course == searched_course or searched_course is None:
                    new_assignment = Assignment(name, course, status)
                    assignments.append(new_assignment)

        return assignments


    def redirect_to_assignment(self, assignment):
        assignment_page = AssignmentPage(self.master, self.user, assignment, self)
        assignment_page.place(relx=.5, rely=.5, anchor=tk.CENTER)
        self.place_forget()



class AssignmentPage(tk.Frame):
    def __init__(self, master, user, assignment, assignments_page):
        super().__init__(master=master)
        self.master = master
        self.user = user
        self.assignment = assignment
        self.assignments_page = assignments_page

        self.attachments_path = f"data\\AssignmentAttachments\\{self.assignment.name}"

        self.return_button = tk.Button(self, text="Return to assignments", command=self.return_to_assignments)
        self.return_button.pack()

        self.assignment_title = tk.Label(self, text=f"Assignment {self.assignment.name}", font=("Arial Bold", 20))
        self.assignment_title.pack()

        self.course_label = tk.Label(self, text=self.assignment.course)
        self.course_label.pack()

        self.assignment_status_label = tk.Label(self, text=f"Assignment status: {self.assignment.status}")
        self.assignment_status_label.pack()

        self.mark_complete_btn = tk.Button(self, text="Mark as complete", command=self.mark_complete)
        self.mark_complete_btn.pack()

        if type(self.user) in [Mentor, Staff]:
            self.delete_assignment_btn = tk.Button(self, text="Delete assignment", command=self.delete_assignment)
            self.delete_assignment_btn.pack()
        
        if os.path.exists(self.attachments_path):
            self.open_button = tk.Button(self, text="Open attachments", command=self.open_attachments)
            self.open_button.pack()

        if type(user) in [Mentor, Staff]:
            self.add_attachment = tk.Button(self, text="Add attachments", command=self.open_attachments)
            self.add_attachment.pack()


    def delete_assignment(self):
        other_lines = []
        with open("data\\assignments.txt", "r") as filer:
            for line in filer.readlines():
                line_information = line.strip().split(",")
                if (self.assignment.name == line_information[0] and self.assignment.course == line_information[1]) == False:
                    other_lines.append(line)
        
        with open("data\\assignments.txt", "w") as filer:
            for line in other_lines:
                filer.write(line)

        self.return_to_assignments()

    
    def mark_complete(self):
        other_lines = []
        with open("data\\assignments.txt", "r") as filer:
            for line in filer.readlines():
                line_information = line.strip().split(",")
                if (self.assignment.name == line_information[0] and self.assignment.course == line_information[1]) == False:
                    other_lines.append(line)
                else:
                    new_line = ",".join(line_information[:-1]) + ",Complete\n"
        
        with open("data\\assignments.txt", "w") as filer:
            for line in other_lines:
                filer.write(line)
            filer.write(new_line)

        self.return_to_assignments()


    def return_to_assignments(self):
        """
        Method to handle the return to assignments page upon button click.

        Parameter(s):
        (None)

        Return(s):
        (None)
        """
        self.assignments_page.place(relx=.5, rely=.5, anchor=tk.CENTER)
        self.place_forget()

    
    def open_attachments(self):
        if os.path.exists(self.attachments_path) == False:
            os.mkdir(self.attachments_path)
        path = os.path.realpath(self.attachments_path)
        os.startfile(path)