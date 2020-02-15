# Author - Shivam Malviya
# Date - 23rd May 2019


import json

filename = "json_files\\numbers.json"
with open (filename,"r") as f_obj:
    numbers = json.load(f_obj)
print (numbers)

