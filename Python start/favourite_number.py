# Author - Shivam Malviya
# Date - 23rd May 2019

import json

filename = "json_files\\favourite_number.json"
try:
    with open(filename,"r") as f_obj:
        favourite_number = json.load(f_obj)

except FileNotFoundError:

    with open(filename,"w") as f_obj:
        favourite_number = input("Enter your favourite number and i will remember it : ")
        json.dump (favourite_number,f_obj)

else:
    print ("Your favourite number is "+favourite_number+".")


