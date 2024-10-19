"Testing for the functionalities within the Login page for EmpowerU"

from classes.cls_app_user import AppUser
from classes.cls_mentor import Mentor

def test_authenticate():
    "Test cases for the authenticate() static method for both the AppUser and Mentor class"
    assert isinstance(Mentor.authenticate("rochelle", "r0che11e", path_to_root=".."), Mentor) == True
    assert isinstance(AppUser.authenticate("jerry", "j3rrymay", path_to_root=".."), AppUser) == True
    assert isinstance(AppUser.authenticate("max", "lynch", path_to_root=".."), AppUser) == False
    assert isinstance(Mentor.authenticate("rochelle", "password", path_to_root=".."), Mentor) == False
    assert isinstance(Mentor.authenticate("", "", path_to_root=".."), Mentor) == False 