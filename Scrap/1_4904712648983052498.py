import shutil, os

# Check for existing directories in root of drive
print('Checking for desired directories...')

Drive = {"localDisk": 'D',
          "Volume1": 'X',
          "Volume2": 'Y',
          "Volume3": 'Z'
          }

FORMATS = {
    "HTML": [".html5", ".html", ".htm", ".xhtml"],
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
               ".heif", ".psd"],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp"],
    "DOCUMENTS": [".oxps", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  "pptx",".txt", ".in", ".out",".csv"],
    "ARCHIVES": [".a", ".ar", ".cpio", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"],
    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
    "EPUBS": [".pdf", ".epub", ".mobi"],
    "PYTHON": [".py"],
    "XML": [".xml"],
    "APPLICATIONS": [".exe", ".msi"],
    "SHELL": [".sh"],
    "DISK_IMAGE": [".iso", ".img"],
    "3D_Files":[".stl", ".obj", ".gcode"]
}

#Select Drive to clean. Drives "Volume 2" and "Volume 3" should not be touched by this program yet
SELECT_DRIVE = f"{Drive['localDisk']}:/"

DIRECTORIES = {"Archives": f"{SELECT_DRIVE}Compressed_Archives",
               "Disk_Images": f"{SELECT_DRIVE}Disk_Images",
               "Applications": f"{SELECT_DRIVE}Applications",
               "Downloads": f"{SELECT_DRIVE}Downloads",
               "Documents": f"{SELECT_DRIVE}Documents",
               "Epubs": f"{SELECT_DRIVE}Documents/Electronic_Publications",
               "Music": f"{SELECT_DRIVE}Music",
               "Pictures": f"{SELECT_DRIVE}Pictures",
               "Videos": f"{SELECT_DRIVE}Videos"
               }


#Check to make sure that necessary Directories exist
for folderName in os.walk(SELECT_DRIVE):
    if os.path.exists(DIRECTORIES["Archives"]) and \
            os.path.exists(DIRECTORIES["Disk_Images"]) and \
            os.path.exists(DIRECTORIES["Applications"]) and \
            os.path.exists(DIRECTORIES["Downloads"]) and \
            os.path.exists(DIRECTORIES["Documents"]) and \
            os.path.exists(DIRECTORIES["Epubs"]) and \
            os.path.exists(DIRECTORIES["Music"]) and \
            os.path.exists(DIRECTORIES["Pictures"]) and \
            os.path.exists(DIRECTORIES["Videos"]):
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

        print('Making dir:' + DIRECTORIES["Epubs"])
        try:
            os.mkdir(DIRECTORIES["Epubs"])
            print('Created:' + 'Electronic_Publications')
        except FileExistsError:
            print("Directory Electronic Applications exists. Continuing")


'''Start Cleaning from Downloads Folder'''
#Move working directory to Downloads folder

os.chdir(DIRECTORIES['Downloads'])
print('Current directory: ' + os.getcwd())

for filename in os.listdir(DIRECTORIES['Downloads']):
    for items in FORMATS["IMAGES"]:
        if filename.endswith(items):
            try:
                shutil.move(filename, DIRECTORIES["Pictures"])
                print(f"{filename} moved to {DIRECTORIES['Pictures']}")
            except:
                print(f"{filename} could not be moved to {DIRECTORIES['Pictures']}...")
                pass

    for items in FORMATS["AUDIO"]:
        if filename.endswith(items):
            try:
                shutil.move(filename, DIRECTORIES["Music"])
                print(f"{filename} moved to {DIRECTORIES['Music']}")
            except:
                print(f"{filename} could not be moved to {DIRECTORIES['Music']}...")
                pass

    for items in FORMATS["DOCUMENTS"]:
        if filename.endswith(items):
            try:
                shutil.move(filename, DIRECTORIES["Documents"])
                print(f"{filename} moved to {DIRECTORIES['Documents']}")
            except:
                print(f"{filename} could not be moved to {DIRECTORIES['Documents']}...")
                pass

    for items in FORMATS["VIDEOS"]:
        if filename.endswith(items):
            try:
                shutil.move(filename, DIRECTORIES["Videos"])
                print(f"{filename} moved to {DIRECTORIES['Videos']}")
            except:
                print(f"{filename} could not be moved to {DIRECTORIES['Videos']}...")
                pass

    for items in FORMATS["ARCHIVES"]:
        if filename.endswith(items):
            try:
                shutil.move(filename, DIRECTORIES["Archives"])
                print(f"{filename} moved to {DIRECTORIES['Archives']}")
            except:
                print(f"{filename} could not be moved to {DIRECTORIES['Archives']}...")
                pass

    for items in FORMATS["ARCHIVES"]:
        if filename.endswith(items):
            try:
                shutil.move(filename, DIRECTORIES["Archives"])
                print(f"{filename} moved to {DIRECTORIES['Archives']}")
            except:
                print(f"{filename} could not be moved to {DIRECTORIES['Archives']}...")
                pass

    for items in FORMATS["EPUBS"]:
        if filename.endswith(items):
            try:
                shutil.move(filename, DIRECTORIES["Epubs"])
                print(f"{filename} moved to {DIRECTORIES['Epubs']}")
            except:
                 print(f"{filename} could not be moved to {DIRECTORIES['Epubs']}...")
                 pass

    for items in FORMATS["APPLICATIONS"]:
        if filename.endswith(items):
            try:
                shutil.move(filename, DIRECTORIES["Applications"])
                print(f"{filename} moved to {DIRECTORIES['Applications']}")
            except:
                 print(f"{filename} could not be moved to {DIRECTORIES['Applications']}...")
                 pass

    for items in FORMATS["APPLICATIONS"]:
        if filename.endswith(items):
            try:
                shutil.move(filename, DIRECTORIES["Applications"])
                print(f"{filename} moved to {DIRECTORIES['Applications']}")
            except:
                 print(f"{filename} could not be moved to {DIRECTORIES['Applications']}...")
                 pass

    for items in FORMATS["DISK_IMAGE"]:
        if filename.endswith(items):
            try:
                shutil.move(filename, DIRECTORIES["Disk_Images"])
                print(f"{filename} moved to {DIRECTORIES['Disk_Images']}")
            except:
                 print(f"{filename} could not be moved to {DIRECTORIES['Disk_Images']}...")
                 pass

print("Process Complete. File structure re-organized.")
exit()
