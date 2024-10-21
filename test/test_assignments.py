"""
FIT1056 2024 Semester 2
EmpowerU Project
Team G08

Contains testing for the Assignments window
"""

from classes.cls_assignment import Assignment
from interfaces.gui_homepage import HomePage
from classes.cls_app_user import AppUser
from interfaces.gui_assignments import AssignmentsPage

def test_read_assignments():
    
    app_user = AppUser("r02", "Jerry","May","0410139244","jerry","j3rrymay")
    home_page = HomePage(None, app_user)
    assignments_page = AssignmentsPage(None, home_page, app_user)

    assert [Assignment("Information Security Assignment 1", "Information Security", "Incomplete"), Assignment("Python Assignment 1", "Programming", "Complete"), Assignment("Python Assignment 2", "Programming", "Incomplete"), Assignment("AI Assignment 2", "AI", "Complete"), Assignment("AI Assignment 1", "AI", "Complete")] == assignments_page.read_assignments(None, None)
    assert [Assignment("Information Security Assignment 1","Information Security","Incomplete")] == assignments_page.read_assignments("Information Security", None)
    assert [Assignment('Python Assignment 1','Programming','Complete'), Assignment("Python Assignment 2","Programming","Incomplete")] == assignments_page.read_assignments("Programming", None)
    assert [Assignment("AI Assignment 2","AI","Complete"), Assignment("AI Assignment 1","AI","Complete")] == assignments_page.read_assignments("AI", None)
    assert Assignment("Information Security Assignment 1","Information Security","Incomplete") == assignments_page.read_assignments(None, "Information Security Assignment 1")
    assert Assignment("Python Assignment 1","Programming","Complete") == assignments_page.read_assignments(None, "Python Assignment 1")
    assert [] == assignments_page.read_assignments("Large language models", None)
    assert [] == assignments_page.read_assignments("", "")
    assert not [] == assignments_page.read_assignments("Programming", None)
    assert not [Assignment('Python Assignment 1','Programming','Complete'), Assignment("","",""), ] == assignments_page.read_assignments("Programming", None)
    assert not Assignment("Information Security Assignment 1","Information Security","Complete") == assignments_page.read_assignments(None, "Information Security Assignment 1")
    assert not Assignment("Python Assignment 2","Programming","Incomplete") == assignments_page.read_assignments(None, "Python Assignment 1")



