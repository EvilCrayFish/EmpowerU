from classes.cls_staff import Staff

class Teacher(Staff):
    def __init__(self, staff_id: int, name: str, email: str, phone: int, role: str, fname: str, lname: str):
        super.__init__(staff_id, name, email, phone, role) # Fix the parameters later
        self.name = name
        self.__email = email
        self._fname = fname
        self._lname = lname

    def get_name(self) -> str:
        """
        Returns the user's full name.
        """
        return f"{self._fname} {self._lname}"
    
    def update_password(self, new_password: str) -> bool:
        """
        Turns the new password into a salted hash and passes to the database. 

        Arguments:
        new_password - plaintext string of the new password to set the user's password to

        Returns:
        A boolean value of whether the new pasword is set or not
        """
        pass

    @staticmethod
    def login(self, username, password) -> Union[Teacher, None]:
        """
        Checks the input username and password against the username and password associated with the user. 

        Arguments:
        username - the username of the user attempting to log in
        password - the plaintext password of the user attempting to log in

        Returns:
        A Teacher if the login was successful, otherwise None
        """
        pass

    def make_post(self) -> Post:
        """
        This is very underdeveloped but the idea is it compiles the post and then returns it for another object to actually store it
        """
        pass

    def grade_task(self, lesson: Task, grade: int) -> None:
        """
        Changes lesson grade

        Arguments:
        task - the task graded
        grade - the % mark given
        """
        pass

    def create_lesson(self, change_this_to_actual_parameters) -> Lesson:
        """
        Takes change_this_to_actual_parameters and compiles them into a lesson

        Returns:
        The lesson made to be stored by a different object
        """
        pass

    def update_lesson(self, lesson: Lesson, change_this_to_actual_parameters) -> None:
        """
        Edits lesson information

        Arguments:
        lesson - the lesson being edited
        change_this_to_actual_parameters - the new information
        """
        pass

    def remove_lesson(self, lesson: Lesson) -> None:
        """
        Removes a lesson

        Arguments:
        lesson - the lesson being removed
        """
        pass