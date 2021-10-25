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

    def save_credentials(self):

        '''
        save_credentials method saves credential objects into credential_list
        '''

        Credentials.credentials_list.append(self)


    @classmethod
    def find_by_name(cls,name):
        '''
        Method that takes in an accountname and returns credentials that matches that name.

        Args:
            name: Account name to search for
        Returns :
            Name of account that matches credentials.
        '''

        for credentials in cls.credentials_list:
            if credentials.accountname == name:
                return credentials

    def delete_credentials(self):

        '''
        delete user method deletes user objects from users list
        '''

        Credentials.credentials_list.remove(self)

new_credentials = Credentials('Facebook -',' Angela22')
new_credentials.newCredentials()