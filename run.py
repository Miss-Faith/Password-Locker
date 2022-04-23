#!/usr/bin/env python3.8

from credentials import Credentials

def create_credentials(account,user,password):
    '''
    Function to create a new credential
    '''
    new_credentials = Contact(account,user,password)
    return new_credentials