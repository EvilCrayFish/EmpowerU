"""
FIT1056 2024 Semester 2
EmpowerU Project
Team G08

Contains testing for the EditLessonPage window
"""

import pytest
import sys
sys.path.append("../interfaces")

from interfaces.gui_edit_lesson_page import EditLessonPage
from interfaces.gui_homepage import HomePage
from classes.cls_app_user import AppUser

def test_get_lesson_line():
    
    app_user = AppUser("r02", "Jerry","May","0410139244","jerry","j3rrymay")
    home_page = HomePage(None, app_user)

    page1 = EditLessonPage(None, "AI", "Intro to AI", home_page, app_user)
    assert page1.get_lesson_line() == ["AI","Intro to AI","1. What is Artificial Intelligence?*Artificial Intelligence (AI) is a field of computer science that focuses on creating systems that can perform tasks that typically require human intelligence.**2. Applications of AI*AI is used in various industries, from healthcare to finance, to enhance decision-making and improve efficiency.**3. Summary*In this lesson, we introduced the basics of AI and its applications.","Complete"]

    page2 = EditLessonPage(None, "AI", "Machine Learning", home_page, app_user)
    assert page2.get_lesson_line() == ["AI","Machine Learning","1. What is Machine Learning?*Machine Learning (ML) is a subset of AI that focuses on building systems that learn from data.**2. Types of Machine Learning*There are three main types: supervised, unsupervised, and reinforcement learning.**3. Summary*In this lesson, we learned about machine learning and its various types.","Complete"]

    page3 = EditLessonPage(None, "AI", "Deep Learning", home_page, app_user)
    assert page3.get_lesson_line() == ["AI","Deep Learning","1. What is Deep Learning?*Deep Learning is a subset of ML that uses neural networks to model complex patterns in data.**2. Neural Networks*Neural networks are inspired by the human brain and consist of layers of interconnected nodes.**3. Summary*In this lesson, we explored the fundamentals of deep learning and neural networks.","Complete"]

    page4 = EditLessonPage(None, "AI", "Natural Language Processing", home_page, app_user)
    assert page4.get_lesson_line() == ["AI","Natural Language Processing","1. What is NLP?*Natural Language Processing (NLP) is a branch of AI that focuses on the interaction between computers and human language.**2. Applications of NLP*NLP is used in chatbots, translation services, and sentiment analysis.**3. Summary*In this lesson, we discussed the basics of NLP and its real-world applications.","Complete"]

    page5 = EditLessonPage(None, "PY", "Hello World!", home_page, app_user)
    assert page5.get_lesson_line() == ["PY","Hello World!","""1. Introduction to Python*Python is a popular, high-level programming language known for its simplicity and readability. It is widely used in various fields such as web development, data analysis, artificial intelligence, and automation.**Before diving into coding, let’s ensure you have Python installed on your computer. Visit the official Python website to download and install Python.**2. Writing Your First Python Program*The traditional first program in any programming language is called "Hello, World!"—this program prints the text "Hello, World!" to the screen.**Here’s what the code looks like in Python:**python*print("Hello, World!")*3. Summary*In this lesson, we learned how to write and run a basic Python program.""","Complete"]

    page6 = EditLessonPage(None, "PY", "Data Types and Variables", home_page, app_user)
    assert page6.get_lesson_line() == ["PY","Data Types and Variables","1. Understanding Data Types*Python has several built-in data types, including integers, floats, strings, and booleans.**2. Variables*Variables are used to store data. You can assign a value to a variable using the equals sign (=).**Example:**python*x = 5*3. Summary*In this lesson, we learned about Python's data types and how to create variables.","Complete"]

    page7 = EditLessonPage(None, "PY", "Control Flow", home_page, app_user)
    assert page7.get_lesson_line() == ["PY","Control Flow","1. Conditional Statements*Python uses if, elif, and else statements to control the flow of your program based on conditions.**2. Loops*Loops allow you to execute a block of code multiple times. The two main types are for loops and while loops.**3. Summary*In this lesson, we explored control flow using conditional statements and loops.","Complete"]

    page8 = EditLessonPage(None, "PY", "Functions and Modules", home_page, app_user)
    assert page8.get_lesson_line() == ["PY","Functions and Modules","""1. What is a Function?*A function is a block of reusable code that performs a specific task.**2. Defining a Function*You define a function using the def keyword.**Example:**python*def greet():*    print("Hello!")*3. Summary*In this lesson, we learned about functions, how to define them, and the importance of modules in organizing code.""","Complete"]

    page9 = EditLessonPage(None, "IS", "Intro to Information Systems", home_page, app_user)
    assert page9.get_lesson_line() == ["IS","Intro to Information Systems","1. What are Information Systems?*Information Systems (IS) are organized systems for collecting, storing, and processing data.**2. Components of IS*IS consists of hardware, software, data, procedures, and people.**3. Summary*In this lesson, we introduced the concept of information systems and their components.","Complete"]

    page10 = EditLessonPage(None, "IS", "Database Management Systems", home_page, app_user)
    assert page10.get_lesson_line() == ["IS","Database Management Systems","1. What is a Database?*A database is an organized collection of data that can be easily accessed and managed.**2. Types of Databases*Common types include relational, NoSQL, and distributed databases.**3. Summary*In this lesson, we learned about databases and their management systems.","Complete"]

    page11 = EditLessonPage(None, "IS", "Systems Development Life Cycle", home_page, app_user)
    assert page11.get_lesson_line() == ["IS","Systems Development Life Cycle","1. What is SDLC?*The Systems Development Life Cycle (SDLC) is a process for planning, creating, testing, and deploying information systems.**2. Phases of SDLC*The main phases include planning, analysis, design, implementation, and maintenance.**3. Summary*In this lesson, we explored the phases of the systems development life cycle.","Complete"]

    page12 = EditLessonPage(None, "IS", "IS Fundamentals", home_page, app_user)
    assert page12.get_lesson_line() == ["IS","IS Fundamentals","1. What is Information Security?*Information Security focuses on protecting information and information systems from unauthorized access, use, disclosure, disruption, modification, or destruction.**2. Key Concepts*Confidentiality, integrity, and availability are the three pillars of information security.**3. Summary*In this lesson, we discussed the basics of information security and its importance.","Complete"]

    page13 = EditLessonPage(None, "Info Sec", "IS Basics", home_page, app_user)
    assert not page13.get_lesson_line() == ["IS", "", "", ""]

    page14 = EditLessonPage(None, "Artificial intelligence", "AI Basics", home_page, app_user)
    assert not page14.get_lesson_line() == ["AI", "Large Language Models", "LLMs are cool", "Complete"]

    page15 = EditLessonPage(None, "Python", "Python Basics", home_page, app_user)
    assert not page15.get_lesson_line() == ["PY", "Python is good for beginners", "Hello World", "Incomplete"]

    page16 = EditLessonPage(None, "PY", "Functions and Modules", home_page, app_user)
    assert not page16.get_lesson_line() == ["PY","""Functions and Modules","1. What is a Function?*A function is a block of reusable code that performs a specific task.**2. Defining a Function*You define a function using the def keyword.**Example:**python*def greet():*    print("Hello!")*3. Summary*In this lesson, we learned about functions, how to define them, and the importance of modules in organizing code.""","Incomplete"]
    