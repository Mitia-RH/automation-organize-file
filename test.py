import os
import numpy as np
import warnings


# Suppress the warning
warnings.filterwarnings("ignore", message="elementwise comparison failed; returning scalar instead, but in the future will perform elementwise comparison")

path = os.path.expanduser("~/Downloads")
file_list = np.array(os.listdir(path))


for f in file_list:
    ext = f.split(".")[-1]

    try:
        if len(ext[0]) > 0:
            path_to_mkdir = os.path.expanduser(f"~/Downloads/{ext}")
            os.mkdir(path_to_mkdir)
            new_file_path = os.path.join(os.path.join(path, ext), f)
            os.rename(os.path.join(path, f), new_file_path)

    except FileExistsError:
        new_file_path = os.path.join(os.path.join(path, ext), f)
        os.rename(os.path.join(path, f), new_file_path)
    
    


#reset warning filter
warnings.resetwarnings()