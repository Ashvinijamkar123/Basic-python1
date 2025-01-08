## WAP to demonstrate continue statement.
l=[1,2,3,4,5,6,7,8,9]
i=0
while i<8:
    print(i)
    i=i+1
    continue

## WAP to demonstrate \n(new line).
# print("hello student welcome to the TKA")
# print("hello\nstudent\nwelcome to the TKA")
# print("Hello \nstudent \nwelcome to the TKA")

## WAP to demonstrate \t(tab).
# print("hello\t\tstudent")
# print("I\t\t\tam\t\t\tgayatri")

#_____________________________________________________________________________________________________
## end,sep are the parameters of print() function.
## the default value of end is whitespace i.e end=""
## the default value of sep is \n(new line) i.e sep="\n"

## WAP to demonstrate sep.
# n1=100
# n2=200
# n3=300
# print(n1,n2,n3,sep=" ")
# print(n1,n2,n3,sep="@")
# print(n1,n2,n3,sep=" @ ")
# print(n1,n2,n3,sep=" # ")

## WAP to demonstrate end.
# n1=100
# n2=200
# n3=300
# print(n1,end="\n")
# print(n2,end="\n")
# print(n3,end="\n")   

# print(n1,end="@")
# print(n2)
# print(n3)

#_________________________________________________________________________________________________
### String formatting:

# n1=eval(input("n1:"))
# n2=eval(input("n2:"))
# print("sum of %d and %d is"%(n1,n2))
# print("sum of %d and %d is %d"%(n1,n2,n1+n2))
# print("sum of %d and %d is %d"%(n1,n2,n1+n2))

## WAP to to calculate square of number.
# num=int(input("enter the number:"))
# print("square of %d is %d"%(num,num*num))


# n1=10.5
# n2=3.6234567
# print("sum of %0.2f and %0.3f is %0.4f"%(n1,n2,n1+n2))

# n1=10.5
# n2=11.5
# print("sum of %0.2f and %0.3f is %0.4f"%(n1,n2,n1+n2))


# n1=10
# n2=20                                                 # There is no change in int value of  %0.2d
# print("sum of %0.2d and %0.2d is %0.2d"%(n1,n2,n1+n2))

#_________________________________________________________________________________________________---

### %d ===> integer
### %f ===> float
### %s ===> string

# fname="rajesh"
# lname="patil"
# city="nashik"
# print("my name is %s %s I am from %s"%(fname,lname,city))
# print("my name is %s%s I am from %s"%(fname,lname,city))

## 1) format() method

# name="Gayatri"
# city="Nashik"
# print("My name is {} and I am from {}".format(name,city))

# n1=eval(input("n1:"))
# n2=eval(input("n2:"))
# n3=eval(input("n3:"))
# print("Product of {},{} and {} is {}".format(n1,n2,n3,n1*n2*n3))


# name="Gayatri"
# city="Nashik"
# print("My name is {} and I am from {}".format(city,name))


# name="Gayatri"
# city="Nashik"
# print("My name is {n} and I am from {c}".format(c=city,n=name))

# name="priti"
# age=25
# city="pune"
# print("my name is {} i am from {} year old and i am from {}".format(name,age,city))

# name="priti"
# age=25
# city="pune"
# print("my name is {} i am from {} year old and i am from {}".format(age,name,city))

# name="priti"
# age=25
# city="pune"
# print("my name is {1} i am from {0} year old and i am from {2}".format(age,name,city))
#______________________________________________________________________________________________________

## 2) fstring :

# name="priti"
# age=25
# city="pune"
# print(f"my name is {name} i am {age} year old and i am from {city}")

# name="priti"
# age=25
# city="pune"
# print("my name is {} i am from {} year old and i am from {}")

#_________________________________________________________________________________________________________________________

name="ashu"
sname="jmk"
print("i am {1} {0}". format(name,sname))