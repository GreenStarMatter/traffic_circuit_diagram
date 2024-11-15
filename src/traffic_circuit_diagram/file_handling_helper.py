import tkinter as tk
from tkinter import filedialog


def open_file_picker(file_type  = "txt"):
    # Initialize Tkinter root
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Open file picker dialog
    if file_type  == "excel":
        file_path = filedialog.askopenfilename(
            title="Select an Excel File",
            filetypes=[("Excel Files", "*.xls*")]
        )
    elif file_type == "txt":
        file_path = filedialog.askopenfilename(
            title="Select an Excel File",
            filetypes=[("Text Files", "*.txt")]
        )
    else:
        print("Unrecognized file type")

    if file_path:
        print(f"Selected file: {file_path}")
    else:
        print("No file selected.")
    return file_path

def open_folder_picker():
    # Create the root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Open the folder picker dialog
    folder_selected = filedialog.askdirectory(title="Select a Folder")

    # Check if a folder was selected
    if folder_selected:
        print(f"Folder selected: {folder_selected}")
    else:
        print("No folder selected.")
    return folder_selected