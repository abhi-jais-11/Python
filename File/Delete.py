import os 
from glob import glob
folder_path = './'
file_pattern = '*.txt'  

files_to_delete = glob(os.path.join(folder_path, file_pattern))


for file_path in files_to_delete:
    try:
        os.remove(file_path)
        print(f"Deleted: {file_path}")
    except Exception as e:
        print(f"Error deleting {file_path}: {e}")