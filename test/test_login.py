"""
FIT1056 2024 Semester 2
EmpowerU Project
Team G08

Contains testing for the LoginPage window
"""


from classes.cls_app_user import AppUser
from classes.cls_mentor import Mentor

def test_authenticate():
    "Test cases for the authenticate() static method for both the AppUser and Mentor class"
    assert isinstance(Mentor.authenticate("rochelle", "r0che11e"), Mentor) == True
    assert isinstance(AppUser.authenticate("jerry", "j3rrymay"), AppUser) == True
    assert isinstance(AppUser.authenticate("max", "lynch"), AppUser) == False
    assert isinstance(Mentor.authenticate("rochelle", "password"), Mentor) == False
    assert isinstance(Mentor.authenticate("", ""), Mentor) == False 
    assert isinstance(AppUser.authenticate("jerry", ""), AppUser) == False 
    assert isinstance(AppUser.authenticate("", "j3rrymay"), AppUser) == False
    assert isinstance(Mentor.authenticate("rochelle", ""), Mentor) == False
    assert isinstance(Mentor.authenticate("", "r0che11e"), Mentor) == False