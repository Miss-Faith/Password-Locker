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

    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self) 

    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)

    @classmethod
    def verify_user(cls,username):
        '''
        Method that takes in the user name and returns user user that matches that account.

        Args:
            User: User name to search for
        Returns :
            User of account that matches the account name.
        '''

        for user in cls.user_list:
            if user.username == username:
                return user
    
    