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

    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)


    def delete_user(self):

        '''
        delete user method deletes user objects from users list
        '''

        User.user_list.remove(self)

    @classmethod
    def find_by_name(cls,name):
        '''
        Method that takes in a name and returns a user that matches that name.

        Args:
            name: User name to search for
        Returns :
            Name of person that matches the name.
        '''

        for user in cls.user_list:
            if user.username == name:
                return user

# new_user = User('Vodca ',' Angela22')
# new_user.newUser()