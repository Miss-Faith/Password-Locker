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
    def verify_user(cls,username, userpassword):
        """
        method to verify whether the user is in our user_list or not
        """
        a_user = ""
        for user in User.user_list:
            if(user.username == username and user.password == password):
                    a_user == user.username
        return a_user
    