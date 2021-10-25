import unittest #Imports unittest module
from user import User #Imports user class

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
        self.new_user = User('Vodca ',' Angela22') # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username,"Vodca ")
        self.assertEqual(self.new_user.password," Angela22")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into the user list
        '''
        self.new_user.save_user() # saving the new contact
        self.assertEqual(len(User.user_list),1)

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []

    def test_save_multiple_users(self):
            '''
            test_save_multiple_users to check if we can save multiple user objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("Test","user") # new contact
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
            '''
            test_delete_user to test if we can create a user
            '''
            self.new_user.save_user()
            test_user = User("Roddy","User254") # new user
            test_user.save_user()

            self.new_user.delete_user()# Deleting a user object
            self.assertEqual(len(User.user_list),1)

    def test_find_user_by_name(self):
        '''
        test to check if we can find a user by username and display information
        '''

        self.new_user.save_user()
        test_user = User("Roddy","User254") # new contact
        test_user.save_user()

        found_user = User.find_by_name("Roddy")

        self.assertEqual(test_user.username,found_user.username)


if __name__ == '__main__':
    unittest.main()