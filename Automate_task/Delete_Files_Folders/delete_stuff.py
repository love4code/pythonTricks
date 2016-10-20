import os, shutil
# to delete a file or a single empty folder you use functions from the os
#  module

# To delete a folder and all of its contents you use shutil

# Be careful when running the kinds of functions.
# run the code with print statements as a dry run before deleting forever!

# delete all .txt files in a given directory
for filename in os.listdir():
    if filename.endswith('txt'):
        #os.unlink(filename)
        print(filename)

# Delete a folder and its contents
shutil.rmtree('location_to_folder')
print('location_to_folder')

# Safe Deletes with send2trash Module

import send2trash

baconFile = open('baconFile.txt', 'a') # Creates a file
baconFile.write('Bacon is not a Vegetable.')
# 25
baconFile.close()
send2trash.send2trash('baconFile.txt')
# If your program needs to free up disk space use the os and shutil
# functions
