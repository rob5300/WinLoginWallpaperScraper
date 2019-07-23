'''
Author: rob5300
Requirements: Pillow


'''

import datetime
import os
import shutil
from os import stat

from PIL import Image

# Min size in bytes
minbytes = 100000

# Max days old
maxdays = 10

# Path to logon images
# Replace rob53 with your user folder name to fix the directory path.
imagespath = "C:\\Users\\rob53\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets"

def GetImages():
    # Start getting the files in the directory.
    ourpath = os.path.dirname(__file__)
    files = os.listdir(imagespath)

    CreateDirs(ourpath)

    for file in files:
        m = os.stat(imagespath + "\\" + file)

        # Check if file size is large enough
        if(m.st_size < minbytes): continue

        #if this can be better please tell me
        filedate = datetime.datetime.fromtimestamp(m.st_mtime)
        daydifference = datetime.datetime.now() - filedate

        #If this is not too old, copy the image.
        if(daydifference.days <= maxdays):
            name = os.path.basename(file)
            filepath = imagespath + "\\" + file
            folderprefix = ""    
            
            #Decide if the image is a desktop or mobile image
            image = Image.open(filepath)
            if(IsDesktop(image.width, image.height)):
                folderprefix = "Desktop\\"
            else:
                folderprefix = "Mobile\\"

            shutil.copyfile(filepath, ourpath + "\\" + folderprefix + name + ".jpg")
        else:
            continue

#Checks if this image is for the desktop or mobile
def IsDesktop(width, height):
    return width > height

#Create subfolders incase they do not exist.
def CreateDirs(topfolder):
    if(os.path.exists(topfolder + "\\Desktop") != True):
        os.mkdir(topfolder + "\\Desktop")

    if(os.path.exists(topfolder + "\\Mobile") != True):
        os.mkdir(topfolder + "\\Mobile")

# Begin getting images
GetImages()