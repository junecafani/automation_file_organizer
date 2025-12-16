import os
import math
from organizer.core import (
    check_file_not,
    check_size,
    convert_size,
    folder_info
)

folder_path = 'D:/LATIHAN_Python_Portofolio/portofolio/automation_file_organizer/tests/sample_files'
contents = os.listdir(folder_path)

for item in contents:
    full_path = os.path.join(folder_path, item)

    if check_file_not(full_path):
        size_bytes = check_size(full_path)
        size_readable = convert_size(size_bytes)
        print(f'[FILE] {item} || {size_readable}')

    else:
        folders, files = folder_info(full_path)
        print(f'[FOLDER] {item} || {folders} folders || {files} files')