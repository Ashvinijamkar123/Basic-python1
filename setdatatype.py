# s={1,2,3,4,5,6}
# print(s)
# print(type(s))

# s=set([1,2,3,4,5,(1,2,3)])
# print(s)                           # {1, 2, 3, 4, 5, (1, 2, 3)}


# # s=set([1,2,3,4,5,[1,2,3]])
# # print(s)                        # error

# s={11,22,22,11,44,55,11}
# print(s)
# print(len(s))


# s={}
# print(type(s))                  #<class 'dict'>
# s=set()
# print(type(s))                  #<class 'set'>

#_________________________________________________________________________

# How to add data into set ?

# s={1,2,3,4}
# m=s.add(5)
# print(m)
# print(s)

#_____________________________________________________________________

# How to delete data of set ?
# 1) remove():
# s={11,22,33,44}
# s.remove(33)
# print(s)                            #{11, 44, 22}

# # 2) pop():
# s={1,2,3,4,5}
# print(s.pop())                      # 1
# print(s)                             # {2, 3, 4, 5}

# s={1,2,3,4}
# s.discard(2)
# print(s)
# s={2,3,4,5,6}
# s.discard(2)
# print(s)

# # 3) discard():
# s={1,2,3,4,5,6}
# s.discard(3)
# print(s)

# 4) clear: delete all the elements within the set
# s={1,2,3,4,5}
# s.clear()
# print(s)                               # set()

# s={1,2,3,4,5}
# del s
# print(s)                             # name 's' is not defined

#____________________________________________________________________________________________________

## Methods of set:
# 1) intersection():
# set1={11,22,33,44,66,55,99}
# set2={88,33,56,87,34}
# print(set1.intersection(set2))

# # 2) union():
# set1={11,22,33,44,66,55,99}
# set2={88,33,56,87,34}
# print(set1.union(set2))

# # 3) difference():
# set1={11,22,33,44,66,55,99}
# set2={88,33,56,87,34}
# print(set1.difference(set2))

# # 4) disjoint():
# set1={11,22,33,44}
# set2={88,33,56,44,99,87,34}
# print(set1.isdisjoint(set2))
# set1={11,22,33,44}
# set2={55,77,88}
# print(set1.isdisjoint(set2))

# # 4) intersection_update():
# set1={11,22,33,44,66,55,99}
# set2={88,33,56,44,99,87,34}
# set1.intersection_update(set2)
# print(set1)

# # 5) difference_update():
# set1={11,22,33,44,66,55,99}
# set2={88,33,56,44,99,87,34}
# set1.difference_update(set2)
# print(set1)

# 6) issubset():
# set1={11,22,33,44,66,55,99}
# set2={88,33,56,44,99,87,34}
# print(set1.issubset(set2))
# set1={11,22,33,44,66,55,99}
# set2={66,33,99}
# print(set2.issubset(set1))

# # 7) issuperset():
# set1={11,22,33,44,66,55,99}
# set2={88,33,56,44,99}
# print(set2.issuperset(set1))
# set1={11,55,99,43,87,67}
# set2={55,87}
# print(set1.issuperset(set2))

# # 8) symmetric_difference:
# set1={11,22,33,44,66,55,99}
# set2={88,33,56,44,99}
# print(set1.symmetric_difference(set2))

# # 9) symmetric_difference_update:
# set1={11,22,33,44,66,55,99}
# set2={88,33,56,44,99}
# set1.symmetric_difference_update(set2)
# print(set1)

# # 10) pop():
# set1={11,22,33,44,66,55,99}
# set2={88,33,56,44,99}
# print(set1.pop())

#____________________________________________________________________________________________________

# s={11,22,33,44}
# for num in s:
#     print(num)


# WAP to create set of numbers between 33-44.
# s=set()
# for num in range(33,45,1):
#     s.add(num)
# print(s)                                   # {33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44}


# create list to add square of numbers in the list.
# l=list()
# for num in range(50,101):
#     sq=num*num
#     l.append(sq)
# print(l)


# WAP to add name of student in set .
# s=set()
# n=eval(input("how many name you want to enter?"))
# for i in range(n):
#     name=input("enter the name:")
#     s.add(name)
# print(s)


# Create list to add name of mobile phones.
# l=list()
# n=eval(input("how many mobile name you want to enter:"))
# for i in range(n):
#     name=input("enter mobile name:")
#     l.append(name)
# print(l)


# WAP to print sum of all numbers in set.
# s={11,22,33,44,55}
# sum=0
# for num in s:
#     sum=sum+num
# print(sum)    

# WAP to print multiplication of all numbers in set.
# s={11,22,33,44,55}
# mult=1
# for num in s:
#     mult=mult*num
# print(mult)

# WAP to print fibonacci series.
# first=0
# second=1
# n=int(input("enter how many numbers:"))
# for i in range(n):
#     print(first)
#     first,second=second,second+first


# l=list()
# num=eval(input("enter the phone"))
# for i in range(num):
#     n=input("enter phone name:")
#     l.append(n)
# print(l)
