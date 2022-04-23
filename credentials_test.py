import unittest
from credentials import Credentials
import pyperclip

class TestCredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the credentials class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = Credentials("GitHub","Miss-Faith","***") # create credentials object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.account,"GitHub")
        self.assertEqual(self.new_credentials.user_name,"Miss-Faith")
        self.assertEqual(self.new_credentials.password,"***")

    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credentials object is saved into the credentials list
        '''
        self.new_credentials.save_credentials() # saving the new credentials
        self.assertEqual(len(Credentials.credentials_list),1)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []

    def test_save_multiple_credentials(self):
        '''
        test_save_multiple_credentials to check if we can save multiple credentials objects to our credentials_list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Account","user","password") # new credential
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credentials(self):
        '''
        test_delete_credentials to test if we can remove a credentials from our credentials list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Account","user","password") # new credentials
        test_credentials.save_credentials()

        self.new_credentials.delete_credentials()# Deleting a credentials object
        self.assertEqual(len(Credentials.credentials_list),1) 

    def test_find_credentials_by_account(self):
        '''
        test to check if we can find a credentials by account and display information
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("Account","user","Password") # new credentials
        test_credentials.save_credentials()

        found_credentials = Credentials.find_by_account("Account")

        self.assertEqual(found_credentials.user_name,test_credentials.user_name)

    def test_credentials_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credentials.
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("Account","user","password") # new credentials
        test_credentials.save_credentials()

        credentials_exists = Credentials.credentials_exist("Account")

        self.assertTrue(credentials_exists)  

    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

    def test_copy_account(self):
        '''
        Test to confirm that we are copying the account name from a found credentials
        '''

        self.new_credentials.save_credentials()
        Credentials.copy_account("Account")

        self.assertEqual(self.new_credentials.account,pyperclip.paste())

if __name__ == '__main__':
    unittest.main()
