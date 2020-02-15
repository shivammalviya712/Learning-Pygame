# Author - Shivam Malviya
# Date - 23rd May 2019


def get_formated_name (first_name,last_name,middle_name=""):
    if middle_name:
        name = first_name.strip()+" "+middle_name.strip()+" "+last_name.strip()

    else:
        name = first_name.strip()+" "+last_name.strip()

    return name.title()



