import unittest
from user import User

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

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

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)  

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_save_multiple_users(self):
        '''
        test_save_multiple_users to check if we can save multiple users objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("UserName","UserPassword") # new user
        test_user.save_user()
        self.assertEqual(len(User.user_list),2) 
    
    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user_list
        '''
        self.new_user.save_user()
        test_user = User("UserName","UserPassword") # new user
        test_user.save_user()

        self.new_user.delete_user()# Deleting a user object
        self.assertEqual(len(User.user_list),1) 

    def test_verify_user(self):
        '''
        test to check if we can find a user by account and display information
        '''

        self.new_user.save_user()
        test_user = User("UserName","UserPassword") # new user
        test_user.save_user()

        found_user = User.verify_user("UserName")

        self.assertEqual(found_user.username,test_user.username)


if __name__ == '__main__':
    unittest.main() 