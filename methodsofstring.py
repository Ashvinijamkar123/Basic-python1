# upper() method
# syntax: var_name.upper()
"""
name="the kiran academy"
print(name.upper())                       # THE KIRAN ACADEMY
print(name)
"""

# lower() method: Convert given string is in lowercase
# syntax: var_name.lower()

# name="THE KIRAN ACADEMY"
# print(name.lower())                         # the kiran academy


# title():Returns the version of string where each word is titlecased.

name="the kiran academy"
p=name.title()                          # The Kiran Academy
print(name)
print(p)

# # capitalize(): Returns the capitalized version of string
# name="the kiran academy"
# print(name.capitalize())                      # The kiran academy
# print(name)

# # isalpha(): Returns true if given string is alphabetic, otherwise false
# name="Gayatri"
# print(name.isalpha())                          # True
# name="Gayatri123"
# print(name.isalpha())                          # False


# #isnumeric(): returns true if given string is numeric, otherwise false
# name="Gayatri123"                          
# print(name.isnumeric())                      # False
# name="12345"
# print(name.isnumeric())                       # True

# # isalnum():returns true if string contain alphabet or number or both alphabet and number,otherwise false.
# name="123"
# print(name.isalnum())                   # True
# name="gayatri"
# print(name.isalnum())                    # True
# name="gayu123"
# print(name.isalnum())                    # True
# name="gayu@"
# print(name.isalnum())                    # False

# # count():
# name="gayatri"
# print(name.count("a"))                 # 2

# # istitle():Returns true if each letter of given sting in capital,otherwise false
# name="gayatri pacharne"
# print(name.istitle())                 # False
# name="Gayatri Pacharne"
# print(name.istitle())                 # True

# # isspace(): Returns true if given string is only whitespace,otherwise false
# name="gayatri pacharne"
# print(name.isspace())                  # False
# name=" "
# print(name.isspace())                  # True

# # islower():Returns true if given string is in lowercase, otherwise false.
# name="gayatri"
# print(name.islower())             # True

# #isupper():Returns true if given string is in uppercase, otherwise false.
# name="GAYATRI"
# print(name.isupper())             # True

# # replace():used to replace any chracter or word from given string.
# name="the keeran academy"
# print(name.replace("ee","i"))   #the kiran academy
# print(name)                     #the keeran academy

# # endswith(): returns true if given string end with specific string, otherwise false.
# # name="gayatri"
# # print(name.endswith("i"))            #True
# # print(name.endswith("tri"))          #True
# # print(name.endswith("g"))            #False

# # startswith():returns true if given string start with specific string, otherwise false.
# # name="gayatri"
# # print(name.startswith("ga"))          #True
# # print(name.startswith("tri"))         #False

# #strip():removes the leading and trailing whitespace character(such as space, tabs and newlines)
# # course="python "
# # print(course.strip())               # "python"
# # print(course.strip("py"))           # " thon"

# #removeprefix():returns the string with given prefix string removed if present.
# # course="python"
# # print(course.removeprefix("pyt"))       # hon

# #removesuffix():returns the string with given suffix string removed if present.
# course="python"
# print(course.removesuffix("on"))           # pyth
# """

# # sort():
# # syntax:  var_name.sort(key=None,reverse=False)
# l=["My","I","Number","Hello"]
# l.sort(key=len)
# print(l)
# l1=["my","i","number","hello"]
# l1.sort()
# print(l1)
# l1.sort(reverse=True)
# print(l1)



# # fname=input("enter the first name:")
# # lname=input("enter the last name:")
# # name=fname+" "+lname
# # name1=name.upper()
# # print("my name is",name1)


course="python programming language"
print(course.split())#
#print(a)



# # 1) intersection():
# # s1={11,22,33,44}
# # s2={33,44,55,66}
# # ns=s1.intersection(s2)
# # print(ns)                           #{33, 44}


# # 2) difference():
# # s1={11,22,33,44}
# # s2={33,44,55,66}
# # ns=s1.difference(s2)
# # print(ns)
# # ns=s2.difference(s1)
# # print(ns)
# # s1.intersection_update(s2)
# # print(s1)
# # s1.difference_update(s2)
# # print(s1)


# # s1={11,22,33,44,55,66,77}
# # s2={44,55}
# # print(s2.issubset(s1))
# # print(s1.issuperset(s2))


# # s1={1,2,3,4}
# # s2={8,9,5}
# # s1.isdisjoint(s2)
# # print(s1.isdisjoint(s2))


# # s1={22,33,44,55,66}
# # # s1.copy()
# # print(s1.copy())

# # s1={11,22,33,4,5}
# # s2={22,44,55}
# # s2.symmetric_difference(s1)
# # print(s2)


# # s1={11,22,33,4,5}
# # s2={22,44,55}
# # s1.symmetric_difference_update(s2)
# # print(s1)

# # s1={11,22,33,4,5}
# # s2=(22,33,44,55,66)
# # ns=s1.union(s2)
# # print(ns)

# # s1={11,22,33,4,5}
# # s1.

















