import shutil, os, pathlib
from pathlib import Path

home = str(Path.home())


"""
for folderName, subfolders, filenames in os.walk('D:\\Downloads'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)

    print('')
"""

def find(name, path):
    os.chdir(path)
    print('Starting search from: ' + path + '\nSearching...')
    for folderName, subfolders, filenames in os.walk(path):
        #if name in folderName:
        #    return os.path.join(folderName)
        for name in folderName:
            return folderName


print(find('\Documents', home))