#!/usr/bin/env python3.8

from credentials import Credentials
from credentials import Password
from user import User

def create_password(passwordlength):
    '''
    Function to create a new password length
    '''
    new_password = Password(passwordlength)
    return new_user

def save_password(password):
    '''
    Function to save password length
    '''
    password.save_password()

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

def login_user(username,userpassword):
    """
    function that checks whether a user exist and then login the user in.
    """
    check_user = User.verify_user(username,userpassword)
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

def generate_Password(passwordLength):
    '''
    generates a random password for the user.
    '''
    auto_password=Credentials.generatePassword(passwordLength)
    return auto_password

def copy_password(account):
    """
    A function that copies the password using the pyperclip framework
    """
    return Credentials.copy_password(account)

def main():
    print("Hello Welcome to your Password Store...\n Please enter one of the following to proceed.\n CA ---  Create New Account  \n SI ---  Sign in to existing Account  \n")
    short_code=input("").lower().strip()
    print('*' * 50)

    if short_code == "ca":
        print("Create Account ... \n")
        print('*' * 40)
        username = input("User_name: \n")
        while True:

            print(" TP - To type your own pasword:\n GP - To generate random Password")
            print('*' * 30)
            password_Choice = input().lower().strip()
            
            if password_Choice == 'tp':
                userpassword = input("Enter Password\n")
                
            elif password_Choice == 'gp':
                print("Select Password length\n")
                print('*' * 30)
                passwordLength = input().strip()
                if passwordLength.isnumeric():
                    userpassword = generate_Password(passwordLength)
                else:
                    print("Enter a valid Password length\n")
                    print('*' * 40) 
                break
            else:
                print("Invalid password please try again")
                print('*' * 30)
        save_user(create_user(username,userpassword))
        print("*"*40)
        print(f"Welcome {username} To PassWord Locker Manager,\n Your account has been created succesfully!\n Your password is: {userpassword}")
        print("*"*40)

    elif short_code == "si":
        print("Enter your User name and Password to log in:")
        print('*' * 40)
        username = input("User name: ")
        userpassword = input("Password: ")

        login = login_user(username,userpassword)
        if login_user == login: 
            print(f"Hello {username}.Welcome To PassWord Locker Manager \n")  
            print('*' * 30)
        else:
            print("Invalid password. \n We would ask you to please try again. \n However we are yet to set up a database to save user credentials.")
            print('*' * 30)
    while True:        
        print("What would you like to do? \n")
        print('*' * 30)
        print('\n')
        print("Use these short codes : cc - create a new credentials, dc - display credentials, fc -find a credential, ex -exit the credentials list ")
        print('*' * 30)
        short_code = input().lower().strip()

        if short_code == 'cc':
            print("New Credentials")
            print("-"*20)

            print ("Account Name ... \n")
            account = input()
            print("-"*10)

            print("User name ... \n")
            user = input()
            print("-"*10)

            print("Password ... \n")
            password = input()
            print("-"*10)

            save_credentials(create_credentials(account,user,password)) # create and save new credentials.
            print("*"*20)
            print ('\n')
            print(f"New Credentials {account}") 
            print ('\n')
            print("{user} created")
            print ('\n')
            print("*"*20)

        elif short_code == 'dc':

            if display_credentials():
                print("Here is a list of all your credentials\n")
                print("*"*20)

                for credentials in display_credentials():
                    print(f"{credentials.account} {credentials.user_name} {credentials.password}")
                    print('\n')
                    print("*"*10)

            else:
                print('\n')
                print("You dont seem to have any credentials saved yet")
                print('\n')
                print("*"*20)

        elif short_code == 'fc':

            print("Enter the account name you want to search for")
            print("*"*20)

            search_account = input()
            if check_existing_credentials(search_account):
                search_credentials = find_credentials(search_account)
                print(f"{search_credentials.account} {search_credentials.user_name} \n")
                print('-' * 20)

                print(f"Password.......{search_credentials.password}")
                print("*"*10)
          
            else:
                print("Those credentials does not exist")
                print("*"*10)

        elif short_code == "ex":
            print("Bye ....... \n")
            print("*"*20)
            break
    
        else:
            print("I really didn't get that. Please use the short codes")
            print("*"*20)

if __name__ == '__main__':

    main()