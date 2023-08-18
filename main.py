import os
import shutil

# Defining the path to my downloads folder
try:
    downloads_path = "/c/Users/jackt/Downloads"
except:
    print("Invalid file path, please try again")

# Create a dictionary with file extensions as keys and corresponding folder names as values
file_extension_folders = {
    ".pdf": "PDFs",
    ".docx": "Documents",
    ".jpg": "Images",
    ".png": "Images",
    ".heic": "Images",
    ".mp3": "Music",
    ".mp4": "Videos",
    ".zip": "Archives",
    ".exe": "Executables",
    ".txt": "TextFiles",
    ".zip": "Compressed Folders",
    ".ics": "Calendar",
}

# Create subdirectories
for folder_name in file_extension_folders.values():
    folder_path = os.path.join(downloads_path, folder_name)
    os.makedirs(folder_path, exist_ok=True)

# Loop through files in Downloads folder
for filename in os.listdir(downloads_path):
    file_path = os.path.join(downloads_paht, filename)

    # Skip directories
    if os.path.isdir(file_path):
        continue

    # Get file extension
    file_extension = os.path.splittext(filename)[1]

    # Determine destination folder
    destination_folder = file_extension_folders.get(file_extension.lower(), "Other")

    # Move the file to the appropriate folder
    new_path = os.path.join(downloads_path, destination_folder, filename)
    shutil.move(file_path, new_path)

print("Files successfully sorted.")
