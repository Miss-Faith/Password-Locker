#!/usr/bin/env python3.8

from credentials import Credentials
from user import User

def create_user(username,userpassword):
    '''
    Function to create a new credential
    '''
    new_user = User(username,userpassword)
    return new_user

def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def display_user():
    """
    Function to display existing user
    """
    return User.display_user()

def login_user(username,password):
    """
    function that checks whether a user exist and then login the user in.
    """
    check_user = Credentials.verify_user(username,password)
    return check_user

def create_credentials(account,user,password):
    '''
    Function to create a new credential
    '''
    new_credentials = Credentials(account,user,password)
    return new_credentials

def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()

def del_credentials(credentials):
    '''
    Function to delete a credential
    '''
    credentials.delete_credentials()

def find_credentials(account):
    '''
    Function that finds a credentials by account and returns the credentials
    '''
    return Credentials.find_by_account(account)

def check_existing_credentials(account):
    '''
    Function that check if a credential exists with that account and return a Boolean
    '''
    return Credentials.credentials_exist(account)

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()

def generate_Password():
    '''
    generates a random password for the user.
    '''
    auto_password=Credentials.generatePassword()
    return auto_password

def main():
    print("Hello Welcome to your Password Store...\n Please enter one of the following to proceed.\n CA ---  Create New Account  \n SI ---  Sign in to existing Account  \n")
    short_code=input("").lower().strip()

    if short_code == "ca":
        print("Create Account ...")
        print('*' * 40)
        username = input("User_name: ")
        while True:
            print(" TP - To type your own pasword:\n GP - To generate random Password")
            password_Choice = input().lower().strip()

            if password_Choice == 'tp':
                password = input("Enter Password\n")
                break
            elif password_Choice == 'gp':
                print("Select Password length\n")
                passwordLength = input().strip()
                if passwordLength.isnumeric():
                    userpassword = generate_Password()
                else:
                    print("Enter a valid Password length\n") 
                break
            else:
                print("Invalid password please try again")
        save_user(create_user(username,userpassword))
        print("*"*85)
        print(f"Hello {username}, Your account has been created succesfully! Your password is: {userpassword}")
        print("*"*85)




    print("Hello Welcome to your credentials list. What would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : cc - create a new credentials, dc - display credentials, fc -find a credential, ex -exit the credentials list ")

        short_code = input().lower().strip()

        if short_code == 'cc':
            print("New Credentials")
            print("-"*10)

            print ("Account Name ...")
            account = input()

            print("User name ...")
            user = input()

            print("Password ...")
            password = input()

            save_credentials(create_credentials(account,user,password)) # create and save new credentials.
            print ('\n')
            print(f"New Credentials {account}") 
            print ('\n')
            print("{user} created")
            print ('\n')

        elif short_code == 'dc':

            if display_credentials():
                print("Here is a list of all your credentials")
                print('\n')

                for credentials in display_credentials():
                    print(f"{credentials.account} {credentials.user_name} {credentials.password}")
                    print('\n')

            else:
                print('\n')
                print("You dont seem to have any credentials saved yet")
                print('\n')

        elif short_code == 'fc':

            print("Enter the account name you want to search for")

            search_account = input()
            if check_existing_credentials(search_account):
                search_credentials = find_credentials(search_account)
                print(f"{search_credentials.account} {search_credentials.user_name}")
                print('-' * 20)

                print(f"Password.......{search_credentials.password}")
          
            else:
                print("Those credentials does not exist")

        elif short_code == "ex":
            print("Bye .......")
            break
    
        else:
            print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':

    main()