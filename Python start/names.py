# Author - Shivam Malviya
# Date - 23rd May 2019


from name_function import get_formated_name

print ("\nEnter 'q' any time you want to quit.")
while True:

    first_name = input ("\nEnter the first name : ")
    if first_name == 'q':
        break

    last_name = input ("Enter the last name : ")
    if last_name == 'q':
        break

    ans = input ("Do you have middle name? (yes or no)\n")
    if ans == "q":
        break

    elif ans == "yes":
        middle_name = input ("\nEnter the middle name : ")
        name = get_formated_name(first_name,last_name,middle_name)

    elif ans == "no":
        name = get_formated_name(first_name, last_name)

    print ("The complete name is : "+name)



