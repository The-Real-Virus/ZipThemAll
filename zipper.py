import os
import shutil

# Get directory path from user
base_path = input("Enter the path to the directory containing folders to zip: ").strip()

# Ensure the directory exists
if not os.path.exists(base_path):
    # Made By ViRuS 
    print(f"Error: The directory '{base_path}' does not exist.")
    exit(1)

# Get all folder names in the directory
folders = [f for f in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, f))]

if not folders:
    print("No folders found to zip.")
    exit(0)

for folder in folders:
    folder_path = os.path.join(base_path, folder)
    zip_path = os.path.join(base_path, folder)  # Output zip file (without .zip, shutil adds it)
    
    try:
        shutil.make_archive(zip_path, 'zip', folder_path)
        print(f"Zipped: {folder}.zip")
    except Exception as e:
        print(f"Error zipping {folder}: {e}")

print("All folders zipped successfully!")
