# Author - Shivam Malviya
# Date - 22nd May 2019


with open("text_files\python.txt") as file_object:
    about_python = file_object.read()
print (about_python)

with open("text_files\python.txt") as file_object:
    for line in file_object:
        print (line.rstrip())

with open("text_files\python.txt") as file_object:
    lines = file_object.readlines()
for line in lines:
    print (line.rstrip().replace ("Python","C"))
