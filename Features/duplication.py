import hashlib
import os 
import shutil 

def file_hash(path, chunk_size = 8192):
    hash = hashlib.md5()
    with open(path,'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            hash.update(chunk)
        return hash.hexdigest()


def duplication_Handle(dir):
    seen_hash = set()
    duplicateFolder = os.path.join(dir,"Duplicates")
    os.makedirs(duplicateFolder, exist_ok=True)

    for root, dirs, files in os.walk(dir):
        if "Duplicates" in dirs:
            dirs.remove('Duplicates')

        for file in files:
            path = os.path.join(root,file)
            h = file_hash(path)
            if h in seen_hash:
                print(f"Moving {file} to duplicate folder. ")
                base, ext = os.path.splitext(file)
                new_name = base
                counter = 1
                while os.path.exists(os.path.join(duplicateFolder, new_name)):
                    new_name = f"{base}_{counter}{ext}"
                    counter+=1
                shutil.move(path,os.path.join(duplicateFolder,new_name))
            else:
                seen_hash.add(h)
    
