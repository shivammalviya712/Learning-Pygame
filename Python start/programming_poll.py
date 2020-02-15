# Author - Shivam Malviya
# Date - 22nd May 2019


filename = "text_files\programming_poll.txt"
print ('\nWhenever you want to exit enter "Exit".\n')

with open (filename,"w") as file_object:
    while True:
        name = input("\nEnter your name : \n").title().strip()
        if  name == "Exit":
            break
        print("Hello! " + name + " you are welcome.")
        reason = input("Why do you like programming?\n").strip()
        if reason.title() == "Exit":
            break

        file_object.write(name + "\n")
        file_object.write("-"+reason.lower()+".\n\n")


