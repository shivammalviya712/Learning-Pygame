# Author -Shivam Malviya
# Date - 23rd May 2019


filename1 = "text_files\dogs.txt"
filename2 = "text_files\cats.txt"

try:
    with open (filename1,"r") as f_obj:
        contents = f_obj.read()

except FileNotFoundError:
    pass

else:
    name = filename1.split("\\")[1]
    print ("\nThe contents of file "+name+" are:\n")
    print (contents)

try:
    with open(filename2, "r") as f_obj:
        contents = f_obj.read()

except FileNotFoundError:
    pass

else:
    name = filename2.split("\\")[1]
    print ("\nThe contents of file " + name + " are:\n")
    print (contents)