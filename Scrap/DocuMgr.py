import shutil, os
from datetime import datetime
import pyglet, glooey

# Check for existing directories in root of drive
print('Checking for desired directories...')

Drives = {"Volume1": 'D',
          "Volume2": 'E',
          "Volume3": 'F'
          }

FORMATS = {
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
               ".heif", ".psd"],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".MP4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp", ".MOV"],
    "DOCUMENTS": [".oxps", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  "pptx", ".txt", ".in", ".out", ".csv", ".html5", ".html", ".htm", ".xhtml"],
    "ARCHIVES": [".a", ".ar", ".cpio", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"],
    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
    "LIBRARY": [".pdf", ".epub", ".mobi"],
    "XML": [".xml"],
    "APPLICATIONS": [".exe", ".msi"],
    "SCRIPTS": [".sh", ".ahk", ".py", ".bat"],
    "DISK_IMAGE": [".iso", ".img"],
    "3D_FILES": [".stl", ".obj", ".gcode", ".fdx", ".x3d", ".wrl", ".blend"]
}

# Select Drive to clean. Drives "Volume 2" and "Volume 3" should not be touched by this program yet
DRIVE = input(f"Select Drive to organize: {Drives.keys()}")

SELECT_DRIVE = f"{Drives[DRIVE]}:/"

DIRECTORIES = {"ARCHIVES": f"{SELECT_DRIVE}Documents/Compressed_Archives",
               "DISK_IMAGE": f"{SELECT_DRIVE}Disk_Images",
               "APPLICATIONS": f"{SELECT_DRIVE}Applications",
               "Downloads": f"{SELECT_DRIVE}Downloads",
               "DOCUMENTS": f"{SELECT_DRIVE}Documents",
               "LIBRARY": f"{SELECT_DRIVE}Documents/Electronic_Library",
               "AUDIO": f"{SELECT_DRIVE}Music",
               "IMAGES": f"{SELECT_DRIVE}Pictures",
               "VIDEOS": f"{SELECT_DRIVE}Videos",
               "3D_FILES": f"{SELECT_DRIVE}3D Objects",
               "Dir_1": f"{os.getcwd()}",
               "SCRIPTS": f"{SELECT_DRIVE}_scripts"
               }

# Check to make sure that necessary Directories exist
for folderName in os.walk(SELECT_DRIVE):
    if os.path.exists(DIRECTORIES["ARCHIVES"]) and \
            os.path.exists(DIRECTORIES["DISK_IMAGE"]) and \
            os.path.exists(DIRECTORIES["APPLICATIONS"]) and \
            os.path.exists(DIRECTORIES["Downloads"]) and \
            os.path.exists(DIRECTORIES["DOCUMENTS"]) and \
            os.path.exists(DIRECTORIES["LIBRARY"]) and \
            os.path.exists(DIRECTORIES["AUDIO"]) and \
            os.path.exists(DIRECTORIES["IMAGES"]) and \
            os.path.exists(DIRECTORIES["VIDEOS"]) and \
            os.path.exists(DIRECTORIES["3D_FILES"]) and \
            os.path.exists(DIRECTORIES['SCRIPTS']) and \
            os.path.exists(f"{DIRECTORIES['Dir_1']}/log.txt"):
        print('Directories found, proceeding...')
        break
    else:
        print('Directories were not found...')
        print('Making dir:' + DIRECTORIES["ARCHIVES"])
        try:
            os.mkdir(DIRECTORIES["ARCHIVES"])
            print('Created:' + 'Compressed_Archives')
        except FileExistsError:
            print("Directory Compressed_Archives exists. Continuing")

        print('Making dir:' + DIRECTORIES["SCRIPTS"])
        try:
            os.mkdir(DIRECTORIES["SCRIPTS"])
            print('Created:' + '_scripts')
        except FileExistsError:
            print("Directory _scripts exists. Continuing")

        print('Making dir:' + DIRECTORIES["DISK_IMAGE"])
        try:
            os.mkdir(DIRECTORIES["DISK_IMAGE"])
            print('Created:' + 'DISK_IMAGE')
        except FileExistsError:
            print("Directory Disk_Images exists. Continuing")

        print('Making dir:' + DIRECTORIES["APPLICATIONS"])
        try:
            os.mkdir(DIRECTORIES["APPLICATIONS"])
            print('Created:' + 'APPLICATIONS')
        except FileExistsError:
            print("Directory Applications exists. Continuing")

        print('Making dir:' + DIRECTORIES["LIBRARY"])
        try:
            os.mkdir(DIRECTORIES["LIBRARY"])
            print('Created:' + 'Electronic_Library')
        except FileExistsError:
            print("Directory Electronic_Library exists. Continuing")
        try:
            log = open(f"{DIRECTORIES['Dir_1']}/log.txt", "w")
            log.close()
            print()
        except:
            pass

