class User:
    '''
    Class that creates new instances of users

    '''
    user_list = [] 

    def __init__(self,username,password):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
            Username: User's name
            Password: Account password
        '''
        self.username = username
        self.password = password

    def newUser(self):
        print ('My user details are '+ self.username + self.password)

new_user = User('Vodca ',' Angela22')
new_user.newUser()