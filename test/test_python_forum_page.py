"""
FIT1056 2024 Semester 2
EmpowerU Project
Team G08

Contains testing for the PyForumPage window
"""

from interfaces.gui_python_forum_page import PyForumPage
from interfaces.gui_homepage import HomePage
from classes.cls_app_user import AppUser
from classes.cls_post import Post


def test_load_posts():
    
    app_user = AppUser("r02", "Jerry","May","0410139244","jerry","j3rrymay")
    home_page = HomePage(None, app_user)
    py_forum_page = PyForumPage(None, home_page, app_user)
    forum_dir = "python_forum"

    assert Post(15, "How to deal with memory leaks in Python?","08/01/2024","20:30","Kevin Malone","I think I have a memory leak in my Python program. How can I find and fix it?", forum_dir) == py_forum_page.load_posts()[5]
    assert Post(1,"How do I make a for loop in python?","07/01/2024","20:10","Eric Hall", "I have been trying to figure out how to make one for the past 30 mins... Someone pls help!", forum_dir) == py_forum_page.load_posts()[6]
    assert Post(7, "Why is my Python script not working after upgrading to Python 3.12?","08/01/2024","15:00","Stanley Hudson", "After upgrading to the latest Python version some of my old scripts stopped working. How do I troubleshoot this?", forum_dir) == py_forum_page.load_posts()[12]
    assert not Post(-1, "What is the best approach to unit testing Python applications that make extensive use of third-party APIs and external services?","08/03/2024","16:15","Caitlin Snow", "I’m building a Python application that interacts heavily with third-party APIs and external services. Writing unit tests for this type of application has been challenging because of the dependency on external resources. I’ve read about mocking external services using libraries like unittest.mock or using third-party libraries like responses or VCR.py to simulate API responses. However I’m not sure which approach is best in terms of reliability ease of use and maintainability. Should I mock API responses or would it be better to use integration tests that actually interact with the live APIs? Additionally, I’m concerned about handling rate limits and ensuring the tests don’t fail due to temporary network issues. How do you strike the right balance between testing core application logic and ensuring external services work as expected? Would appreciate any detailed advice or examples of testing strategies in these scenarios!", forum_dir) == py_forum_page.load_posts()[8]
    assert not Post(8, "", "", "", "", "", forum_dir) == py_forum_page.load_posts()[13]
    assert not Post(16, "How to parse JSON data in Python?","08/01/2024","17:45","Andy Bernard", "I need to work with JSON data in my Python project. How can I parse and extract the relevant information?", forum_dir) == py_forum_page.load_posts()[14]