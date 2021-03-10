"""import shutil, os

class DirectoryOrganizer:

    def checkFiles(SELECT_DRIVE):
        DIRECTORIES = {"Archives": f"{SELECT_DRIVE}Compressed_Archives",
                       "Disk_Images": f"{SELECT_DRIVE}Disk_Images",
                       "Applications": f"{SELECT_DRIVE}Applications",
                       "Downloads": f"{SELECT_DRIVE}Downloads",
                       "Documents": f"{SELECT_DRIVE}Documents",
                       "Library": f"{SELECT_DRIVE}Documents/Electronic_Library",
                       "Music": f"{SELECT_DRIVE}Music",
                       "Pictures": f"{SELECT_DRIVE}Pictures",
                       "Videos": f"{SELECT_DRIVE}Videos",
                       "3D_Files": f"{SELECT_DRIVE}3D Objects",
                       "Dir_1": f"{os.getcwd()}"
                       }

        # Check to make sure that necessary Directories exist
        for folderName in os.walk(SELECT_DRIVE):
            if os.path.exists(DIRECTORIES["Archives"]) and \
                    os.path.exists(DIRECTORIES["Disk_Images"]) and \
                    os.path.exists(DIRECTORIES["Applications"]) and \
                    os.path.exists(DIRECTORIES["Downloads"]) and \
                    os.path.exists(DIRECTORIES["Documents"]) and \
                    os.path.exists(DIRECTORIES["Library"]) and \
                    os.path.exists(DIRECTORIES["Music"]) and \
                    os.path.exists(DIRECTORIES["Pictures"]) and \
                    os.path.exists(DIRECTORIES["Videos"]) and \
                    os.path.exists(DIRECTORIES["3D_Files"]) and \
                    os.path.exists(f"{DIRECTORIES['Dir_1']}/log.txt"):
                print('Directories found, proceeding...')
                break
            else:
                print('Directories were not found...')
                print('Making dir:' + DIRECTORIES["Archives"])
                try:
                    os.mkdir(DIRECTORIES["Archives"])
                    print('Created:' + 'Compressed_Archives')
                except FileExistsError:
                    print("Directory Compressed_Archives exists. Continuing")

                print('Making dir:' + DIRECTORIES["Disk_Images"])
                try:
                    os.mkdir(DIRECTORIES["Disk_Images"])
                    print('Created:' + 'Disk_Images')
                except FileExistsError:
                    print("Directory Disk_Images exists. Continuing")

                print('Making dir:' + DIRECTORIES["Applications"])
                try:
                    os.mkdir(DIRECTORIES["Applications"])
                    print('Created:' + 'Applications')
                except FileExistsError:
                    print("Directory Applications exists. Continuing")

                print('Making dir:' + DIRECTORIES["Library"])
                try:
                    os.mkdir(DIRECTORIES["Library"])
                    print('Created:' + 'Electronic_Library')
                except FileExistsError:
                    print("Directory Electronic Applications exists. Continuing")
                try:
                    log = open(f"{DIRECTORIES['Dir_1']}/log.txt", "w")
                    log.close()
                    print()
                except:
                    pass

"""
import os
os.chdir("D:/")
for (rootDir, subDirs, files) in os.walk("."):
    for file in files:
        print(file)
    for subDir in subDirs:
        print(subDir)