# Author - shivam Malviya
# Date - 22nd May 2019


filename = "text_files\guest.txt"
with open (filename,"w") as file_object:
    file_object.write(input("Please enter your name : ").title())
