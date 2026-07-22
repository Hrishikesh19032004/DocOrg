import os
import shutil
from pathlib import Path
from Features.category import categorise
from Features.duplication import duplication_Handle
from Features.logger import log_move, log_duplicate, log_error
from Features.snapshot import SnapshotManager

snapshot = SnapshotManager()
dir = str(Path.home()/"Desktop"/"Test")

print("Duplicate detection :")
duplication_Handle(dir, snapshot)
print("Duplicate detection complete :")

for file in os.listdir(dir):
    complete_path = os.path.join(dir, file)
    
    if os.path.isfile(complete_path):
        try:
            category = categorise(file)
            categoryFolder = os.path.join(dir,category)
            os.makedirs(categoryFolder, exist_ok=True)

            destination_path = os.path.join(categoryFolder, file)
            shutil.move(complete_path, destination_path)

            snapshot.add_operation(
                source=complete_path,
                destination=destination_path,
                operation_type="category"
            )
            
            log_move(file, complete_path, destination_path, category)
            print(f"{file} -> {category}")

        except Exception as e:
            log_error(file, complete_path, e)
            print(f"Error moving {file}: {e}")
if snapshot.operations:
    snapshot.save()

print("Successful Categorisation.")

