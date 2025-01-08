# # WAP to calculate factorial of number.
num=int(input("enter the number:"))
fact=1
if num<0:
    print("factorial of negative number is not calculate.")
elif num==0 or num==1:
    print("factorial of",num,"is 1")
else:
    for i in range(2,num+1):
        fact=fact*i
    print("factorial of",num,"is",fact)


# # WAP to calculate factorial of any number(using while loop)
# num=eval(input("enter the number:"))
# i=1
# fact=1
# while i<=num:
#     fact=fact*i
#     i=i+1
# print(fact)

# num=eval(input("enter num:"))
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
# print(fact)

#________________________________________________________________________________________________________________________

## WAP to check number is perfect or not.
# num=eval(input("enter num:"))
# sum=0
# for i in range(1,num):
#     if num%i==0:
#       sum=sum+i
#       if sum==num:
#         print("number is perfect")
#       else:
#          print("not perfect")

## WAP to check string is palindrome or not.
# str=input("enter the string:")
# if str[::1]==str[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")

## WAP to check number is palindrome or not.
# num=eval(input("enter number:"))
# string=str(num)
# if string[::1]==string[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")

#_________________________________________________________________________________________________________

## WAP to check number is armstrong or not.
# num=eval(input("enter the number:"))
# num1=str(num)
# sum=0
# for n in num1:
#     new_num=int(n)
#     sum=sum+(new_num**3)
# if sum==num:
#     print("armstrong")
# else:
#     print("not armstrong")


