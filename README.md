# Create New Project File

This repository provides Python scripts for creating project folders with predefined subfolders, designed to better organize and manage projects. Using these tools, you can easily setup working project directory structures automatically. Two scripts have been created: one you can run from a command line, and the other using a GUI. An executable file has been added to allow

## Command Line Script

The `create_new_project_file.py` script is a command line interface tool for creating new project folders. It prompts the user to enter project details and choose a location for the new project folder. It then creates the specified folder structure.

## GUI Script

The `create_new_project_file_gui.py` script provides a graphical user interface (GUI) using PySimpleGUI. It allows users to interactively enter project details, choose a location for the new project folder, and select main folders to create. This script can easily create project folders with a more user-friendly experience.

### Requirements
Before using the GUI script, ensure you have PySimpleGUI installed. You can install it via pip.

`pip install PySimpleGUI`

For more information see the [PySimpleGUI Documentation](https://docs.pysimplegui.com/en/latest/).

## GUI Executable

The `create_new_project_file_gui.exe` allows any user to run the packaged GUI script from a standalone executable file, and without installing Python. This was created using PyInstaller. For more information see [PyInstaller](https://pyinstaller.org/en/stable/).

### How to create a new .exe package

To create a new .exe file from a modification of `create_new_python_file_gui.py`, ensure you have PyInstaller installed. You can install it via pip.

`pip install pyinstaller`

After you have modified the GUI Script, navigate to the directory containing the Python file and using a command line interface run: `pyinstaller --onefile --noconsole create_new_project_file_gui.py`. Please note that you will need to update the name of the Python file in the command prompt if you have renamed it.