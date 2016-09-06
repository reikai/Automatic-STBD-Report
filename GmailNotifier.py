#! python3

# Uses a Gmail account to notify you of anything.
# You can input a To: list, a Subject line, and messages.
# Emails come from Gmail account: practicingpython006@gmail.com.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Gmail(object):
    def __init__(self):
        pass

    def sendemail(self, toList, subjectText, bodyText):
        username = 'practicingpython006@gmail.com'
        password = 'practicingpython'

        # Open Gmail in Firefox
        browser = webdriver.Firefox()
        browser.get('https://gmail.com')
        print('Opening Gmail...')
        time.sleep(2)

        # Select login field, input username
        print('Attempting to login...')
        LoginElem = browser.find_element_by_id('Email')
        LoginElem.send_keys(username)

        # Click Next to unlock/unhide the password field
        NextButton = browser.find_element_by_id('next')
        NextButton.click()
        time.sleep(1)

        # Select Password field, input password
        PassElem = browser.find_element_by_id('Passwd')
        PassElem.send_keys(password)

        # Click Sign in button, wait 5 seconds.
        print('Username & Password have been inputted. Signing in...')
        SignInButton = browser.find_element_by_id('signIn')
        SignInButton.click()
        time.sleep(3)         # This way, the program doesn't execute faster than a slow internet connection
        print('Gmail should now be open.')

        # Click compose to cause the in-browser popup
        ComposeButton = browser.find_element_by_class_name('z0')
        ComposeButton.click()
        time.sleep(2)

        # select To field, Input toList
        ToFieldElem = browser.find_element_by_class_name('vO')

        # Case for more than 1 email target
        if len(toList) > 1:
            for email in self.ToList:
                ToFieldElem.send_keys(email)
                ToFieldElem.send_keys(Keys.TAB)
                ToFieldElem = browser.find_element_by_class_name('vO')
        # Case for exactly 1 email target
        elif len(toList) == 1:
            ToFieldElem.send_keys(toList[0])
            ToFieldElem.send_keys(Keys.TAB)
        # Error case
        else:
            print('The toList variable is messed up. Make sure it\'s a list of email addresses.')

        # Write the email:
        print('Writing email...')
        # Input subjectText
        SubjectElem = browser.find_element_by_id(':97')
        SubjectElem.send_keys(subjectText)
        # Input bodyText
        bodyelem = browser.find_element_by_id(':ac')
        bodyelem.send_keys(bodyText)
        bodyelem.send_keys('''
Warning: This is an automated message.
Do not reply directly to this address.
Direct all comments, questions, concerns to:
Ty.Tippawang@vizientinc.com''')

        # Send message:
        bodyelem.send_keys(Keys.CONTROL, Keys.ENTER)

        print('****************************************** \n\nMessage sent to the following people:')
        for name in toList:
            print(name)
        print('Subject: ' + subjectText)
        print('Message:' + bodyText)
        print('\n******************************************')

        browser.close()