'''Start Cleaning from Downloads Folder'''
# Move working directory to Downloads folder
os.chdir(DIRECTORIES['Downloads'])
print('Current directory: ' + os.getcwd())
log = open(f"{DIRECTORIES['Dir_1']}/log.txt", "a")
log.write('\n' + "-" * 7 + '\n' + str(datetime.now()) + '\n' + "-" * 7)
for key in FORMATS:
    for filename in os.listdir(DIRECTORIES['Downloads']):
        for items in FORMATS[key]:
            if filename.endswith(items):
                try:
                    shutil.move(filename, DIRECTORIES[key])
                    log.write('\n' + f"{filename} moved to {DIRECTORIES[key]}")
                    print('\n' + f"{filename} moved to {DIRECTORIES[key]}")
                except:
                    os.remove(filename)
                    log.write('\n' + f"{filename} could not be moved to {DIRECTORIES[key]}...DELETED")
                    print('\n' + f"{filename} could not be moved to {DIRECTORIES[key]}")
                    pass

# Run CCLEANER
os.chdir("C:\Program Files\CCleaner")
os.system('cmd /c "CCleaner64.exe/AUTO"')
log.write('\n' + "Ran CCleaner...")


# TODO:Drive backup feature
"""
def backup(src,dest):
    SRC_DIR = {"Archives": f"{src}Compressed_Archives",
                   "Disk_Images": f"{src}Disk_Images",
                   "Applications": f"{src}Applications",
                   "Documents": f"{src}Documents",
                   "Library": f"{src}Documents/Electronic_Library",
                   "Music": f"{src}Music",
                   "Pictures": f"{src}Pictures",
                   "Videos": f"{src}Videos",
                   "3D_Files": f"{src}3D Objects",
                   "Root": f"{src}:/"
                   }

    DEST_DIR = {"Archives": f"{dest}Compressed_Archives",
                       "Disk_Images": f"{dest}Disk_Images",
                       "Applications": f"{dest}Applications",
                       "Documents": f"{dest}Documents",
                       "Library": f"{dest}Documents/Electronic_Library",
                       "Music": f"{dest}Music",
                       "Pictures": f"{dest}Pictures",
                       "Videos": f"{dest}Videos",
                       "3D_Files": f"{dest}3D Objects",
                       "Root": f"{dest}:/"
                       }
    for values in SRC_DIR.values():
        try:
            shutil.copytree(SRC_DIR[values],DEST_DIR[values])
        # Directories are the same
        except shutil.Error as e:
            print('Directory not copied. Error: %s' % e)
        # Any error saying that the directory doesn't exist
        except OSError as e:
            print('Directory not copied. Error: %s' % e)




answer = None
while answer not in ("y","n","yes","no"):
    answer = input("Would you like to backup any drives? Enter yes (y) or no (n)")
    if answer == "no" or answer == "n":
        print("Process Complete. File structure re-organized." + "\nCheck log file for more information")
    elif answer == "yes" or answer == "y":
        src_drv = f"{input(f'Select source Drive: {Drives.keys()}')}"
        dest_drv = f"{input(f'Select destination Drive: {Drives.keys()}')}"
        backup(Drives[f'{src_drv}'],Drives[f'{dest_drv}'])
    else:
        print("Please enter yes (y) or no (n)")
"""
log.close()
exit()
