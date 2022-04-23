import pyperclip

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
    
    @classmethod
    def find_by_account(cls,account):
        '''
        Method that takes in account name and returns credentials that matches that account.

        Args:
            number: Account name to search for
        Returns :
            Credentials of account that matches the account name.
        '''

        for credentials in cls.credentials_list:
            if credentials.account == account:
                return credentials
    
    @classmethod
    def credentials_exist(cls,account):
        '''
        Method that checks if a credentials exists from the credentials list.
        Args:
            account: Account name to search if it exists
        Returns :
            Boolean: True or false depending if the credentials exists
        '''
        for credentials in cls.credentials_list:
            if credentials.account == account:
                    return True

        return False

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list
