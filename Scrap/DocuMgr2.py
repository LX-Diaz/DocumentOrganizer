import shutil, os

#Check for existing directories in root of drive
os.chdir('D:\\')
print('Checking for desired directories...')

for folderName in os.walk('D:\\'):
    if os.path.exists('Compressed_Archives') and\
            os.path.exists('Disk_Images') and\
            os.path.exists('Applications') and\
            os.path.exists('Downloads') and\
            os.path.exists('Documents') and\
            os.path.exists('D:\\Documents\Electronic_Publications') and\
            os.path.exists('Music') and\
            os.path.exists('Pictures') and\
            os.path.exists('Videos'):
        print('Directories found, proceeding...')
        break
    else:
        print('Directories were not found...')
        print('Making dir:' + 'D:\\Compressed_Archives')
        try:
            os.mkdir('D:\\Compressed_Archives')
            print('Created:' + 'Compressed_Archives')
        except FileExistsError:
            print("Directory Compressed_Archives exists. Continuing")

        print('Making dir:' + 'D:\\Disk_Images')
        try:
            os.mkdir('D:\\Disk_Images')
            print('Created:' + 'Disk_Images')
        except FileExistsError:
            print("Directory Disk_Images exists. Continuing")

        print('Making dir:' + 'D:\\Applications')
        try:
            os.mkdir('D:\\Applications')
            print('Created:' + 'Applications')
        except FileExistsError:
            print("Directory Applications exists. Continuing")

        print('Making dir:' + 'D:\\Documents\Electronic_Publications')
        try:
            os.mkdir('D:\\Documents\Electronic_Publications')
            print('Created:' + 'Electronic_Publications')
        except FileExistsError:
            print("Directory Electronic Applications exists. Continuing")


'''Start Cleaning from Downloads Folder'''
#Move working directory to Downloads folder
os.chdir('D:\\Downloads')
print('Current directory: ' + os.getcwd())


#Move all stray compressed files to a directory called "Compressed_Archives" at root of D:\\ drive
for filename in os.listdir():
    if filename.endswith('.zip') or \
            filename.endswith('.rar') or \
            filename.endswith('.gz') or \
            filename.endswith('.7z') or \
            filename.endswith('.tgz'):
        try:
            shutil.move(filename, 'D:\\Compressed_Archives')
        print('Moved ' + filename + ' to "D:\\Compressed_Archives"')

#Move all stray '.msi' and '.exe' to a folder in the root directory, called 'Installation_File_Backups'
    elif filename.endswith('.exe') or \
            filename.endswith('.msi'):
        shutil.move(filename, 'D:\\Applications')
        print('Moved ' + filename + ' to "D:\\Applications"')


#Move all Office-related and text documents to the 'Documents' directory
    elif filename.endswith('.txt') or\
            filename.endswith('.html') or\
            filename.endswith('htm') or\
            filename.endswith('.docx') or\
            filename.endswith('.doc') or\
            filename.endswith('.odt'):
        shutil.move(filename, 'D:\\Documents')
        print('Moved ' + filename + ' to "D:\\Documents"')

#Move Electronic Publications to Documents and move them to appropriate folder
    elif filename.endswith('.pdf') or\
            filename.endswith('.epub') or\
            filename.endswith('.mobi'):
        shutil.move(filename, 'D:\\Documents\Electronic_Publications')
        print('Moved ' + filename + ' to "D:\\Documents\Electronic_Publications"')

#Move all isos and disk image files to a 'Disk_Images' directory in the root of D:\\ drive
    elif filename.endswith('.iso') or\
            filename.endswith('.img'):
        shutil.move(filename, 'D:\\Disk_Images')
        print('Moved ' + filename + ' to "D:\\Disk_Images"')

#Move all music and audio file to the 'Music' directory
    elif filename.endswith('.mp3') or\
            filename.endswith('.wma') or\
            filename.endswith('.mid'):
        shutil.move(filename, 'D:\\Music')
        print('Moved ' + filename + ' to "D:\\Music"')
#Move all images to the 'Pictures' directory
    elif filename.endswith('.jpg') or\
            filename.endswith('.gif') or\
            filename.endswith('.png') or \
            filename.endswith('.xcf') :
        shutil.move(filename, 'D:\\Pictures')
        print('Moved ' + filename + ' to "D:\\Pictures"')
#Move all videos to the 'Videos' directory
    elif filename.endswith('.mp4') or\
            filename.endswith('.mkv'):
        shutil.move(filename, 'D:\\Videos')
        print('Moved ' + filename + ' to "D:\\Videos"')
#Change working directory to Documents
    os.chdir('D:\\Documents')


print("Process Complete. File structure re-organized.")
exit()
