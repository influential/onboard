#!/usr/bin/python3

import os, sys, shutil
from pathlib import Path


#    ____        _                         _ 
#   / __ \      | |                       | |
#  | |  | |_ __ | |__   ___   __ _ _ __ __| |
#  | |  | | '_ \| '_ \ / _ \ / _` | '__/ _` |
#  | |__| | | | | |_) | (_) | (_| | | | (_| |
#   \____/|_| |_|_.__/ \___/ \__,_|_|  \__,_|


def welcome():
    print("===================================================")
    print("    ____        _                         _ ")                                
    print("   / __ \      | |                       | |")                                
    print("  | |  | |_ __ | |__   ___   __ _ _ __ __| |")                                
    print("  | |  | | '_ \| '_ \ / _ \ / _` | '__/ _` |")                                
    print("  | |__| | | | | |_) | (_) | (_| | | | (_| |")                                
    print("   \____/|_| |_|_.__/ \___/ \__,_|_|  \__,_|")                                
    print()
    print("===================================================")





# Determine if the session is for a CONCERT or MUSIC VIDEO
def getContentType():
    while True:
        contentType = int(input("Which option?:\n(1) Concert\n(2) Music Video\n(3) Exit program\n"))

        if contentType == 1 or contentType == 2 or contentType == 3:
            return contentType
        else:
            print("\nInvalid Choice - please enter 1, 2, or 3")


def displayDebugInfo(saveDrivePath, inputDrivePath):
    print(f"Drive we are saving to:\n   {saveDrivePath}")
    print()
    print(f"Drive we are pulling from:\n    {inputDrivePath}")
    print()

    saveDriveFiles = os.listdir(saveDrivePath)
    dcimDirPath = os.path.join(inputDrivePath, "DCIM")
    inputDriveFolders = os.listdir(dcimDirPath)

    print(f"Save Drive Folders:")
    for file in saveDriveFiles:
        print(f"    {file}")

    print()

    print(f"Input Drive Folders:")
    for folder in inputDriveFolders:
        # print(file)
        # print(folder)
        dataFolderPath = os.path.join(dcimDirPath, folder)
        print(dataFolderPath)
        
        dataFiles = os.listdir(os.path.join(dcimDirPath, folder))
        
        # Copy everything from the input drive into the RAW directory
        for file in dataFiles:
            print(f"    {file}")
            # dataFilePath = os.path.join(dataFolderPath, file)

    print()
    print("===================================================")
    print()
    print()


# Builds a RAW directory at the target path
def buildRAW(target):
    # Create the raw directory that stores all of the input data
    try:
        rawDirPath = os.path.join(target, "RAW")
        os.mkdir(rawDirPath)
    except:
        print(f"Error making 'RAW' folter at {rawDirPath}")
    
    return rawDirPath

# Builds all of the necessary folders per Z's specification
def buildConcertDirs(concertAbsPath):
    # Dictionary of paths
    paths = {}

    # Get the path to the RAW directory 
    rawDirPath = buildRAW(concertAbsPath)
    paths['raw'] = rawDirPath

    # Create a photos directory inside of RAW
    try:
        photosDirPath = os.path.join(rawDirPath, "photos")
        os.mkdir(photosDirPath)
    except:
        print(f"Error making 'photos' folder at {photosDirPath}")
        print("Exiting...")
        quit()
    paths["photos"] = photosDirPath

    try:
        footageDirPath = os.path.join(rawDirPath, "footage")
        os.mkdir(footageDirPath)
    except:
        print(f"Error making 'footage' folder at {footageDirPath}")
        print("Exiting...")
        quit()
    paths["footage"] = footageDirPath

    try:
        toEditDirPath = os.path.join(photosDirPath, "To Edit")
        os.mkdir(toEditDirPath)
    except:
        print(f"Error making 'To Edit' folder at {toEditDirPath}")
        print("Exiting...")
        quit()
    paths["toEdit"] = toEditDirPath
    return paths

# Copies all of the files inside of the DCIM/###_PANA directory into the specified RAW folder path
# TODO: NEED TO CHECK THAT FILES ARE NOT FROM OLD IMPORT BASED ON DATE <-- Get INPUT

