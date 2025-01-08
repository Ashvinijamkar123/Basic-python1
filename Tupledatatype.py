# Tuple: tuple is collection of comma seprated values within  ().
# It is ordered, immutable,heterogeneous collection of elements and duplicate values are allowed.
# syntax: var_name=(val1,val2,val3,...)

# How to access elements of tuple ?
# 1) indexing:To fetch single element from the tuple
# t=(11,22,33,[222,333,444,("raj","pavan","lalit")])
# print(t[2])                      # 33
# print(t[3][1])                   # 333
# print(t[3][3][2])             # lalit

# t=(11,22,33,[222,333,444,("raj","pavan","lalit")])
# print(t[-2])                      # 33
# print(t[-1][-3])                   # 333
# print(t[-1][-1][-1])                #lalit

#_____________________________________________________________
# 2) slicing

# t=(11,22,33,[222,333,444,("raj","pavan","lalit")])
# print(t[0:3])                   # (11,22,33)
# print(t[3][1:3])                # [333,444]
# print(t[3][3][1::1])            # ('pavan','lalit')

#_______________________________________________________________


# from sys import getsizeof
# t=(1,2,3,4,5)                      # 80
# print(getsizeof(t))
                ## 104

#________________________________________________________________

# packing and unpacking

t=(100,200,300)
a,b,c=t                # unpacking
print(b)

x=10
y=20
z=30                    # packing
t=x,y,z
print(t)

l=[1,2,3]
a,b,c=l                 # unpacking
print(b)

