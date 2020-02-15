# Author - Shivam Malviya
# Date - 20th May 2019
# Importing Classes

import Ice_CreamStand

# Child Class
# Ice Cream Parlour
class IceCreamParlour (Ice_CreamStand.Resturant):

    def __init__ (self,name,cuisine,*flavours):

        super().__init__ (name,cuisine)
        self.flavours = flavours
        self.dog = Dog()

    def describe_flavours (self):

        print ("The flavours available in this parlour are :")
        for flavour in self.flavours:
            print ("-"+flavour.title())

    def print_dog(self):
        print ("The dog of this ice cream parlour is "+self.dog.name.title())


class Dog ():

    def __init__(self,name="Ronnie"):
        self.name = name

    def take_care(self):
        print (self.name.title()+" is taking care.")


ice_cream_shop = IceCreamParlour ("Creamy Ice","Chinese","vanilla","strawberry","chocolate","butter scotch","mango")
ice_cream_shop.describe_flavours()
ice_cream_shop.print_dog()
