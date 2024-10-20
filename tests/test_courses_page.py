"Testing for the functionalities within the Progress tracker page for EmpowerU"

from interfaces.gui_courses_page import CoursesPage

def test_read_lessons():
    
    courses_page = CoursesPage(root, )

    assert CoursesPage.read_lessons("AI") == []
    assert CoursesPage.read_lessons("AI") == []
    assert CoursesPage.read_lessons("AI") == []
    assert CoursesPage.read_lessons("PY") == []
    assert CoursesPage.read_lessons("PY") == []
    assert CoursesPage.read_lessons("PY") == []
    assert CoursesPage.read_lessons("SE") == []
    assert CoursesPage.read_lessons("SE") == []
    assert CoursesPage.read_lessons("SE") == []