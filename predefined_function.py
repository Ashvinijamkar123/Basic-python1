## Predefined functions are the functions that are already built in language and ready to used without defining them.
# 1) id() : returns the memory address of variable.

# name="ashu"
# print(id(name))

#course="python"
#course1="python"
#print(id(course))                         #2215182515200
#print(id(course1))                        #2215182515200

# course="python"
# print(course)                               
# print(id(course))
# course="java"
# print(course)
# print(id(course))

#___________________________________________________________________________________________________________

# 2) input() : Reads input from the user via the console.

#name=input("enter your name")
#print(name)

# name=input("name:")
# age=input("age:")
# city=input("city:")
# print(name,age,city)

# name=input("enter name of student:")
# address=input("enter address of student:")
# course=input("enter the course:")
# print("My name is",name,"I am from",address,"I choose",course,"course")


# no1=int(input("enter first number:"))
# no2=int(input("enter second number:"))
# sum=no1+no2
# print("sum of",no1,"and",no2,"is",sum)

# no1=int(input("enter first number"))
# no2=int(input("enter second number:"))
# mult=no1*no2
# print("Multiplication=",mult)

# n1=int(input("enter the number:"))
# square=n1*n1
# print("square of",n1,"is",square)
#____________________________________________________________________________________________________

# 3) type(): returns the data type of an object/variable.

# no=100
# no=str(no)
# print(no)
# print(type(no))
# no1=20
# no1=float(no1)
# print(no1)
# print(type(no1))
# no2=20.20
# no2=int(no2)
# print(no2)
# print(type(no2))
# no3="45"
# no3=str(no3)
# print(no3)
# print(type(no3))
#_________________________________________________________________________________________________________

# 4) eval() function : convert the string data into the specific data type.

# num=eval(input("enter the number:"))
# cube=num*num*num
# print("cube of",num,"is",cube)


# len=eval(input("enter length of rectangle:"))
# width=eval(input("enter width of rectangle:"))
# area=len*width
# print("area of rectangle is",area)


# pi=3.14
# r=eval(input("enter the radius:"))
# area=pi*r**2
# print("area if circle is",area)

# side=eval(input("enter side:"))
# p=4*side
# print("perimeter of square=",p)

# pi=3.14
# r=eval(input("enter radius:"))
# circum=2*pi*r
# print("circumference of circle:",circum)


# P=eval(input("enter principle:"))
# R=eval(input("enter rate:"))
# T=eval(input("enter year:"))
# SI=(P*R*T)/100
# print("simple interest=",SI)

#__________________________________________________________________________________________________

# 5) len(): Returns the length of an object like string,list,tuple,etc.

# str="gayatri pacharne"
# print(len(str))
# list=[11,22,33,44,5,66,77,8]
# print(len(list))
# t=(1,2,3,4,5,6,7,[1,2,3])
# print(len(t))

#_______________________________________________________________________________________________

# 6) range(): generates a sequence of numbers.

# for i in range(1,11):
#     print(i)

#_____________________________________________________________________________________________

# 7) max() and min():find the maximum and minimum value in a collection.

# l=[44,22,11,66,98,34]
# print(min(l))
# print(max(l))

#______________________________________________________________________________________________

# 8) sum():calculate the sum of elements in a collection.

# l=[11,22,33,44,55]
# print(sum(l))
# t=(11,22,33,44,55)
# print(sum(t))
#_____________________________________________________________________________________________-

# 9) sorted(): returns a new sorted list from the elements of any iterable.

# l=[4,2,7,55,22,88,66,12]
# print(sorted(l))
# t=(4,2,7,55,22,88,66,12)
# print(sorted(t))

#______________________________________________________________________________________________

# 10) abs(): returns the absolute value of a number(if number is negative,it always returns positive value)

# num=-18.2
# print(abs(num))

#______________________________________________________________________________________________

# 11) round(): rounds a number to a specified number of digits.

# num=18.9
# print(round(num))

#--------------------------------------------------------------------------------------------------

## WAP to print absolute value of number without using predefined function.
# num=eval(input("enter the number:"))
# if num<0:
#     abs_value=-num
#     print("absolute value of number is=",abs_value)
# else:
#     abs_value=num
#     print("absolute value of number is=",abs_value)


