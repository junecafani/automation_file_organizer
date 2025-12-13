import os
import math

folder_path = 'D:/LATIHAN_Python_Portofolio/portofolio/automation_file_organizer/tests/sample_files'
contents = os.listdir(folder_path)

# New Variable Definition
## Convert bytes from stats.st_size to different size
def convert_size(sizes_bytes):
    if sizes_bytes == 0 :
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(sizes_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(sizes_bytes / p, 2)
    return "%s %s" % (s, size_name[i])

print(f'Contents of {folder_path} : ')
for item in contents:
    full_path = os.path.join(folder_path, item)

    # check file or not
    if os.path.isfile(full_path):
        stats = os.stat(full_path)
        print(item,'||', convert_size(stats.st_size)) 
    else:
        print(item, '|| This is Folder')


# print(type(item))
# # ukuran file
# stats = os.stat('')



# ekstensi


