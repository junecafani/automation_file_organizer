# modul yang diperlukan

# reader
import os

folder_path = 'C:/Users/Cafani/Downloads'
contents = os.listdir(folder_path)

print(f'Contents of {folder_path} : ')
for item in contents:
    full_path = os.path.join(folder_path, item)

    stats = os.stat(full_path)
    print(item,'||', stats.st_size, 'bytes') # ini bisa diubah ke mb nantinya

# print(type(item))
# # ukuran file
# stats = os.stat('')



# ekstensi
