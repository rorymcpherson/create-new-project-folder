#! python3
# create_new_project_folder_gui.py

"""
Create New Project Folder GUI
Author: Rory McPherson | https://github.com/rorymcpherson

This script creates a GUI for creating a new project folder structure with subfolders for better organising and managing projects.

User Notes: Modify the subfolders as you like.

"""

import os
import PySimpleGUI as sg
from datetime import date

def create_project_layout():
    return [
        [sg.Text("Create New Project Folders", font=('Helvetica', 16), justification='center')],
        [sg.Text("Author: Rory McPherson | https://github.com/rorymcpherson", font=('Helvetica', 10))],
        [sg.Text("\nThis tool is for creating a new project folder for work projects.\nEnter the project details, designate a folder location, select a\nlocation for the folder, and the new project folder will be created.\nModify the subfolders list as you like in the Python script.", font=('Helvetica', 12))],
        [sg.Text("\nProject Details:", font=('Helvetica', 14))],
        [sg.Text("Project ID Number:", size=(14, 1)), sg.InputText(key="project_num", size=(32, 1))],
        [sg.Text("Project Name:", size=(14, 1)), sg.InputText(key="project_name", size=(32, 1))],
        [sg.Text("Client:", size=(14, 1)), sg.InputText(key="client_name", size=(32, 1))],
        [sg.Text("Default Location:"), sg.InputText(key="default_location", size=(30, 1), disabled=True), sg.FolderBrowse("Browse", target="default_location")],
        [sg.Text("\nSelect Main Folders to Create:", font=('Helvetica', 14))],
        [sg.Checkbox(main_folder, key=f"main_folder_{i}", default=False) for i, main_folder in enumerate(main_folders)],
        [sg.Text()],
        [sg.Button("Create Project", button_color=('#000', '#87CEEB')), sg.Button("Exit", button_color=('#000', '#87CEEB'))]
    ]

def create_project_window():
    sg.theme("Default1")
    layout = create_project_layout()
    return sg.Window("Create Project", layout, finalize=True)

def create_project():
    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Exit":
            break
        elif event == "Create Project":
            project_num = values["project_num"]
            project_name = values["project_name"]
            client_name = values["client_name"]
            default_location = values["default_location"]

            # Create project directory
            year = str(date.today().year)
            project_dir = os.path.join(default_location, f"{project_num} - {project_name} ({client_name} {year})")

            # Create selected main folders and their associated subfolders
            selected_main_folders = [main_folder for i, main_folder in enumerate(main_folders) if values[f"main_folder_{i}"]]
            for main_folder in selected_main_folders:
                main_folder_path = os.path.join(project_dir, main_folder)
                if not os.path.exists(main_folder_path):
                    os.makedirs(main_folder_path)
                    for subfolder in subfolder_mapping.get(main_folder, []):
                        subfolder_path = os.path.join(main_folder_path, subfolder)
                        os.makedirs(subfolder_path)
                else:
                    sg.popup_error(f"Directory already exists: {main_folder_path}")

            # Open new project folder
            try:
                os.startfile(project_dir)
            except Exception as e:
                sg.popup_error(f"Error opening project folder: {e}")

def main():
    global window
    window = create_project_window()
    create_project()
    window.close()

main_folders = [
    'ArcGIS',
    'Data',
    'Documents',
    'Images',
    'Scripts'
]

subfolder_mapping = {
    'ArcGIS': ['Maps', 'Layer Files'],
    'Data': ['Received', 'Sourced', 'New', 'FME'],
    'Images': ['Branding', 'Icons', 'Thumbnails']
}

if __name__ == "__main__":
    main()