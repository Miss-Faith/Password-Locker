import pyperclip
import random
import string
class Password:
    """
    Create Password class that generates a new length of a password.
    """
    password_list = []

    def __init__(self, passwordLength):
        """
        method that defines the properties of a user.
        """
        self.passwordLength = passwordLength

    def save_password(self):
        """
        A method that saves a new password instace into the password list
        """
        Password.user_password.append(self)

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

    @classmethod
    def copy_password(cls,account):
        credentials_found = Credentials.find_by_account(account)
        pyperclip.copy(credentials_found.password)

    def generatePassword(passwordLength):
        """
        Generate a random password string of uppercase and lowercase letters, digits and special characters
        """
        password = string.hexdigits + string.punctuation
        return ''.join(random.choice(password) for i in range(int(passwordLength)))

