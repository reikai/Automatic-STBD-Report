#! python3
# Generates fresh STBD report, saves it to share drive, and emails interested parties.

import pandas as pd
import numpy as np
from selenium import webdriver
from datetime import datetime
import os
import time

# Email variables. To List, Subject Line, Message body.
ToList = ['ty.tippawang@vizientinc.com']
SubjectLine = 'Reporting Test'
MessageBody = '''
A new L-Vizient report has just been run 
'''

# This is where the file gets downloaded. chdir to the folder, get the latest file.
DLlocation = r'C:\Python Practice 3\Reporting Practice'
os.chdir(DLlocation)
files = [x for x in os.listdir('.') if x.endswith('.xlsx')]
newest = max(files, key=os.path.getctime)  # newest = the latest modified file

df = pd.read_excel(newest)            # Read in Excel file into Pandas Dataframe.

df.columns = df.iloc[0,:]             # Overwrite the columns to be the first row.
df = df.drop(df.index([[0]]))         # Eliminate the first row.
df = df.drop(df.index([[-1]]))        # Eliminate the last row.

# TODO: Leave the original data on one tab, but also make a Pivot Table on another tab.

# TODO: Save the file in a team location.

# TODO: Log on to Gmail and email the file out.
def GmailLogin():
    # Define credentials
    username = 'practicingpython006@gmail.com'
    password = 'practicingpython'

    # Open Gmail in Firefox
    browser = webdriver.Firefox()
    browser.get('https://gmail.com')
    print('Opening Gmail...')

    # Select login field, input username
    print('Attempting to login...')
    LoginElem = browser.find_element_by_id('Email')
    LoginElem.send_keys(username)

    # Click Next to unlock/unhide the password field
    NextButton = browser.find_element_by_id('next')
    NextButton.click()

    # Select Password field, input password
    PassElem = browser.find_element_by_id('Passwd')
    PassElem.send_keys(password)

    # Click Sign in button, wait 5 seconds.
    print('Username & Password have been inputted. Signing in...')
    SignInButton = browser.find_element_by_id('signIn')
    SignInButton.click()
    time.sleep(5)         # This way, the program doesn't execute faster than a slow internet connection

def Compose(toList, subjectText, bodyText):
    # Click compose to cause the in-browser popup
    ComposeButton = browser.find_element_by_class_name('z0')
    ComposeButton.click()


# TODO: Close the browser, logging out of everything. (Closing a Selenium browser is the equivalent of logging off.)
