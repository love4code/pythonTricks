import shelve

# You can save variables in your python programs to Binary shelf files
# using the shelve module
# This way your program can restore data to variables from the harddrive

# Plain text is useful for creatingfiles that youll read in a text editor
# But if you want to save data from your python programs use Shelve

shelfFile = shelve.open('mydata')
cats = ['Meows', 'Mittens', 'Tiger']
shelfFile['cats'] = cats
shelfFile.close()

# | >>> import os
# | >>> os.chdir('Shelve_Module')
# | >>> os.getcwd()
# | '/Users/markgrover/Desktop/Automate_task/Shelve_Module'
# | >>> shelfFile = shelve.open('mydata')
# | Traceback (most recent call last):
# |   File "<input>", line 1, in <module>
# | NameError: name 'shelve' is not defined
# | >>> import shelve
# | >>> shelfFile = shelve.open('mydata')
# | >>> shelfFile['cats']
# | ['Meows', 'Mittens', 'Tiger']

shelfFile = shelve.open('mydata')
list(shelfFile.keys())
# | >>> list(shelfFile.keys())
# |
# | ['cats']
list(shelfFile.values())
# | >>> list(shelfFile.values())
# |
# | [['Meows', 'Mittens', 'Tiger']]
shelfFile.close()