def copyInputToRAW(paths, inputPath):
    # Set up DCIM path
    dcimDirectory = os.path.join(inputPath, "DCIM")
    # print(dcimDirectory)
    print()

    # Iterate through each data folder inside of DCIM
    dcimFolders = os.listdir(dcimDirectory)
    for folder in dcimFolders:
        # print(folder)
        dataFolderPath = os.path.join(dcimDirectory, folder)
        # print(dataFolderPath)
        
        dataFiles = os.listdir(os.path.join(dcimDirectory, folder))
        
        # Copy everything from the input drive into the appropriate directory
        for file in dataFiles:
            try:
                extension = file.split('.')[1]
            except:
                print(f"Error getting extension of file {file}")
                print("Exiting...")
                quit()    
           
            print(extension)
             
            if extension == 'mov' or extension == 'MOV':
                copyToTargetPath(paths['footage'], dataFolderPath, file)
            elif extension == 'jpg' or extension == 'JPG' or extension == 'jpeg' or extension == 'JPEG' or extension == 'rw2' or extension == 'RW2':
                copyToTargetPath(paths['photos'], dataFolderPath, file)
            elif extension == "txt" or extension == 'TXT':
                copyToTargetPath(paths['photos'], dataFolderPath, file)
            else:
                print(f"Invalid file type found {extension}")
                print("Exiting...")
                quit()
            
            
        # print()
    
        

# Copy the input file to the specified target path
def copyToTargetPath(targetPath, inputFolderPath, file):
    inputFilePath = os.path.join(inputFolderPath, file)
    shutil.copy(inputFilePath, targetPath) 
    print("Success!")
    print(f"{inputFilePath} --> {targetPath}")


# Handles all of the logic for concert sessions
def concert(savePath, inputPath):
    concertName = str(input("\nEnter concert title:\n"))

    liveShowsDirPath = os.path.join(savePath, "LiveShows")  # Determine path of LiveShows folder
  
    # print(liveShowsDirPath)
    # print(newProjectDirPath)

    # Create new project folder based on concert name
    try:
        newProjectDirPath = os.path.join(liveShowsDirPath, concertName)  # Append new project directory to LiveShows path
        os.mkdir(newProjectDirPath)
    
    # If the concert somehow already exists, throw an error and exit gracefully
    except FileExistsError:
        print(f"Found previous artist folder {newProjectDirPath}")
        print("Exiting...")
        quit()
    
    # Create all of the necessary sub-directories inside of the concert folder
    pathsDict = buildConcertDirs(newProjectDirPath)

    # Copy data from input drive into RAW directory
    copyInputToRAW(pathsDict, inputPath)


def musicVid(savePath, inputPath):
    artistName = str(input("Enter artist name:\n"))
    songName = str(input("Enter song name:\n"))

    artistsDirPath = os.path.join(savePath, "Artists")  # Determine path of Artists folder
    newArtistDirPath = os.path.join(artistsDirPath, artistName)  # Append new project directory to Artists path
    
    # Try to create a new folder using artist name
    try:
        os.mkdir(newArtistDirPath)
        print(f"Successfully created artist folder {newArtistDirPath}")
    
    # If the file already exists its okay, handle the error graciously and continue
    except FileExistsError:
        print(f"Found previous artist folder {newArtistDirPath}")

    # print(newArtistDirPath)

    # Create a new project folder inside of the artist's folder
    newProjectDirPath = os.path.join(newArtistDirPath, songName)
    
    # Try to create new folder for the song
    try:
        os.mkdir(newProjectDirPath)
        # print(newProjectDirPath)
        print(f"Successfully created song folder {newProjectDirPath}")

    # If the song already has a folder, throw an error. Can handle this if we need to later
    except FileExistsError:
        print(f"Error - This song folder already exists {newProjectDirPath}")
        print("Exiting...")
        quit()

    # Create the raw directory that stores all of the input data
    rawDirectory = buildRAW(newProjectDirPath)

    # Copy data from input drive into RAW directory
    copyInputToRAW(rawDirectory, inputPath)


def main():
    # Replace these with environment variables, which will depend on the system it is running on
    saveDrivePath = '/mnt/i/testingDirVal'
    inputDrivePath = '/mnt/e/testingDirOdin'

    windowsSaveDrivePath = "I:\testingDirVal"
    windowsInputDrivePath = "E:\testingDirOdin"

    welcome()

    displayDebugInfo(saveDrivePath, inputDrivePath)
    mode = getContentType()

    if mode == 1:  # CONCERT
        concert(saveDrivePath, inputDrivePath)
        # concert(windowsSaveDrivePath, windowsInputDrivePath)
    elif mode == 2: # MUSIC VIDEO
        musicVid(saveDrivePath, inputDrivePath)
        # musicVid(windowsSaveDrivePath, windowsInputDrivePath)
    elif mode == 3:
        return
    else:
        print("Error - Invalid Content Type")

    print()
    print("Done")

if __name__ == "__main__":
    main()