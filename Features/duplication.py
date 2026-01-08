import hashlib
import os 
import shutil 
from collections import defaultdict

def file_hash(path, chunk_size = 8192):
    hashMD5 = hashlib.md5()
    with open(path,'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            hashMD5.update(chunk)
        return hashMD5.hexdigest()


def duplication_Handle(dir):
    
    duplicateFolder = os.path.join(dir,"Duplicates")
    os.makedirs(duplicateFolder, exist_ok=True)

    size_map = defaultdict(list)
    for root, dirs, files in os.walk(dir):
        if "Duplicates" in dirs:
            dirs.remove('Duplicates')

        for file in files:
            path = os.path.join(root,file)
            size = os.path.getsize(path)
            size_map[size].append(path)

    for size, paths in size_map.items():
            if len(paths)<2:
                continue
            
            seen_hash = {}

            for path in paths:
                h = file_hash(path)
                file_name = os.path.basename(path)

                if h in seen_hash:
                    print(f"Moving {file_name} to duplicate folder. ")
                    base, ext = os.path.splitext(file_name)
                    new_name = file_name
                    counter = 1
                    while os.path.exists(os.path.join(duplicateFolder, new_name)):
                        new_name = f"{base}_{counter}{ext}"
                        counter+=1
                    shutil.move(path,os.path.join(duplicateFolder,new_name))
                else:
                    seen_hash[h]=path
    
