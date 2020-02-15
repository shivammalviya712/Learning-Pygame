# Author - Shivam Malviya
# Date - 22nd May 2019


filename = "text_files\writing_in_the_file.txt"
with open(filename,"a") as file_object:
    file_object.write("I also like finding meanings in large datasets.\n")
    file_object.write("I also love creating apps that can run in a browser.\n")


