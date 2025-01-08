# list is collection of comma seprated value within [].
# list is an ordered,mutable,heterogeneous elements collection and duplicate elements are allowed.
# syntax:
# var_name=[val1,val2,val3,...]

# numbers=[10,20,30,40]
# courses=['python','java','cpp','aws']
# print(type(courses))

# evenno=[2,4,6,8,10]
# print(evenno)
# print(id(evenno))
# print(type(evenno))


# name=["gayu","priti","rani","mahi","chetan","paresh","rohit","parag","om","ritesh"]
# print(name)
# print(id(name))
# print(type(name))

# list is ordered data type
# course="python"
# course1=course.upper()
# print(course)
# print(course1)
# print(id(course))
# print(id(course1))

#list is mutable
# l=[11,22,33]
# print("before change:",id(l))
# l.append(44)
# print(l)
# print("after change",id(l))

#list contain heterogeneous element
# l=[11,10.56,3+6j,'False',True,[1,2,3]]
# print(l)

# list contain duplicate elements
# l1=[11,22,33,44,11,22,33]
# print(l1)
#______________________________________________________________________

# Indexing of list
# l=[11,22,[33,44,55],66,77]
# l1=l[2]
# l2=l1[1]
# print(l2)

# l=[11,22,[33,44,55],66,77]
# print(l[2][1])                            # 44
# print(l[2][2])                            # 55


# l=[11,22,["rajesh","pavan","dhiraj",["vijay","ajay"]],33,44,55]
# print(l)
# print(l[1])         #22
# print(l[-2])          #44
# print(l[2][2])        #dhiraj
# print(l[2][3][1])      #ajay
# print(l[2][2][3:6:1])     #raj
# print(l[2][3][0][::-1])     #yajiv
# print(l[2][3][1].upper())   #AJAY

# l=[11,22,["rajesh","pavan","dhiraj",["vijaykumar","ajay"]],33,44,55]
# print(l[2][3][0].count('a'))     #2

# __________________________________________________________

# Slicing of list
# l=[11,22,33,44,55,66]
# print(l[1::2])           #[22,44,66]
# print(l[-2]+l[1])         #77
# print(l[-2::-2])           # [55,33,11]
# print((l[0]**2)+(l[2]**2))   # 1210


# l=[11,22,33,["raj","yash","ram","sham"],44,55]
# print(l[3][1:-1:1])                          #['yash','ram']                        
# print(l[3][-1:-5:-1])                        #['sham','ram','yash','raj']

#________________________________________________________________________________________

# methods of list:
# 1) append():
# l=[11,22,33]
# l.append(44)
# print(l)
# l1=[11,22,33,[44,55,66],88,99]
# l1.append(100)
# print(l1)
# l1[3].append(77)
# print(l1)

# l=[11,22,33,[44,55,66,["raj","pavan"]],88,99]
# l[3][3].append("mayur")
# print(l)
# l=[11,22,33,[44,55,66,["raj","pavan"],77],88,99]
# l[3].append(999)
# print(l)


# 2) insert():
# l=[11,22,33,[44,55,66,["raj","pavan"],77],88,99]
# l.insert(3,888)
# print(l)
        #[11, 22, 33, 888, [44, 55, 66, ['raj', 'pavan'], 77], 88, 99]
# l[4].insert(2,777)
# print(l)
        #[11, 22, 33, 888, [44, 55, 777, 66, ['raj', 'pavan'], 77], 88, 99]
# l[4].insert(5,666)
# print(l)
        #[11, 22, 33, 888, [44, 55, 777, 66, ['raj', 'pavan'], 666, 77], 88, 99]
# l[4][4].insert(1,"vijay")
# pritn(l)
#      #[11, 22, 33, 888, [44, 55, 777, 66, ['raj', 'vijay', 'pavan'], 666, 77], 88, 99]


# updating of list using indexing and slicing:
# l=[11,22,33,[44,55,66,["raj","pavan"],77],88,99]
# l[1]=222
# print(l)
# l[3][1]=555
# print(l)
# l[3][-2][0]="rajesh"
# print(l)
# l[3][4]=777
# print(l)

#______________________________________________________________________________________
#______________________________________________________________________________________

