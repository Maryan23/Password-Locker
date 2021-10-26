import random, string, pyperclip
from user import User
from credentials import Credentials

def create_user(username,password):
    '''
    Function to create a new user
    '''
    new_user = User(username,password)
    return new_user

def create_credentials(accountname,loginkey):
    '''
    Function to create new credentials
    '''
    new_credentials = Credentials(accountname,loginkey)
    return new_credentials

def generate_loginkey():
    '''
    Function that generates a loginkey
    '''
    phrase = phrase = string.digits + string.ascii_lowercase + string.ascii_uppercase
    while True:
        try:
            length = int(input('Enter length of loginkey!'))
            loginkey = random.sample(phrase, length)

        except ValueError:
            print("Please enter a valid number!")
            continue
        else:
            loginkey = ("".join(loginkey))
            return loginkey

def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()

def del_credentials(credentials):
    '''
    Function to delete credentials
    '''
    credentials.delete_credentials()

def find_credentials(aname):
    '''
    Function that finds credentials by accountname and returns the credential
    '''
    return Credentials.find_by_name(aname)

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()

def main():
    print('Hello! Welcome to Password Locker.')
    print('What would you like to do? Find ways to navigate around below.')
    print('\n')

    while True:
        print("lg => to Login to your account")
        print("sg => to Sign-up and create an account.")
        short_code = input().lower()
        print('\n')
        if short_code == 'sg':
                            print("Enter UserName")
                            username = input()

                            print ("Enter Password")
                            password = input()
                            
                            print ("Confirm Password")
                            confirm_password = input()

                            while confirm_password != password:
                                print("Passwords did not match! Kindly try again")
                                print("Enter Password")
                                password = input()
                                print("Confirm Password")
                                confirm_password = input()
                            else :
                                print(f"Congratulations {username}! Your account was created successfully!")
                                print('\n')
                                print("Please proceed to login")
                                print("Enter Username")
                                entered_username = input()
                                print("Enter Password")
                                entered_password = input()
                            
                            while entered_username != username or entered_password != password:
                                print("Invalid username or password")

                                print("Enter your Username")
                                entered_username = input()
                                print("Enter your Password")
                                entered_password = input()

                            else:
                                print(f"Welcome to your account {username}")
                                while True:
                                    print("Please choose an option to continue")
                                    print("cc => to create new credentials")
                                    print("dc => to display credentials")
                                    print("cp => to copy credential details to clipboard")
                                    print("du => to delete account credentials")
                                    print("ex => to exit the application")
                                    short_code = input().lower()
                                    if short_code == 'cc':
                                        print("Enter Account Name")
                                        a_name = input()

                                        while True:
                                            print("Use the shortcodes to choose login key option")
                                            print("el => to enter login key")
                                            print("gl => for a system generated key")
                                            print("ex => to exit the prompt")
                                            l_key = input().lower()
                                            print("\n")
                                            if l_key == 'el':
                                                print("Enter login key")
                                                log_key = input()
                                            elif l_key == 'gl':
                                                log_key = generate_loginkey()
                                                break
                                            elif l_key == 'ex':
                                                break
                                            else:
                                                print("Please check your input!")

                                        save_credentials(create_credentials(a_name,log_key)) #creates and saves new credentials
                                        print(f"Credentials for {a_name} have been created and its login key is {log_key}")

                                    elif short_code == 'dc':
                                        if display_credentials():
                                            print("Find a list of your credentials below")
                                            print("\n")
                                            for credentials in display_credentials():
                                                print(f"{credentials.accountname} - {credentials.login_key}")
                                        else:
                                            print("You dont have any saved credentials yet!")

                                    elif short_code == 'cp':
                                        print("Enter account name whose credentials you want to copy!")
                                        accountname = input()
                                        account = find_credentials(accountname)
                                        pyperclip.copy(account.accountname)

                                    elif short_code == 'du':
                                        print("Enter account name you wish to delete")
                                        accountname = input()
                                        account = find_credentials(accountname)
                                        del_credentials(account)

                                    elif short_code == 'ex':
                                        print("Are you sure you want to leave?")
                                        print("Y/N?")
                                        answer = input().upper()
                                        if answer == 'Y':
                                            print("It is sad to see you leave :(!")
                                            break
                                        elif answer == 'N':
                                            print("Please choose an option to continue:'cc' to create new credentials,'du' to delete account credentials,'dc' to display credentials,'cp' to copy credential details to clipboard, 'ex' to exit the application")
                                            short_code = input().lower()
                                        else:
                                            print("Choose a valid option!")

                                    
        elif short_code == 'lg':
            print("Enter Username")
            default_username = input()
            print("Enter Password")
            default_password = input()

            while default_username != 'Vodca' or default_password != 'Angela22':
                print("Wrong username or password")
                
            else:
                print("Login success!:)")
                while True:
                    print("Please choose an option to continue")
                    print("cc => to create new credentials")
                    print("dc => to display credentials")
                    print("cp => to copy credential details to clipboard")
                    print("du => to delete account credentials")
                    print("ex => to exit the application")
                    short_code = input().lower()
                    if short_code == 'cc':
                        print("Enter Account Name")
                        a_name = input()

                        while True:
                            print("Use the shortcodes to choose login key option")
                            print("el => to enter login key")
                            print("gl => for a system generated key")
                            print("ex => to exit the prompt")
                            l_key = input().lower()
                            print("\n")
                            if l_key == 'el':
                               print("Enter login key")
                               log_key = input()
                            elif l_key == 'gl':
                                 log_key = generate_loginkey()
                                 break
                            elif l_key == 'ex':
                                 break
                            else:
                                print("Please check your input!")
                        save_credentials(create_credentials(a_name,log_key)) #creates and saves new credentials

                        print(f"Credentials for {a_name} have been created and its login key is {log_key}")

                    elif short_code == 'dc':

                        if display_credentials():
                            print("Find a list of your credentials below")
                            print("\n")
                            for credentials in display_credentials():
                                print(f"{credentials.accountname} - {credentials.login_key}")
                        else:
                            print("You dont have any saved credentials yet!")

                    elif short_code == 'cp':
                            print("Enter account name whose credentials you want to copy!")
                            accountname = input()
                            account = find_credentials(accountname)
                            pyperclip.copy(account.accountname)

                    elif short_code == 'du':
                            print("Enter account name you wish to delete")
                            accountname = input()
                            account = find_credentials(accountname)
                            del_credentials(account)

                    elif short_code == 'ex':
                            print("Are you sure you want to leave?")
                            print("Y/N?")
                            answer = input().upper()
                            if answer == 'Y':
                                print("It is sad to see you leave :(!")
                                break
                            elif answer == 'N':
                                print("Please choose an option to continue:'cc' to create new credentials,'du' to delete a user credentials,'dc' to display credentials, 'ex' to exit the application")
                                short_code = input().lower()
                            else:
                                print("Choose a valid option!")

        else:
            print("Enter valid short code to continue!")

if __name__ == "__main__":
    main()
