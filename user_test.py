import unittest
from user import User

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Faith","*****") # create user object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username,"Faith")
        self.assertEqual(self.new_user.password,"*****")