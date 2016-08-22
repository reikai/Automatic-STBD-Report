#! python3
# Generates fresh STBD report, saves it to share drive, and emails interested parties.

from selenium import webdriver

URL = 'https://adfs.alliancewebs.net/adfs/ls/?wa=wsignin1.0&wtrealm=http%3a%2f%2fallianceprod.cloud.infor.com%2fadfs%2fservices%2ftrust&wctx=5aa26fcd-2991-41bc-b9ff-2e34216ebadc'
URL2 = 'https://allianceprod.cloud.infor.com/LawsonBI/SitePages/Default.aspx'

# Log on to Lawson/LBI/whatever.
username = r'VHACORP\ttippawa'
password = input('Please enter Ty\'s password.')
browser = webdriver.Firefox()
browser.get(URL)

# Input the username.
print('Inputting username...')
usernameElem = browser.find_element_by_id('ctl00_ContentPlaceHolder1_UsernameTextBox')
usernameElem.send_keys(username)
print('Username has been inputted.')

# Input the password.
print('Inputting password...')
passwordElem = browser.find_element_by_id('ctl00_ContentPlaceHolder1_PasswordTextBox')
passwordElem.send_keys(password)
print('Password has been inputted.')

# Sign in once. This shouldn't work, based on testing.
print('Login attempt one.')
signInButtonElem = browser.find_element_by_id('ctl00_ContentPlaceHolder1_SubmitButton')
signInButtonElem.click()
print('Login attempt one completed.')

# Sign in again.
print('Login attempt 2. If this fails, end the program.')
browser.get(URL2)
continueToSignInElem = browser.find_element_by_id('ctl00_ContentPlaceHolder1_PassiveSignInButton')
continueToSignInElem.click()

# TODO: Navigate the menus to the STBD report. Click the report and cause the popup.


# TODO:
# TODO:
# TODO:
# TODO:
# TODO:
# TODO:
