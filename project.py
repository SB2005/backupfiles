import os
import shutil
import time

days = 30
path = "folderA"

seconds = time.time() - (days * 24 * 60 * 60)

def get_age(root_path):
    current_time = os.stat(root_path).st_ctime
    return current_time

def remove_folder(root_path):
    if not shutil.rmtree(root_path):
        print(root_path, " removed successfully")
    else:
        print("can't remove")

if (os.path.exists(path)):
    for root, folders, files in os.walk(path):
        print(root, folders, files)
        if seconds >= get_age(root):
            remove_folder(root)
            break
        else:
            for f in folders:
                f_path = os.path.join(root, f)
                if seconds >= get_age(f_path):
                    remove_folder(f_path)
                    break

            for f in files:
                f_path = os.path.join(root, f)
                if seconds >= get_age(f_path):
                    remove_folder(f_path)
                    break

            
        
else:
    print("Path not found")



