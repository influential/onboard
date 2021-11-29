#!/usr/bin/python3

import os, sys, shutil
from pathlib import Path

# Copies all of the files inside of the DCIM/###_PANA directory into the specified RAW folder path
def copyInputToRAW(targetPath):
    # Set up DCIM path
    dcimDirectory = os.path.join(inputDrivePath, "DCIM")
    print(dcimDirectory)
    print()

    # Iterate through each data folder inside of DCIM
    dcimFolders = os.listdir(dcimDirectory)
    for folder in dcimFolders:
        # print(folder)
        dataFolderPath = os.path.join(dcimDirectory, folder)
        print(dataFolderPath)
        
        dataFiles = os.listdir(os.path.join(dcimDirectory, folder))
        
        # Copy everything from the input drive into the RAW directory
        for file in dataFiles:
            print(file)
            datFilePath = os.path.join(dataFolderPath, file)
            shutil.copy(datFilePath, targetPath)
        print()
    
        print("Successfully copied data!")
        print(f"{dataFolderPath} --> {targetPath}")


saveDrivePath = '/mnt/i/testingDirVal'
inputDrivePath = '/mnt/e/testingDirOdin'

print(saveDrivePath)
print(inputDrivePath)
print()

saveDriveFiles = os.listdir(saveDrivePath)
inputDriveFiles = os.listdir(inputDrivePath)

print(f"Save Drive Files:")
for file in saveDriveFiles:
    print(file)

print()

print(f"Input Drive Files:")
for file in inputDriveFiles:
    print(file)

print()
print()



# Determine if the session is for a CONCERT or MUSIC VIDEO
while True:
    contentType = int(input("Which option?:\nConcert (1)\nMusic Video (2)\n"))

    if contentType == 1 or contentType == 2:
        break
    else:
        print("\nInvalid Choice - please enter 1 or 2")


# CONCERT
if contentType == 1:

    concertName = str(input("\nConcert Title:\n"))

    print("Concert")
    
    # Determine path of LiveShows and 
    liveShowsDirPath = os.path.join(saveDrivePath, "LiveShows")

    # Append new project directory to LiveShows path
    newProjectDirPath = os.path.join(liveShowsDirPath, concertName)

    print(liveShowsDirPath)
    print(newProjectDirPath)

    # Create new project folder based on concert name
    os.mkdir(newProjectDirPath)

    # Create RAW folder inside of project directory
    rawDirectory = os.path.join(newProjectDirPath, "RAW")
    os.mkdir(rawDirectory)

    print(rawDirectory)

    # Copy data from input drive into RAW directory
    copyInputToRAW(rawDirectory)

    # Seperate the .MOV files from .JPG and .RW2


# MUSIC VIDEO
elif contentType == 2:
    print("Music Video")





else:
    print("Error - Invalid Content Type")


print()
print("Done")