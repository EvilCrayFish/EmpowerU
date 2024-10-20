"""
FIT1056 2024 Semester 2
EmpowerU Project
Team G08

Contains testing for the ProgressTracker window
"""


from interfaces.gui_progress_tracker import ProgressTracker
from interfaces.gui_homepage import HomePage
from classes.cls_app_user import AppUser



def test_measure_lesson_progress():

    
    app_user = AppUser("r02", "Jerry","May","0410139244","jerry","j3rrymay")
    home_page = HomePage(HomePage.master, app_user)
    progress_tracker = ProgressTracker(ProgressTracker.master, app_user)

    assert progress_tracker.measure_lesson_progress("AI") == [4, 4, 100]

    assert progress_tracker.measure_lesson_progress("PY") == [4, 4, 100]

    assert progress_tracker.measure_lesson_progress("IS") == [4, 4, 100]

    assert progress_tracker.measure_lesson_progress("") == [0, 0, 0]
    