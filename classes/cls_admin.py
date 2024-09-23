"""
FIT1056 2024 Semester 2
EmpowerU Project

This file contains the class definition for the admin class.
"""


from classes.cls_staff import Staff

class Admin(Staff):

    def __init__(self, staffID, name, email, phone, role, adminLevel):
        """
        Constructor method for the Student class
        """
        super().__init__(staffID, name, email, phone, role)
        self.admin_level = adminLevel

    def assignRole():
        #TODO Write method
        pass
    def updateVersion():
        #TODO Write method
        pass
    def viewUsers():
        #TODO Write method
        pass

# DO NOT MODIFY BEYOND THIS LINE
if __name__ == "__main__":
    pass
