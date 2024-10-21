"""
FIT1056 2024 Semester 2
EmpowerU Project
Team G08

This file contains the class definition for the Assignment class.
"""

class Assignment:
    def __init__(self, name, course, status):
        self.name = name
        self.course = course
        self.status = status

    def __eq__(self, other):
        if not isinstance(other, Assignment):
            return False
        
        if self.name != other.name:
            print(f"Name mismatch: {self.name} != {other.name}")
        if self.course != other.course:
            print(f"Course mismatch: {self.course} != {other.course}")
        if self.status != other.status:
            print(f"Status mismatch: {self.status} != {other.status}")
            
        return (
            self.name == other.name and 
            self.course == other.course and 
            self.status == other.status
            )