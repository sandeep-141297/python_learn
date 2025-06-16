#Label the program written in problem 4 with comments. 

import os

#  add path of directory
path = 'D:/Learn/Python ChapterWise Notes'

# Get the list of files and directories with the help of 'os' module
entries = os.listdir(path)

# print directory content lists
for item in entries:
    print(item)