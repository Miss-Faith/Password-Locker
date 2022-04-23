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

    def save_credentials(self):

        '''
        save_credentials method saves credentials objects into credentials_list
        '''

        Credentials.credentials_list.append(self) 

    def delete_credentials(self):

        '''
        delete_credentials method deletes a saved credentials from the credentials_list
        '''

        Credentials.credentials_list.remove(self)