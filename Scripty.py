import os
import tempfile
import shutil
import ctypes
import subprocess

def delete_temp_files():
    temp_folder = tempfile.gettempdir()

    for root, dirs, files in os.walk(temp_folder):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                os.remove(file_path)
                print(f"Deleted file: {file_path}")
            except Exception as e:
                print(f"Failed to delete file: {file_path}, Error: {e}")

        for dir in dirs:
            dir_path = os.path.join(root, dir)
            try:
                shutil.rmtree(dir_path)
                print(f"Deleted folder: {dir_path}")
            except Exception as e:
                print(f"Failed to delete folder: {dir_path}, Error: {e}")

def delete_downloads_files():
    downloads_folder = os.path.expanduser("~/Downloads")

    for root, dirs, files in os.walk(downloads_folder):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                os.remove(file_path)
                print(f"Deleted file: {file_path}")
            except Exception as e:
                print(f"Failed to delete file: {file_path}, Error: {e}")

        for dir in dirs:
            dir_path = os.path.join(root, dir)
            try:
                shutil.rmtree(dir_path)
                print(f"Deleted folder: {dir_path}")
            except Exception as e:
                print(f"Failed to delete folder: {dir_path}, Error: {e}")
                
def delete_empty_folders(root_folder):
    empty_folders_count = 0

    for root, dirs, files in os.walk(root_folder, topdown=False):
        for dir in dirs:
            folder_path = os.path.join(root, dir)
            try:
                if not os.listdir(folder_path):  # Check if folder is empty
                    os.rmdir(folder_path)  # Remove the empty folder
                    empty_folders_count += 1
                    print(f"Deleted empty folder: {folder_path}")
            except Exception as e:
                print(f"Failed to delete folder: {folder_path}, Error: {e}")

    return empty_folders_count

# Specify the root folder to start searching for empty folders
root_folder = "C:/"

delete_temp_files()
delete_downloads_files()
try:
    total_empty_folders = delete_empty_folders(root_folder)
    print(f"Total empty folders removed: {total_empty_folders}")
except Exception as e:
    print(f"An error occurred: {e}")

def empty_recycle_bin():
    SHEmptyRecycleBin = ctypes.windll.shell32.SHEmptyRecycleBinW
    SHEmptyRecycleBin(None, None, 1)
    print("Recycle bin emptied successfully.")

# Empty the recycle bin
empty_recycle_bin()

def stop_and_disable_wsearch_service():
    # Stop the WSearch service
    subprocess.run(['sc', 'stop', 'WSearch'], capture_output=True, text=True, check=True)

    # Disable the WSearch service
    subprocess.run(['sc', 'config', 'WSearch', 'start=', 'disabled'], capture_output=True, text=True, check=True)

    print("WSearch service stopped and disabled successfully.")

# Stop and disable the WSearch service
stop_and_disable_wsearch_service()
