# Author - Shivam Malviya
# Date - 22nd May 2019
# Exception Addition


print ("Give me two integers and I will add them.")
print ("To quit at any time enter 'q'.")

while True:
    try :
        a = int(input("\nEnter the first number : "))

    except ValueError:
        print ("Please enter a valid number.")
        continue

    try :
        b = int(input("Enter the second number : "))

    except ValueError:
        print("Please enter a valid number.")
        continue

    print ("The addition of two numbers is "+str(a+b))




