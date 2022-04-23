import unittest
from credentials import Credentials

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

    # def tearDown(self):
    #     '''
    #     tearDown method that does clean up after each test case has run.
    #     '''
    #     Credential.credential_list = []

    def test_save_multiple_credentials(self):
        '''
        test_save_multiple_credentials to check if we can save multiple credentials objects to our credentials_list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Account","user","password") # new credential
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

if __name__ == '__main__':
    unittest.main()
