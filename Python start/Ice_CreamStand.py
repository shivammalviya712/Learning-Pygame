# Author - Shivam Malviya
# Date - 20th May 2019
# Ice Cream Stand

# Resturant class
class Resturant ():

    def __init__ (self,name,cuisine):

        self.name = name
        self.cuisine = cuisine


    def describe_resturant (self):

        print ("The name of the resturant is "+self.name.title()+".\nHere type of cuisine is "+self.cuisine.title())


    def open_resturant (self):

        print ("\nThe restaurant "+self.name.title()+" is open now.")





























