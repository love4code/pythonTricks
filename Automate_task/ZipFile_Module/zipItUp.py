import zipfile, os

os.chdir('dir_name') # move to the folder within the exampleZip.zip

exampleZip = zipfile.ZipFile('exampleZip.zip')

exampleZip.namelist()
# Creates a list of file and folder names

spamInfo = exampleZip.getinfo('filename') # name from namelist()
print(spamInfo.file_size)
# 212839
print(spamInfo.compress_size)
print('Compressed File Size is %sx smaller!' % (round(spamInfo.file_size /
 spamInfo.comress_size, 2)))

exampleZip.close()
# To Add files to a zip object open the object with the 'a' flag
#

# The extractall() method for ZipFile objects
# Extracts all the the files and folders from a Zip CWD
# Optionally you can pass a Folder name in as a parameter
# if the Folder is non existent One will be created

extractZip = zipfile.ZipFile('exampleZip.zip')
exampleZip.extractall()
exampleZip.close()

# The extract() method of the ZIpFile Object extracts a single file
# from the zip file

exampleZip.extract('filename.txt')
exampleZip.extract('filename.txt', '/some/new/folders/')
exampleZip.close()

# Optionally you can pass in the name of the folder to contain the file
# if the folder is non existent it/they will be created

# To Create Your Own ZIP
# You must open the ZipFile Object in 'write mode'
# by passing 'w' as the Second Parameter
# the first parameter is the name of the new zip file

newZip = zipfile.ZipFile('new.zip', 'w')

# The write() methos takes 2 parameters
# string of the filename to add
# the compression type which tells the computer what algorithm to use
# Always use ZIP_DEFLATED because it works well on all types of data
newZip.write('file.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()

# Keep in mind opening a zip object in write mode will erase old content
# If you want to add to a zip file open the ZipFile Obj with the 'a' flag
