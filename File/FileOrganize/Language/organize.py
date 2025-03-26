import os
import shutil
import json
from pathlib import Path
import logging

def configure_log():
    """Configure logs for tracking file operations."""
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)
    logging.basicConfig(
        filename=os.path.join(log_dir, "file_organizer.log"),
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

def load_categories():
    """Load file categories from a JSON file."""
    try:
        with open("file_categories.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        logging.error("Error: file_categories.json not found.")
        return {}

def create_folders(directory, categories):
    """Create folders based on categories if they don't exist."""
    for folder in categories:
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            logging.info(f"Created folder: {folder_path}")

def organize_files(directory):
    """Organize files in the specified directory based on their extensions."""
    categories = load_categories()
    if not categories:
        print("No categories found. Please check file_categories.json.")
        return

    create_folders(directory, categories.keys())
    moved_files = 0

    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):  # Check if it's a file
            ext = Path(file).suffix.lower()
            moved = False

            for category, extensions in categories.items():
                if ext in extensions:
                    dest_folder = os.path.join(directory, category)
                    dest_path = os.path.join(dest_folder, file)
                    counter = 1

                    # Handle duplicate filenames
                    while os.path.exists(dest_path):
                        new_name = f"{Path(file).stem} ({counter}){ext}"
                        dest_path = os.path.join(dest_folder, new_name)
                        counter += 1

                    shutil.move(file_path, dest_path)
                    logging.info(f"Moved {file} to {dest_path}")
                    moved_files += 1
                    moved = True
                    break  # Stop checking once the file is moved

            if not moved:
                logging.info(f"No category for {file}, leaving in place.")

    print(f"Organized {moved_files} files.")

def main():
    """Main function to handle file organization."""
    configure_log()
    target_directory = input("Enter the directory to organize (Press Enter for current directory): ").strip()

    # Default to current working directory if input is empty
    if not target_directory:
        target_directory = os.getcwd()
        print(f"Using current working directory: {target_directory}")

    if os.path.exists(target_directory):
        organize_files(target_directory)
    else:
        print("Invalid directory. Please provide a valid path.")

if __name__ == "__main__":
    main()
