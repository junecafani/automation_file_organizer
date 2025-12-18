import argparse
import os
import math
from organizer.core import (
    check_file_not,
    check_size,
    convert_size,
    folder_info
)

parser = argparse.ArgumentParser(description="Automation File Organizer")

parser.add_argument(
    "--path",
    required=True,
    help="Target folder path to scan"
)

parser.add_argument(
    "--mode",
    default="scan",
    choices=["scan"],
    help="Operation mode"
)

args = parser.parse_args()

if args.mode != "scan":
    print("Mode not supported")
    exit(1)

folder_path = args.path
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