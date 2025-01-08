# 1) if statement:
## syntax:
#    if condition:
#     #block if

# WAP to check person is eligible for votting or not.
# age=int(input("enter age:"))
# if age>18:
#     print("you are eligible for votting.")

# WAP to iterate only negative numbers.
# l=[11,-22,33,-44,55,-66]
# for num in l:
#     if num<0:
#         print(num)


# WAP to check number is even or not.
# num=eval(input("enter number:"))
# if num%2==0:
#     print("number is even")

# WAP to check number is odd or not.
# num=eval(input("enter the number:"))
# if num%2==1:
#     print("number is odd")


# WAP to print even number from given list.
# l=[11,22,33,44,55]
# for num in l:
#     if num%2==0:
#         print(num)


# WAP to print list of square of odd numbers from given list.
# l=[1,2,3,4,5,6]
# l1=[]
# for num in l:
#     if num%2==1:
#         l1.append(num*num)
# print(l1)


# WAP to print set of cube of even numbers from given list.
# l=[1,2,3,4,5,6]
# s=set()
# for num in l:
#     if num%2==0:
#         cube=num**3
#         s.add(cube)
# print(s)
        
# WAP to print list of name of pass student.
# result={"amruta":78,"bharti":35,"dipak":31,"harshad":67}
# l=[]
# for name,per in result.items():
#     if per>=40:
#         l.append(name)
# print(l)


# WAP to print dictionary of persons who are eligible for votting.
# p={"ajay":25,"vijay":45,"sujay":12,"pranav":17}
# eligible={}
# for name,age in p.items():
#     if age>18:
#         eligible[name]=age
# print(eligible)

# WAP to print the set of names that ends with "i" from given list.
# l=["priti","ashwini","gayatri","payal","Meera","kalpana"]
# s=set()
# for name in l:
#     if (name.endswith("i")):
#         s.add(name)
# print(s)

# WAP to print set of numbers which are divisible by 2 and 3 from the given set.
# s={33,55,87,21,65,78,45}
# d=set()
# for num in s:
#     if num%2==0 and num%3==0:
#         d.add(num)
# print(d)

# WAP to print list of month if it contain 31 days from the given dictionary.
# d2={"Jan":30,"Feb":28,"March":31,"Apr":30,"May":30,"Jun":30,"July":31,"Aug":30,"Sep":30}
# l=[]
# for month,days in d2.items():
#     if days==31:
#         l.append(month)
# print(l)

# WAP  to check number is between 50 and 100.
# num=eval(input("enter the number:"))
# if 50<num<100:
#     print("number is between 50 and 100")


# WAP to check number is perfect square or not.
# num=eval(input("enter the number:"))
# is_perfect_square=False
# if num>0:                                                   # wrong
#     square_root=num**0.5
#     if square_root==int(square_root):
#         is_perfect_square=True
        
# WAP to check number is multiple of 4 but not 6.
# num=eval(input("enter the number:"))
# if num%4==0 and num%6!=0:
#     print("number is multiple of 4 but not 6")

# WAP to check number is single digit or not.
# num=eval(input("enter the number:"))
# if num>=0 and num<10:
#     print("number is single digit")

#_________________________________________________________________________________________________

## if-else statement:
# # syntax:
#   if condition:
#     #block if
#   else:
#     #block else


# per=eval(input("enter the percentage:"))
# if per>=40:
#     print("student is pass")
# else:
#     print("student is fail")

## WAP to check number is greater than 10 or not
# num=eval(input("enter the number:"))
# if num>10:
#     print("number is greater than 10")
# else:
#     print("number is less than 10")

# WAP to print list of positive number and list of negative numbers from given list.
# l=[11,22,-33,44,-55]
# l1=[]
# l2=[]
# for num in l:
#     if num>0:
#         l1.append(num)
#     else:
#         l2.append(num)
# print(l1)
# print(l2)

## WAP to check number is even or not
# num=eval(input("enter number:"))
# if num%2==0:
#     print("number is even")
# else:
#     print("number is odd")


## WAP to check number is odd or even.
# num=eval(input("enter number"))
# if num%2==1:
#     print("number is odd")
# else:
#     print("number is even")

## WAP to print list of even numbers and set of odd numbers
# numbers=[11,-22,33,-44,55,-66]
# even_list=[]
# odd_set=set()
# for num in numbers:
#     if num%2==0:
#         even_list.append(num)
#     else:
#         odd_set.add(num)
# print(even_list)
# print(odd_set)


# l=[1,22,3,4,56,7]
# list1=[]
# set1=set()
# for i in l:
#     if i%2==0:
#         list1.append(i)
#     else:
#         set1.add(i)
# print(list1)
# print(set1)


## WAP to print square of even numbers and cube od odd number
# for num in range(1,11):
#     if num%2==0:
#         print(num**2)
#     else:
#         print(num**3)

## WAP to print list of pass student and list of fail student from given dictionary.
# result={"kunal":67,"rajesh":98,"raj":34,"umesh":32,"lalit":65}
# pass_list=[]
# fail_list=[]
# for name,per in result.items():
#     if per>40:
#         pass_list.append(name)
#     else:
#         fail_list.append(name)
# print(pass_list)
# print(fail_list)

