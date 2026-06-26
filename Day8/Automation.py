import os
import shutil

# Folder to organize
folder = r"C:\Users\User\Downloads"

# File categories
file_types = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",

    ".pdf": "PDFs",

    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",

    ".mp3": "Music",

    ".mp4": "Videos",
    ".mkv": "Videos",

    ".xlsx": "Spreadsheets",
    ".xls": "Spreadsheets",

    ".py": "Python Files"
}

# Read everything in the folder
for file in os.listdir(folder):

    file_path = os.path.join(folder, file)

    # Skip folders
    if os.path.isdir(file_path):
        continue

    # Get file extension
    extension = os.path.splitext(file)[1].lower()

    # Determine destination folder
    destination_folder = file_types.get(extension, "Others")

    destination_path = os.path.join(folder, destination_folder)

    # Create folder if it doesn't exist
    os.makedirs(destination_path, exist_ok=True)

    # Move file
    shutil.move(file_path, os.path.join(destination_path, file))

    print(f"Moved: {file} → {destination_folder}")

print("\nOrganization Complete!")