"""
FIT1056 2024 Semester 2
EmpowerU Project
Team G08

Contains testing for the Courses window
"""

from interfaces.gui_courses_page import CoursesPage
from interfaces.gui_homepage import HomePage
from classes.cls_app_user import AppUser

def test_read_lessons():

    app_user = AppUser("r02", "Jerry","May","0410139244","jerry","j3rrymay")
    home_page = HomePage(None, app_user)
    
    courses_page = CoursesPage(None, home_page, app_user)

    assert courses_page.read_lessons("AI") == ["Intro to AI", "Machine Learning", "Deep Learning", "Natural Language Processing"]

    assert courses_page.read_lessons("PY") == ["Hello World!", "Data Types and Variables", "Control Flow", "Functions and Modules"]

    assert courses_page.read_lessons("IS") == ["Intro to Information Systems", "Database Management Systems", "Systems Development Life Cycle", "IS Fundamentals"]

    assert courses_page.read_lessons("") == []

    assert not courses_page.read_lessons("AI") == ["Introduction to AI", "AI is great", "LLM", "Natural Language Processing"]

    assert not courses_page.read_lessons("PY") == ["I love programming", "helloworld", "", "Functions and Modules"]

    assert not courses_page.read_lessons("IS") == ["", "", "", ""]
