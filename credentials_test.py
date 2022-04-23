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


if __name__ == '__main__':
    unittest.main()