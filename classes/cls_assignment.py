"""
FIT1056 2024 Semester 2
EmpowerU Project
Team G08

This file contains the class definition for the Assignment class.
"""

class Assignment:
    def __init__(self, name, course, status):
        """
        Constructor method for the Assignment class.
        
        Parameters:
        - name: string - name of the assignment. 
        - course: string - name of the course
        - status: string - The status of the the course (either Complete or Incomplete)
        """
        self.name = name
        self.course = course
        self.status = status

    def __eq__(self, other):
        if not isinstance(other, Assignment):
            return False
        
        if self.name != other.name:
            print(f"Name mismatch: {self.name.strip()} != {other.name.strip()}")
        if self.course != other.course:
            print(f"Course mismatch: {self.course.strip()} != {other.course.strip()}")
        if self.status != other.status:
            print(f"Status mismatch: {self.status.strip()} != {other.status.strip()}")
            
        return (
            self.name.strip() == other.name.strip() and 
            self.course.strip() == other.course.strip() and 
            self.status.strip() == other.status.strip()
            )