import os
import math

# New Function
## File or folder
def check_file_not(check_path):
    return os.path.isfile(check_path)

## Grab file size
def check_size(size_a_file):
    this_size = os.stat(size_a_file)
    return this_size.st_size

## Convert size from bytes to another
def convert_size(sizes_bytes):
    if sizes_bytes == 0 :
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(sizes_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(sizes_bytes / p, 2)
    return "%s %s" % (s, size_name[i])

## Check sum of files inside folder
def folder_info(path):
    total_folders = 0
    total_files = 0

    for root, dirs, files in os.walk(path):
        total_folders += len(dirs)
        total_files += len(files)

    return total_folders, total_files

## Rename files
def preview_rename(path):
    items = os.listdir(path)

    for i, name in enumerate(items, start=1):
        full_path = os.path.join(path, name)

        if not os.path.isfile(full_path):
            continue

        root, ext = os.path.splitext(name)
        new_name = f"secretary-kim_{i}{ext}"

        print(f"[DRY-RUN] {name} -> {new_name}")

def apply_rename(path):
    items = os.listdir(path)
    index = 1

    for name in items:
        full_path = os.path.join(path, name)

        if not os.path.isfile(full_path):
            continue

        root, ext = os.path.splitext(name)
        new_name = f"secretary-kim_{index}{ext}"
        new_path = os.path.join(path, new_name)

        os.rename(full_path, new_path)
        index += 1
