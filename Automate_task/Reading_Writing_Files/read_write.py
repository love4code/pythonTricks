#!/Users/markgrover/Desktop/Automate_task/venv/bin/python3.5

import os
# | this variable is set to the correct separator for folders-separating
# | of the operating system
os.sep()
# | >>> os.sep
# | '/'

print(os.getcwd())
# | /Users/markgrover/Desktop/Automate_task
os.chdir('../')
print(os.getcwd())
# | /Users/markgrover/Desktop
os.listdir('Automate_task')
# | ['.idea',
# |  'Password_Locker',
# |  'Reading_Writing_Files',
# |  'Text_Manipulation',
# |  'venv']

# | Create new folders with os.makedirs()
os.makedirs('delicious/walnut/waffles')
# | >>> os.makedirs('delicious/walnut/waffles')
# |
# | >>> os.listdir()
# | ['__init__.py', 'delicious', 'read_write.py']
# | >>> os.listdir('./delicious')
# | ['walnut']
# | >>> os.listdir('./delicious/walnut/')
# | ['waffles']
# |
# ---------------------------------------------------------------->>>
# | Create paths in a way to work on any operating system
os.path.join('usr','bin','python')
# | 'usr/bin/python'

# | Returns a string of the absolute path of the argument
#    os.path.abspath(path)
# | Returns True if the argument is an Absolute Path
# | And False if it is a Relative path
#    os.path.isabs(path)
# | Calling os.path.relpath(path, start) will return a string of a
# | relative path from the start path to path
# | If start is not provided the cwd is used in its place

os.path.abspath('.')
#  '/Users/markgrover/Desktop/Automate_task/Reading_Writing_Files'

os.path.abspath('./Scripts')
#  '/Users/markgrover/Desktop/Automate_task/Reading_Writing_Files/Scripts'
os.path.abspath('Scripts')
#  '/Users/markgrover/Desktop/Automate_task/Reading_Writing_Files/Scripts'
os.path.isabs('.')
# False
os.path.isabs(os.path.abspath('.'))
# True
os.path.relpath('/Desktop','/')
# | >>> os.path.relpath('/Desktop','/')
# | 'Desktop'

os.path.relpath('/Desktop','/Automate_task/Reading_Writing_Files')
# | '../../Desktop'

# | Calling os.path.dirname() will return everything that comes before the
# last slash
# | Calling os.path.basename() will return everything after the last slash

path = '/Desktop/Automating_task/Password_Locker/pw.py'
os.path.basename(path)
# | >>> os.path.basename(path)
# | 'pw.py'
os.path.dirname(path)
# | >>> os.path.dirname(path)
# | '/Desktop/Automating_task/Password_Locker'

# | If you need a paths dirname and base name together you can call
# | os.path.split()
os.path.split(path)
# | >>> os.path.split(path)
# | ('/Desktop/Automating_task/Password_Locker', 'pw.py')

path.split(os.path.sep)
# | >>> path.split(os.path.sep)
# | ['', 'Desktop', 'Automating_task', 'Password_Locker', 'pw.py']

# FINDING FILE SIZES AND FOLDER CONTENTS --------------------------->>>

# | Calling os.path.getsize(path) will return the size in bytes of the file
# in the path argument

# | Calling os.listdir(path) will return a list of filename strings for
# each file in the path argument

os.path.getsize(os.getcwd()+os.sep+'read_write.py')
# | '/Users/markgrover/Desktop/
#          Automate_task/Reading_Writing_Files'+ '/' + 'read_write.py'
# | >>> os.path.getsize(os.getcwd()+os.sep+'read_write.py')
# | 2920

os.listdir('../../')
# | >>> os.listdir('../../')
# |
# | ['.DS_Store',
# |  '.htaccess',
# |  '.localized',
# |  'alienInvasion',
# |  'AquarianWorkBooks',
# |   ...]
# |
totalSize = 0
for filename in os.listdir('../../'):
    totalSize = totalSize + os.path.getsize(os.path.join('../../',filename))
print(totalSize)
# | >>> totalSize = 0
# |
# | >>> for filename in os.listdir('../../'):
# |         totalSize = totalSize + os.path.getsize(os.path.join('../../',filename))
# |
# | >>> print(totalSize)
# | 143593901

# PATH VALIDITY

# | Calling os.path.exists(path) will return a Bool val

# | Calling os.path.isfile(path) will return Bool val if exists and is a
#  file

# | Calling os.path.isdir(path) will return Bool val if exist and is folder

testFile = open(os.getcwd()+os.sep+'test.txt')
testFile.read()
# | 'Hello World, I would like to congratulate you\nFor all your hard work.\nThank you and good night\n\nSincerely\nMark Grover'
testFile = open(os.getcwd()+os.sep+'test.txt')
testFile.readlines()
# | ['Hello World, I would like to congratulate you\n', 'For all your hard work.\n', 'Thank you and good night\n', '\n', 'Sincerely\n', 'Mark Grover']


# | >>> testFile = open(os.getcwd()+os.sep+'test.txt','w')
# | >>> testFile.write('Life is Good!\n')
# | 14
# | >>> testFile.close()
# | >>> testFile = open(os.getcwd()+os.sep+'test.txt','a')
# | >>> testFile.write('Life is Good!\n')
# | 14
# | >>> testFile.close()
# | >>> content = testFile.read()
# | Traceback (most recent call last):
# |   File "<input>", line 1, in <module>
# | ValueError: I/O operation on closed file.
# | >>> testFile = open(os.getcwd()+os.sep+'test.txt')
# | >>> content = testFile.read()
# | >>> print(content)
# | Life is Good!
# | Life is Good!