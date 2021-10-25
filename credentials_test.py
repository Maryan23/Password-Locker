import unittest #Imports unittest module
from credentials import Credentials #Imports credentials class

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
        self.new_credentials = Credentials('Facebook -',' Angela22') # create credentials object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.accountname,"Facebook -")
        self.assertEqual(self.new_credentials.login_key," Angela22")

    def test_save_credentials(self):
        '''
        test_save_credential test case to test if the crededential object is saved into the credential list
        '''
        self.new_credentials.save_credentials() # saving new credentials
        self.assertEqual(len(Credentials.credentials_list),1)

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.credentials_list = []

    def test_save_multiple_credentials(self):
            '''
            test_save_multiple_credentials to check if we can save multiple credential objects to our credentials_list
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("New","Key") # new credentials
            test_credentials.save_credentials()
            self.assertEqual(len(Credentials.credentials_list),2)

    def test_generate_loginkey(self):
        '''
        test_generate_loginkey
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("New","key") #new credentials
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list))

    def test_find_credentials_by_name(self):
        '''
        test to check if we can find Credentials by accountname and display information
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("Insta","User254") # new credentials
        test_credentials.save_credentials()

        found_credential= Credentials.find_by_name("Insta")

        self.assertEqual(test_credentials.accountname,found_credential.accountname)

    def test_delete_credentials(self):
            '''
            test_delete_credentials to test if we can delete credentials
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("LinkedIn","User254") # new credentials
            test_credentials.save_credentials()

            self.new_credentials.delete_credentials()# Deleting credentials
            self.assertEqual(len(Credentials.credentials_list),1)

    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)



if __name__ == '__main__':
    unittest.main()