"""
FIT1056 2024 Semester 2
EmpowerU Project
Team G08

Contains testing for the SecurityForumPage window
"""

from interfaces.gui_security_forum_page import SecurityForumPage
from interfaces.gui_homepage import HomePage
from classes.cls_app_user import AppUser
from classes.cls_post import Post


def test_load_posts():
    
    app_user = AppUser("r02", "Jerry","May","0410139244","jerry","j3rrymay")
    home_page = HomePage(None, app_user)
    security_forum_page = SecurityForumPage(None, home_page, app_user)
    forum_dir = "security_forum"

    assert Post(10, "How does EmpowerU handle data backup and recovery in case of a security incident?", "10/10/2024", "13:30", "James Martin", "In case of a breach or data loss how does EmpowerU ensure that data is backed up and can be recovered?", forum_dir) == security_forum_page.load_posts()[0]
    assert Post(1, "How does multi-factor authentication (MFA) improve security on the EmpowerU platform?", "10/10/2024", "09:00", "Sarah Evans", "I’m wondering if adding MFA to our EmpowerU accounts is worth it. Can someone explain how it actually enhances security?", forum_dir) == security_forum_page.load_posts()[1]
    assert Post(3, "How does EmpowerU handle data encryption?", "10/10/2024", "10:00", "Emily Turner", "I’m curious about how EmpowerU protects sensitive data. Is the data encrypted at rest and in transit?", forum_dir) == security_forum_page.load_posts()[3]
    assert not Post(-1, "How does EmpowerU handle data backup and recovery in case of a security incident?", "10/10/2024", "13:30", "James Martin", "In case of a breach or data loss how does EmpowerU ensure that data is backed up and can be recovered?", forum_dir) == security_forum_page.load_posts()[0]
    assert not Post(6, "", "", "", "", "", forum_dir) == security_forum_page.load_posts()[6]
    assert not Post(11, "How often should I update my EmpowerU password to maintain security?", "10/10/2024", "12:30", "Mark Lewis", "I’ve been told to regularly change my passwords on different platforms. How often should I change my EmpowerU password to keep it secure?", forum_dir) == security_forum_page.load_posts()[9]