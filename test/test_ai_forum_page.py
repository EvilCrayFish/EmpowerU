"""
FIT1056 2024 Semester 2
EmpowerU Project
Team G08

Contains testing for the Aiforumpage window
"""

from interfaces.gui_ai_forum_page import AiForumPage
from interfaces.gui_homepage import HomePage
from classes.cls_app_user import AppUser
from classes.cls_post import Post


def test_load_posts():
    
    app_user = AppUser("r02", "Jerry","May","0410139244","jerry","j3rrymay")
    home_page = HomePage(None, app_user)
    ai_forum_page = AiForumPage(None, home_page, app_user)
    forum_dir = "ai_forum"

    assert Post(10, "What exactly is unsupervised learning used for?","08/05/2024","15:00","Aaron Green", "I know unsupervised learning deals with unlabeled data but what real-world applications does it have?", forum_dir) == ai_forum_page.load_posts()[0]
    assert Post(1, "What exactly is a Neural Network?","07/01/2024","20:30","Melissa Perera", "Guys I still don't get it... Can someone explain?", forum_dir) == ai_forum_page.load_posts()[1]
    assert Post(3, "What’s the difference between supervised and unsupervised learning?","08/05/2024","10:30","Jessica Zhang","Can someone clarify the key differences between these two types of learning? I keep mixing them up.", forum_dir) == ai_forum_page.load_posts()[3]
    assert not Post(-1, "How does a convolutional neural network (CNN) work?","08/05/2024","13:10","Nina Davis","I’m trying to learn about CNNs, but I’m confused about how they process images. Can someone explain?", forum_dir) == ai_forum_page.load_posts()[7]
    assert not Post(6, "", "", "", "", "", forum_dir) == ai_forum_page.load_posts()[6]
    assert not Post(11, "What is overfitting in machine learning?","08/05/2024","13:45","David Lee","I’ve seen warnings about overfitting models, but how can I recognize when this happens?", forum_dir) == ai_forum_page.load_posts()[9]