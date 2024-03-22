import os
import warnings

# Suppress the warning
warnings.filterwarnings("ignore", message="elementwise comparison failed; returning scalar instead, but in the future will perform elementwise comparison")

path = os.path.expanduser("~/Downloads")
file_list = os.listdir(path)

for f in file_list:
    full_path = os.path.join(path, f)
    
    if os.path.isfile(full_path):
        ext = f.split(".")[-1]

        if ext:  
            path_to_mkdir = os.path.join(path, ext) 
            os.makedirs(path_to_mkdir, exist_ok=True)
            new_file_path = os.path.join(path_to_mkdir, f)
            os.rename(full_path, new_file_path)

# Reset warning filter
warnings.resetwarnings()



