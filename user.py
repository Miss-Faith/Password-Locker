from credentials import Credentials

class User:
    """
    Create User class that generates new instances of a user.
    """
    
    def __init__(self, username, userpassword):
        """
        method that defines the properties of a user.
        """
        self.username = username
        self.password = userpassword