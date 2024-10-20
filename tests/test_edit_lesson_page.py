"Testing for the functionalities within the edit lesson page for EmpowerU"

from interfaces.gui_edit_lesson_page import EditLessonPage
from interfaces.gui_homepage import HomePage
from classes.cls_app_user import AppUser
# import tkinter as tk

def get_lesson_line():
    
    app_user = AppUser("r02", "Jerry","May","0410139244","jerry","j3rrymay")
    home_page = HomePage(HomePage.master, app_user)

    page1 = EditLessonPage(EditLessonPage.master, "AI", "Introduction to Artificial Intelligence: What is AI?", home_page, app_user)
    assert page1.get_lesson_line() == ["AI";"Introduction to Artificial Intelligence: What is AI?";"Welcome, students, to your first lesson on Artificial Intelligence! In this introductory lesson, we’ll explore what AI is and why it’s such an important field today. AI refers to the ability of machines to mimic human intelligence, such as learning, problem-solving, and decision-making. We’ll discuss the history of AI, key milestones, and how AI is used in our daily lives, from virtual assistants like Siri to self-driving cars. Understanding AI is the first step toward appreciating its potential and challenges.";"Complete"]

    page2 = EditLessonPage(EditLessonPage.master, "AI", "Understanding Machine Learning: The Heart of AI", home_page, app_user)
    assert page2.get_lesson_line() == ["AI";"Understanding Machine Learning: The Heart of AI";"In this lesson, we’ll dive into Machine Learning (ML), a key subset of AI that enables computers to learn from data. Machine learning involves algorithms that automatically improve through experience, which is why it’s so powerful. We’ll cover the basics of supervised learning, where models learn from labeled data, and unsupervised learning, where the goal is to find hidden patterns in data. This understanding is critical for grasping how modern AI systems like recommendation engines or facial recognition work.";"Incomplete"]

    page3 = EditLessonPage(EditLessonPage.master, "AI", "Neural Networks: The Building Blocks of AI", home_page, app_user)
    assert page3.get_lesson_line() == ["AI";"Neural Networks: The Building Blocks of AI";"In lesson 3, we’ll explore Neural Networks, the foundation of many advanced AI systems. Neural networks are inspired by the human brain and consist of interconnected nodes (neurons) that process information. We’ll break down how these networks learn through training, using data to adjust the strength of connections between neurons. You’ll also learn about different types of neural networks, such as feedforward and convolutional neural networks (used for image processing). Understanding neural networks is key to grasping AI’s capabilities in fields like computer vision and natural language processing.";"Incomplete"]

    page4 = EditLessonPage(EditLessonPage.master, "AI", "AI in Practice: Real-World Applications?", home_page, app_user)
    assert page4.get_lesson_line() == ["AI";"AI in Practice: Real-World Applications";"In this final lesson, we'll look at real-world applications of AI and how it’s transforming various industries. From healthcare, where AI helps diagnose diseases, to finance, where it detects fraudulent transactions, AI is everywhere. We’ll discuss autonomous systems like self-driving cars and robots, as well as how AI is being used in creative industries, like art and music. Understanding these applications will show you the practical impact of AI and inspire you to think about the future possibilities of this technology.";"Incomplete"]

    page5 = EditLessonPage(EditLessonPage.master, "PY", "Introduction to Python and Basic Syntax", home_page, app_user)
    assert page5.get_lesson_line() == ["PY";"Introduction to Python and Basic Syntax";"""Welcome, students, to your first Python lesson! In this introduction, you’ll learn the basics of Python syntax and how to write your very first Python program. Python is known for its readability and simplicity, making it beginner-friendly. We will start by using the print() function to display text on the screen. For instance, print("Hello, World!") outputs the classic beginner message. You’ll also learn about the importance of comments in Python, created with #, which allow you to add explanations within your code without affecting how the program runs.!""";"Complete"]

    page6 = EditLessonPage(EditLessonPage.master, "PY", "Understanding Variables and Data Types", home_page, app_user)
    assert page6.get_lesson_line() == ["PY";"Understanding Variables and Data Types";"In lesson 2, we’ll explore variables and data types in Python. A variable is like a container that holds data, and in Python, you don’t need to declare its type—Python infers it. For example, age = 25 creates a variable age with the integer value 25. We’ll cover basic data types like integers, floats (decimal numbers), and strings (text). This understanding will help you store and manipulate different types of information in your Python programs. Variables make your code dynamic and flexible.";"Complete"
]

    page7 = EditLessonPage(EditLessonPage.master, "PY", "Using Conditionals and If Statements", home_page, app_user)
    assert page7.get_lesson_line() == ["PY";"Using Conditionals and If Statements";"In this lesson, you’ll learn how to use conditionals to make decisions in your Python programs. The if statement allows your code to execute certain blocks of code only when specific conditions are met. For example, if score > 50: would check if a score is above 50 and take action if it is. You’ll also learn about elif (else if) and else statements, which provide alternative conditions and outcomes. These concepts will enable your programs to handle different situations and make them more interactive!";"Complete"
]

    page8 = EditLessonPage(EditLessonPage.master, "PY", "Mastering Loops: For and While", home_page, app_user)
    assert page8.get_lesson_line() == ["PY";"Mastering Loops: For and While";"Today’s lesson covers loops, an essential part of programming that lets you repeat tasks efficiently. You’ll learn about the for loop, which is great for iterating over a known range or a list of items. For instance, for item in shopping_list: will go through each item in the list. We’ll also look at the while loop, which continues to execute a block of code as long as a condition remains true. Loops are a powerful tool that help you write concise, efficient code when you need to perform repetitive tasks.;CompletePY;AI demo lesson;Hello, everyone!";"Incomplete"
]

    page9 = EditLessonPage(EditLessonPage.master, "SE", "Introduction to Security: Why Security Matters", home_page, app_user)
    assert page9.get_lesson_line() == ["SE";"Introduction to Security: Why Security Matters";"Welcome to your first lesson on Security! In this introduction, we will explore the importance of security in the digital age. Security refers to the practice of protecting systems, networks, and data from unauthorized access, damage, or theft. We’ll discuss key security principles like confidentiality, integrity, and availability, often referred to as the CIA Triad. This lesson will also cover why security is crucial in a world where cyberattacks are becoming more common, affecting both individuals and organizations. Understanding these basics will set the foundation for our future discussions.";"Complete"
]

    page10 = EditLessonPage(EditLessonPage.master, "SE", "Understanding Cyber Threats: Types of Attacks", home_page, app_user)
    assert page10.get_lesson_line() == ["SE";"Understanding Cyber Threats: Types of Attacks";"In this lesson, we'll dive into the different types of cyber threats and attacks that can compromise security. You'll learn about common attacks such as phishing, malware, ransomware, and Distributed Denial of Service (DDoS). We'll also cover social engineering, a method attackers use to manipulate individuals into divulging confidential information. Understanding these threats is essential for recognizing potential risks and safeguarding your systems. This lesson will help you become more aware of the dangers lurking in the digital world and how they can be mitigated.";"Complete"]

    page11 = EditLessonPage(EditLessonPage.master, "SE", "Encryption and Authentication: Protecting Data", home_page, app_user)
    assert page11.get_lesson_line() == ["SE";"Encryption and Authentication: Protecting Data";"In this lesson, we’ll explore two critical security measures: encryption and authentication. Encryption is the process of converting data into a secure format that can only be read by authorized parties. We’ll discuss how symmetric and asymmetric encryption work, along with real-world examples like HTTPS. Authentication, on the other hand, ensures that the person or system accessing data is who they claim to be, often using passwords, two-factor authentication, or biometric methods. These concepts are the backbone of securing sensitive information and preventing unauthorized access.";"Complete"
]

    page12 = EditLessonPage(EditLessonPage.master, "SE", "Security Best Practices: Keeping Systems Safe", home_page, app_user)
    assert page12.get_lesson_line() == ["SE";"Security Best Practices: Keeping Systems Safe";"In this final lesson, we’ll focus on practical security measures and best practices for keeping systems and data safe. You’ll learn about strategies like creating strong passwords, updating software regularly, and using firewalls and antivirus programs. We’ll also cover the importance of network security, including how to secure Wi-Fi networks and the role of Virtual Private Networks (VPNs). By following these best practices, you can reduce the risk of cyberattacks and ensure that your personal and professional information stays secure.";"Incomplete"
]