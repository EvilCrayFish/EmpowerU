"Testing for the functionalities within the Progress tracker page for EmpowerU"

from interfaces.gui_edit_lesson_page import EditLessonPage
from interfaces.gui_homepage import HomePage
from classes.cls_app_user import AppUser

def test_get_lesson_line():
    
    app_user = AppUser("r02", "Jerry","May","0410139244","jerry","j3rrymay")
    home_page = HomePage(HomePage.master, app_user)

    page1 = EditLessonPage(EditLessonPage.master, "AI", "Introduction to Artificial Intelligence: What is AI?", home_page, app_user)
    assert page1.get_lesson_line() == []

    page2 = EditLessonPage(EditLessonPage.master, "AI", "Understanding Machine Learning: The Heart of AI", home_page, app_user)
    assert page2.get_lesson_line() == []

    page3 = EditLessonPage(EditLessonPage.master, "AI", "Neural Networks: The Building Blocks of AI", home_page, app_user)
    assert page3.get_lesson_line() == []

    page4 = EditLessonPage(EditLessonPage.master, "AI", "AI in Practice: Real-World Applications?", home_page, app_user)
    assert page4.get_lesson_line() == []

    page5 = EditLessonPage(EditLessonPage.master, "PY", "Introduction to Python and Basic Syntax", home_page, app_user)
    assert page5.get_lesson_line() == []

    page6 = EditLessonPage(EditLessonPage.master, "PY", "Understanding Variables and Data Types", home_page, app_user)
    assert page6.get_lesson_line() == []

    page7 = EditLessonPage(EditLessonPage.master, "PY", "Using Conditionals and If Statements", home_page, app_user)
    assert page7.get_lesson_line() == []

    page8 = EditLessonPage(EditLessonPage.master, "PY", "Mastering Loops: For and While", home_page, app_user)
    assert page8.get_lesson_line() == []

    page9 = EditLessonPage(EditLessonPage.master, "SE", "Introduction to Security: Why Security Matters", home_page, app_user)
    assert page9.get_lesson_line() == []

    page10 = EditLessonPage(EditLessonPage.master, "SE", "Understanding Cyber Threats: Types of Attacks", home_page, app_user)
    assert page10.get_lesson_line() == []

    page11 = EditLessonPage(EditLessonPage.master, "SE", "Encryption and Authentication: Protecting Data", home_page, app_user)
    assert page11.get_lesson_line() == []

    page12 = EditLessonPage(EditLessonPage.master, "SE", "Security Best Practices: Keeping Systems Safe", home_page, app_user)
    assert page12.get_lesson_line() == []