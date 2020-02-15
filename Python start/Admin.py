# Author - Shivam Malviya
# Date - 20th May 2019
# Admin

#User class
class User ():

    def __init__(self,first_name,last_name,**inform):

        self.info = {}
        self.info ["First Name"] = first_name.title ()
        self.info ["Last Name"] = last_name.title ()
        for key,value in inform.items ():
            self.info [key.title()] = value


    def describe_user (self):

        print ("\nSome information regarding user are :")
        for key,value in self.info.items():
            print (key+" - "+str(value))


    def greet_user (self):
        print ("Hello! My dear "+" "+self.info ["First Name"]+self.info ["Last Name"]+".")


class Admin(User):

    def __init__(self,first_name,last_name,*previliges,**inform):

        super().__init__(first_name,last_name,inform = inform)
        self.previliges = previliges

    def describe_previliges(self):

        print ("\nThe previliges of an Admin are :")
        for i in self.previliges:
            print ("-"+i)


admin = Admin ("Shivam","Malviya","he can delete post","he can remove users",interest = "Coding",looks = "Handsome")
admin.describe_user()
admin.describe_previliges()

