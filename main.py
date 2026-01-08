import os
import shutil
from pathlib import Path
from Features.category import categorise
from Features.duplication import duplication_Handle
dir = str(Path.home()/"Desktop"/"Test")
        
for file in os.listdir(dir):
    complete_path = os.path.join(dir, file)
    if os.path.isfile(complete_path):
        category = categorise(file)
        categoryFolder = os.path.join(dir,category)
        os.makedirs(categoryFolder, exist_ok=True)
        shutil.move(complete_path, os.path.join(categoryFolder, file))

        print("Duplicate detection :")
        duplication_Handle(dir)
        print("Duplicate detection complete :")

print("Successful Categorisation.")

