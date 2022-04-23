class Credentials:
    """
    Class that generates new instances of credentials
    """

    credentials_list = [] # Empty credentials list

    def __init__(self,account,user_name,password):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
            account: New credentials account.
            user_name: New credentials user name.
            password : New credentials password.
        '''
        self.account = account
        self.user_name = user_name
        self.password = password    