## WAP to increase the percentage of pass student by 2 and fail student by 10 of given dictionary.
# result={"kunal":67,"rajesh":98,"raj":34,"umesh":32,"lalit":65}
# for name,per in result.items():
#     if per>40:
#         result[name]=per+2
#     else:
#         result[name]=per+10
# print(result)

'''
result={"kunal":67,"rajesh":98,"raj":34,"umesh":32,"lalit":65}
for name,per in result.items():
    if per>40:
        del result[per]
print(result)

## WAP to delete the data of all fail student.
result={"kunal":67,"rajesh":98,"raj":34,"umesh":32,"lalit":65}
keys_to_delete=[key for key,value in result.items() if value<40]
for key in keys_to_delete:
    del result[key]
print(result)
'''

# student={"gayatri":34,"priti":23,"neha":27,"onkar":13}
# name_to_delete=[name for name,age in student.items() if age<25]
# for name in name_to_delete:
#     del student[name]
# print(student)


student={"gayatri":34,"priti":87,"neha":27,"onkar":13}
for name,per in list(student.items()):
    if per<40:
        del student[name]
print(student)


#__________________________________________________________________________________________________________
## 3) if-elif-else statement:
# syntax:
# if cond1:
#     body if
# elif cond2:
#     body elif
# else:
#     body else

## WAP to check elder student among two student.
# jay_age=eval(input("enter age of jay:"))
# kumar_age=eval(input("enter age of kumar:"))
# if jay_age>kumar_age:
#     print("jay is elder than kumar")
# else:
#     print("kumar is elder than jay")

## WAP to check elder student among three student.
# s1=int(input("enter age of s1 student:"))
# s2=int(input("enter age of s2 student:"))
# s3=int(input("enter age of s3 student:"))
# if s1>s2 and s1>s3:
#     print("s1 is greater")
# elif s2>s1 and s2>s3:
#     print("s2 is greater")
# else:
#     print("s3 is greater")

# WAP to check number is positive,negative or zero.
# num=eval(input("enter the number:"))
# if num>0:
#     print("number is positive")
# elif num<0:
#     print("number is negative")
# else:
#     print("number is zero")

# WAP to check the grade of student.
# per=eval(input("enter the percentage:"))
# if per>=90:
#     print("A+ grade")
# elif per>=80:
#     print("A grade")
# elif per>=70:
#     print("B+")
# elif per>=60:
#     print("B grade")
# else:
#     print("C grade")

# WAP to create calci.
# num1=eval(input("enter the number1:"))
# operator=input("enter the operator:")
# num2=eval(input("enter the number2:"))
# if operator=="+":
#     print(num1+num2)
# elif operator=="-":
#     print(num1-num2)
# elif operator=="*":
#     print(num1*num2)
# elif operator=="/":
#     print((num1/num2))
# else:
#     print("another operation")

# per=eval(input("enter the percentage:"))
# if per>=90:
#     print("Outstanding")
# elif 80<=per<90:
#     print("Excellent")
# elif 70<=per<80:
#     print("With distinction")
# elif 60<=per<70:
#     print("average")
# else:
#     print("poor")

# WAP to update salary if salary=<20000(increase by 20%),if salary is between 20000-50000(increase by 10%) and if salary>=5000(increase by 5%)
# employee={"uday":15000,"majanu":25000,"jay":35000,"veeru":37000,"pranav":78000,"kunal":60000,"vijay":45000}
# for name,salary in employee.items():
#     if salary=<20000:
#         employee[name]=salary+(salary*(20/100))
#     elif 20000<salary<50000:
#         employee[name]=salary+(salary*(10/100))
#     elif salary>=50000:
#         employee[name]=salary+(salary*(5/100))
#     else:
#         print("invalid condition")
# print(employee)


# l=["ashvini","rani","shruti","kajal"]
# li=[]
# for name in l:
#     if (name.startswith("a")):
#         li.append(name)
# print(li)


# l=["ashvini","rani","shruti","kajal"]
# s=set()
# for i in l:
#     if (i.endswith("l")):
#         s.add(i)
# print(s)
    

# l=[11,-22,-33] 
# l1=[]
# l2=[]
# for num in l:
#     if num>0:
#         l1.append(num)
#     else:
#         l2.append(num)
# print(l1)
# print(l2)

# x=10
# if x>5:
#     print("a",end=" ")
#     if x==10:
#         print("b",end=" ")
# else:
#         print("c",end=" ")
#         print("d")

# a=2024
# if (a%2==0):
#     print("come here")
# else:
#     print("eth ethe eth")

# a=int(input("enter the value of x:"))
# b=int(input("enter the value of z:"))
# c=int(input("enter the value of y:"))
# if a>b and a>c:
#     print("a is greter")
# elif b>a and b>c:
#     print(b," is greter")
# else:
#     print("c is greter")


# a=4+3%5
# print(a)
