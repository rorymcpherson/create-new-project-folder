#! python3
# create-new-project-folder.py

"""
Create New Project Folder
Author: Rory McPherson | https://github.com/rorymcpherson

This script creates a new project folder structure with subfolders for better organising and managing projects.

User Notes: Modify the subfolders as you like.

"""

import os
from datetime import date

def createProject():
    print(
        'This script creates a new project folder for work projects. Enter the project details, designate a folder location, and the new project folder will be created.\n\n')
    print('Step 1/2: Enter project details:')

    projectNum = str(input('Project ID Number: '))
    projectName = str(input('Project Name: '))
    clientName = str(input('Client: '))

    year = str(date.today().year)

    # set project directory location
    projectDir = ''
    while projectDir == '':
        defaultDir = os.path.expanduser("~")
        changeDir = str(input(
            f'The default location for projects is set to {defaultDir}\nStep 2/2: Enter "y" to use this location, or "n" to set a new location: '))
        if changeDir.lower() == "y":
            projectDir = defaultDir
        elif changeDir.lower() == "n":
            newProjectDir = str(input('Enter new path location: '))
            while not os.path.isdir(newProjectDir):
                print("Invalid path. Please enter a valid directory.")
                newProjectDir = str(input('Enter new path location: '))
            projectDir = newProjectDir

    # create project directory
    newProject = os.path.join(projectDir, f"{projectNum} - {projectName} ({clientName} {year})")

    # create project subdirectories
    subdirectories = [
        'ArcGIS',
        'ArcGIS/Maps',
        'ArcGIS/Layer Files',
        'Data',
        'Data/Received',
        'Data/Sourced',
        'Data/New',
        'Data/FME',
        'Documents',
        'Communications',
        'Images',
        'Images/Branding',
        'Images/Icons',
        'Images/Thumbnails',
        'Scripts'
    ]

    for subdir in subdirectories:
        subdir_path = os.path.join(newProject, subdir)
        if not os.path.exists(subdir_path):
            os.makedirs(subdir_path)
        else:
            print(f"Directory already exists: {subdir_path}")

    # open new project folder
    try:
        os.startfile(newProject)
    except Exception as e:
        print(f"Error opening project folder: {e}")


# call functions
createProject()