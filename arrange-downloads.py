import os
import shutil
import time
from pathlib import Path

#Get Download Directory
home_dir = Path.home()
downloads_dir = os.path.join(home_dir, 'Downloads')

#Create Base Folders
folders = ['Video', 'Programs', 'Compressed', 'Documents', 'Music', 'Pictures', 'Others']
for folder in folders:
    try:
        create_folder = os.path.join(downloads_dir, folder)
        os.mkdir(create_folder)
    except FileExistsError:
        continue

#Loop through each file in the main folder and separate accordingly
list_files = os.listdir(downloads_dir)
extensions = {
    'Video' : ['mp4', 'mkv', 'avi', 'flv', 'webm', 'mov', 'wmv'],
    'Music' : ['wav', 'mp3', 'aac', 'ogg'],
    'Pictures' : ['png', 'jpg', 'jpeg', 'gif', 'bmp'],
    'Programs' : ['exe', 'msi', 'cmd', 'app', 'vb', 'scr', 'py', 'cpp', 'js', 'sh'],
    'Compressed' : ['zip', '7z', 'gz', 'rar', 'tar'],
    'Documents' : ['doc', 'docx', 'html', 'htm', 'odt', 'pdf', 'xls', 'xlsx', 'ods', 'ppt', 'pptx', 'txt']
}

def movefile(file, dest):
    destination_path = os.path.join(downloads_dir, dest)
    destination_path = os.path.join(destination_path, file)
    file_path = os.path.join(downloads_dir, file)
    shutil.move(file_path, destination_path)
print ("Working on Files....")
for file in list_files:
    file_extension = os.path.splitext(file)[1][1:]
    if file_extension:
        if file_extension in extensions['Video']:
            movefile(file, 'Video')
        elif file_extension in extensions['Music']:
            movefile(file, 'Music')
        elif file_extension in extensions['Pictures']:
            movefile(file, 'Pictures')
        elif file_extension in extensions['Programs']:
            movefile(file, 'Programs')
        elif file_extension in extensions['Compressed']:
            movefile(file, 'Compressed')
        elif file_extension in extensions['Documents']:
            movefile(file, 'Documents')
        else:
            movefile(file, 'Others')


time.sleep(0.5)
print ("Finished Moving Files")
time.sleep(0.5)
