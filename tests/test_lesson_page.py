"Testing for the functionalities within the Progress tracker page for EmpowerU"

from interfaces.gui_edit_lesson_page import EditLessonPage

def test_get_lesson_line():
    
    page1 = EditLessonPage()
    assert page1.get_lesson_line() == []

    page2 = EditLessonPage()
    assert page2.get_lesson_line() == []

    page3 = EditLessonPage()
    assert page3.get_lesson_line() == []

    page4 = EditLessonPage()
    assert page4.get_lesson_line() == []

    page5 = EditLessonPage()
    assert page5.get_lesson_line() == []

    page6 = EditLessonPage()
    assert page6.get_lesson_line() == []

    page7 = EditLessonPage()
    assert page7.get_lesson_line() == []

    page8 = EditLessonPage()
    assert page8.get_lesson_line() == []