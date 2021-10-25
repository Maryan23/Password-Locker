from user import User
class Credentials:
    '''
    Class that creates instances of user credentials
    '''
    credentials_list = []
    def __init__(self,accountname,login_key):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
            accountname: Acount name 
            login key: Account password
        '''
        self.accountname = accountname
        self.login_key = login_key

    def newCredentials(self):
        print ('My credential details are '+ self.accountname + self.login_key)

new_credentials = Credentials('Facebook',' Angela22')
new_credentials.newCredentials()