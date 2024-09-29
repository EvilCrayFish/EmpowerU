class Student():
    def __init__(self, student_id: int, username: str, password: str, email: str, fname: str, lname: str):
        self.student_id = student_id
        self.username = username
        self.__email = email
        self._fname = fname
        self._lname = lname
        self.progress = ProgressTracker() # Fix the parameters later

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
    def login(self, username, password) -> Student:
        """
        Checks the input username and password against the username and password associated with the user. 

        Arguments:
        username - the username of the user attempting to log in
        password - the plaintext password of the user attempting to log in

        Returns:
        A boolean of whether the login was successful or not
        """
        pass

    def update_lesson_progress(self, course, progress) -> None:
        """
        Updates lesson progress, idk how yet

        Arguments:
        course - the area where progress was made
        progress - the amount of progress made
        """
        pass

    def get_lesson_progress(self, course) -> int:
        """
        Checks the amount of progress made in a course and returns the % amount

        Arguments: 
        course - which course is being reported on

        Returns:
        An integer of the amount of progress the user has made in that course
        """
        pass

    def make_post(self) -> Post:
        """
        This is very underdeveloped but the idea is it compiles the post and then returns it for another object to actually store it
        """
        pass