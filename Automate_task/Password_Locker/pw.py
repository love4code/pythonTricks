#!/Users/markgrover/Desktop/Automate_task/venv/bin/python3.5
# pw.py An insecure password locker program

PASSWORDS = {
    'email': 'emailpassword',
    'website':'websitepassword',
    'lifesavings':'lifesavingspasssword'
}

import sys
import pyperclip

if len(sys.argv) < 2:
    print('USAGE: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line argument a the second position
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)