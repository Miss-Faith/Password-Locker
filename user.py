from credentials import Credentials

class User:
    """
    Create User class that generates new instances of a user.
    """
    user_list = []
    
    def __init__(self, username, userpassword):
        """
        method that defines the properties of a user.
        """
        self.username = username
        self.password = userpassword