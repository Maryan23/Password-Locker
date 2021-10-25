import unittest #Imports unittest module
from user import User #Imports user class
from credentials import Credentials #Imports credentials class

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

    def test_create_user(self):
            '''
            test_create_contact to test if we can create a user
            '''

            self.new_user.create_user()# Creating a user object
            self.assertEqual(len(User.user_list),1)


if __name__ == '__main__':
    unittest.main()