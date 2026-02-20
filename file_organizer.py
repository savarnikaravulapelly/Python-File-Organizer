import os
import shutil

# Path of folder to organize
folder_path = "test_folder"   # Change this to your folder path

# File type folders
file_types = {
    "Images": [".jpg", ".png", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Music": [".mp3"],
    "Archives": [".zip", ".rar"]
}

# Create folders if not exist
for folder in file_types.keys():
    os.makedirs(os.path.join(folder_path, folder), exist_ok=True)

# Move files
for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):
        for folder, extensions in file_types.items():
            if file.lower().endswith(tuple(extensions)):
                shutil.move(file_path, os.path.join(folder_path, folder, file))
                break

print("Files organized successfully!")
