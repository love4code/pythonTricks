import os, shutil

# Copy File from Destination location to the new location
# if filename is declared in the new location then the file will be renamed
shutil.copy(os.getcwd()+'/Shelve_Module/shelve_mod_ex.py',
            os.getcwd()+'/Shutil_Usage')
# Returns
#  '/Users/markgrover/Desktop/Automate_task/Shutil_Usage/shelve_mod_ex.py'

# shutil.copy() copies a single file
# shutil.copytree copies a complete folder and all its contents
shutil.copytree(os.getcwd()+'/Shelve_Module/',os.getcwd()+'/Shelve_Backup')
#Returns:
#  '/Users/markgrover/Desktop/Automate_task/Shelve_Backup'

# Move a folder or file
# careful for move. if it doesnot find a folder specified it will rename
# the file to the specified location as a file without an extension
shutil.move(os.getcwd()+'/Shelve_Module/',os.getcwd()+'/Shutil_Usage')
# Returns:
#  '/Users/markgrover/Desktop/Automate_task/Shutil_Usage/Shelve_Module'