# Author - Shivam Malviya
# Date - 22nd May 2019
# Ordered Dictionary


from collections import OrderedDict

favourite_languages = OrderedDict()
favourite_languages["Shivam"] = "Python"
favourite_languages["Shiva"] = "C++"
favourite_languages["Punit"] = "Java"

for name,language in favourite_languages.items():
    print (name.title()+" likes "+language.title()+".")







