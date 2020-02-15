# Author - Shivam Malviya
# Date - 22nd May 2019


filename = "text_files\guest_book.txt"
print ("\nWhenever you want to exit enter 'exit'.\n\n")

with open (filename,"w") as file_object:
    while True:
        name = input("Enter your name : \n").title().strip()
        if  name == "Exit":
            break
        file_object.write(name + "\n")
        print("Hello! " + name + " you are welcome.\n")
