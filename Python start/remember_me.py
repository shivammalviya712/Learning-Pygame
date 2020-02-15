# Author - Shivam Malviya
# Date - 23rd May 2019

import json

filename = "json_files\\username.json"
try :
    with open (filename,"r") as f_obj:
        name = json.load(f_obj)

except FileNotFoundError:
    with open(filename, "w") as f_obj:
        name = input("Enter your name : ")
        json.dump(name, f_obj)
        print ("I will remember you.")

else:
    print ("Hi! "+name.title()+" you are welcome.")



