import os
import math

folder_path = 'D:/LATIHAN_Python_Portofolio/portofolio/automation_file_organizer/tests/sample_files'
contents = os.listdir(folder_path)

# New Function
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

print(f'Contents of {folder_path} : ')
for item in contents:
    full_path = os.path.join(folder_path, item)

    # check file or not
    if os.path.isfile(full_path):
        stats = os.stat(full_path)
        print('[FILE]', item,'|| ', convert_size(stats.st_size))
    else:
        folders, files = folder_info(full_path)
        print(f'[FOLDER] {item} || {folders} folders || {files} files')
