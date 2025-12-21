import argparse
import os

from organizer.core import (
    check_file_not,
    check_size,
    convert_size,
    folder_info,
    preview_rename,
    apply_rename
)

parser = argparse.ArgumentParser(
    description="Automation File Organizer"
)

parser.add_argument(
    "--path",
    required=True,
    help="Target folder path"
)

parser.add_argument(
    "--mode",
    default="scan",
    choices=["scan", "rename"],
    help="Operation mode"
)

parser.add_argument(
    "--dry-run",
    action="store_true",
    help="Simulate rename only (no changes)"
)

parser.add_argument(
    "--confirm",
    action="store_true",
    help="Apply rename changes"
)

args = parser.parse_args()
folder_path = args.path

if not os.path.exists(folder_path):
    print(f"[ERROR] Path not found: {folder_path}")
    exit(1)

if not os.path.isdir(folder_path):
    print(f"[ERROR] Path is not a folder: {folder_path}")
    exit(1)

if args.mode == "scan":
    contents = os.listdir(folder_path)

    if not contents:
        print("[INFO] Folder is empty.")
        exit(0)

    for item in contents:
        full_path = os.path.join(folder_path, item)

        if check_file_not(full_path):
            size_bytes = check_size(full_path)
            size_readable = convert_size(size_bytes)
            print(f"[FILE] {item} || {size_readable}")
        else:
            folders, files = folder_info(full_path)
            print(f"[FOLDER] {item} || {folders} folders || {files} files")

    exit(0)

elif args.mode == "rename":

    if args.dry_run:
        print("[INFO] Dry-run mode enabled (no changes will be made)")
        preview_rename(folder_path)
        exit(0)

    if args.confirm:
        print("[INFO] Confirm mode enabled (files WILL be renamed)")
        apply_rename(folder_path)
        print("[OK] Rename applied")
        exit(0)

    print("[ERROR] Rename mode requires --dry-run or --confirm")
    exit(1)

else:
    print("[ERROR] Unsupported mode")
    exit(1)