# How to delete data from list?
# remove()
# l=[22,44,66,77,88]
# l.remove(44)
# print(l)
# l=[11,22,["rahul","Kunal"],33,44]
# l[2].remove("Kunal")
# print(l)
# l=[11,22,["rahul","Kunal",[True,"False"]],33,44]
# l[2][2].remove(True)
# print(l)
# l[2][2].remove("False")
# print(l)
# l=[11,22,33,22,44]
# l.remove(22)
# print(l)                            #[11, 33, 22, 44]

#________________________________________________________________________________

# pop()
# l=[11,22,33,44,55,22,77]
# l.pop(-2)
# print(l)
# l=[11,22,33,44,22,55]
# print(l.pop(-2))                                        #22
# print(l)                                                #[11, 22, 33, 44, 55]
# print(l.pop(-2))                                        # 44
# print(l)                                                # [11, 22, 33, 55]
# print(l.pop(-2))                                        # 33
# print(l)                                                # [11,22,55]
# p=["rajesh","pavan","vijay"]
# f=["raj","parth","ajay","sujay"]
# n=f.pop(-1)
# print(n)                    # sujay
# print(f)                    #['raj', 'parth', 'ajay']
# p.append(n)
# print(p)                    #['rajesh', 'pavan', 'vijay', 'sujay']
# p.append(f.pop(-1))
# print(p)                    #['rajesh', 'pavan', 'vijay', 'sujay', 'ajay']
# l=[11,22,33,44,55,"raj"]
# print(l.pop())                #raj
# l.remove()
# print(l)                      # argument error
# l=[11,22,33,44,55,66,77]
# del l[1::2]
# print(l)                       #[22,44,66]


# l=[11,22,88,44,9,66]
# l.copy()
# print(l)
# print(l.copy())
# l.sort()
# print(l)
# l.extend([111,222,333])
# print(l)
# l.extend(())
# print(l)
# l=[1,22,33,44]
# l.reverse()
# print(l)

# l=[11,22,33,44,55]
# l.extend([111,222,333])
# print(l)                        #[11, 22, 33, 44, 55, 111, 222, 333]
# l.append([111,222,333])
# print(l)                        #[11, 22, 33, 44, 55, 111, 222, 333, [111, 222, 333]]


#________________________________________________________________________________________

# # copy()
# student=["raj","vijay","pavan"]
# s=student
# print(s)
# s.append("ajay")                           # wrong
# print(s)
# print(student)
# print(id(student))
# print(id(s))


# student=["raj","vijay","pavan"]
# s=student.copy()
# print(s)
# s.append("ajay")                            # correct
# print(s)
# print(student)
# print(id(student))
# print(id(s))

#________________________________________________________________________________________


# l=[1,5,1,2,3,3,8,2]
# m=l.copy()
# l.append(10)
# print(l)
# print(m)

# import copy
# l=[1,2,[1,2,3],3,4]
# m=copy.deepcopy(l)
# m=l.copy()
# m[2].append(10)
# print(l)
# print(m)


l=["apple","om","shweta","meera","I"]
l.sort(key=len)
print(l)


# l=[1,2,3,4,5,6]
# print(l.pop(-2))
# print(l)

# l=[]
# l.pop()
# print(l)


"""

num=int(input("enter num:"))
mult=1
for n in range(1,11):
    mult=num*n
    print(num,"*",n,"=",mult)


l=[1,2,3,4,5]
print(l[0])
print(l[-1])
print(l[1::2])
l.append(6)
print(l)
l.pop(2)
print(l)


l=[11,22,33,["raj","yash","ram","sham"],44,55]
print(l[3])
print(l[3][2])
l.append(88)
print(l)
l.extend({4,8,1})
print(l)



l=[11,22,33,["raj","yash","ram","sham"],44,55]
l.insert(2,35)
print(l)
print(l[2])


num=int(input("enter no:"))
mult=1
for i in range(1,11):
    mult=(num*i)
    print(num,"*",i,"=",mult)


l=[3,5,7,8,9]
from functools import reduce
max_num=reduce(lambda x,y:x if x>y else y,l)
print(max_num)
"""

l=[3,5,7,8,9]
length=len(l)
def max_num(seq):
    for i in range(length-1):
       for j in range(length):
          if l[i]<l[j]:
            return l[j]
print(max_num(l))

#return larges number.
# l=[3,2,1,8,9]
# l.sort()
# print(l[-1])


        
 



l=[3,5,7,8,9]
print(len(l))
