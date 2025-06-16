#Write a python program to print the contents of a directory using the os module.Search online for the function which does that.
#To print the contents of a directory using the os module in Python, you can use the os.listdir() function. This function returns a list of all files and folders in the specified path.

import os

path = r'D:\Learn\Python ChapterWise Notes'

# Get the list of files and directories
entries = os.listdir(path)

# Print the contents
print(f"Contents of '{path}':")
for entry in entries:
    print(entry)

#Key function to list directory contents
'''
entries = os.listdir('D:\\Learn\\Python ChapterWise Notes')
print(entries)
'''

#Improved version: only list files
'''files = [
    f
    for f in os.listdir(path)
    if os.path.isfile(os.path.join(path, f))
]
for f in files:
    print(f)'''


#Alternative: recursively list through subdirectories
'''for dirpath, dirnames, filenames in os.walk(path):
    print(f"Contents of {dirpath}:")
    for filename in filenames:
        print(filename)'''


#Bonus: os.scandir() for efficiency
'''with os.scandir(path) as it:
    for entry in it:
        if entry.is_file():
            print(entry.name)'''

#Complete Example: list files only at top level
'''def print_directory_files(path):
    try:
        for name in os.listdir(path):
            full = os.path.join(path, name)
            if os.path.isfile(full):
                print(name)
    except FileNotFoundError:
        print(f"Directory not found: '{path}'")
    except PermissionError:
        print(f"Permission denied: '{path}'")
    except OSError as err:
        print(f"Error accessing '{path}': {err}")

if __name__ == "__main__":
    folder = input("Enter directory path: ").strip()
    print_directory_files(folder)'''






