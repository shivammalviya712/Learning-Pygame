# AUthor - Shivam Malviya
# Date - 22nd May 2019
# Die Class


from random import randint

class Die():

    def __init__(self,sides = 6):
        self.sides = sides

    def roll_die(self):
        print ("The number we got is "+str(randint(1,self.sides))+".")


die1 = Die()
die2 = Die(10)
die3 = Die(20)

print ("\nI am going to roll 1st die 10 times")
[die1.roll_die() for i in range (10)]

print ("\nI am going to roll 2nd die 10 times")
[die2.roll_die() for i in range (10)]

print ("\nI am going to roll 3rd die 10 times")
[die3.roll_die() for i in range (10)]
