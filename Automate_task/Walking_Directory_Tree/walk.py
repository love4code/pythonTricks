import os

# The os.walk() function returns 3 values each time trough the loop
# 1.  A String of The Current Folders Name
# 2.  A List of Strings of the Folders in the current folder
# 3. A List of strings of the files in the current folder

for folderName, subFolders, fileNames in os.walk(os.getcwd()):
    print('The Current folder is ' + folderName)

    for subFolder in subFolders:
        print('Subfolder of ' + folderName + ': ' + subFolder)

    for fileName in fileNames:
        print('File Inside ' + folderName + ': ' + fileName)


