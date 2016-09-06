#! python3
# Generates fresh STBD report, saves it to share drive, and emails interested parties.

import pandas as pd
import numpy as np

from datetime import datetime
import os
import time

# Email variables. To List, Subject Line, Message body.
ToList = ['ty.tippawang@vizientinc.com', 'creativepsp@gmail.com']
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



# TODO: Close the browser, logging out of everything.

