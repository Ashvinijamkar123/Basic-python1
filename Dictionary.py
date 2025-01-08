# dictionary: It is comma seprated key values within curly braces { }.
# It is ordered,mutable,heterogeneous collection of elements where data is represented in the form of key and value.
# empty dictionary can be defined as,var_name={ }
# syntax:
#  var_name={key1:value1,key2:value2,...}


# d1={"roll":1,"name":"gayatri","city":"nashik","per":78}
# print(d1)
# d2={"roll":11,"name":"raj","marks":{"math":67,"english":89,"python":88},"per":89}
# print(d2)

#_________________________________________________________________________________________________________________________________________
## How to access data from dictionary
# syntax:var_name[key]
# var_name.get(key)

# d3={"roll":11,"name":"raj","marks":{"math":67,"english":89,"python":88},"per":89}
# print(d3["name"])                                           # raj
# print(d3["marks"]["math"])                                  # 67
# print(d3.get("name"))                                         # raj
# print(d3["marks"].get("math"))                                # 67

#____________________________________________________________________________________________________________________________________

# How to add data into dictionary?
# syntax: var_name[key]=value

# d4={"roll":11,"name":"raj","marks":{"math":67,"english":89,"python":88},"per":89}
# d4["course"]="python"
# print(d4)
# d4["marks"]["java"]=78
# print(d4)

#__________________________________________________________________________________________________________________________________

# How to update data of dictionary ?
# syntax: var_name[key]=uvalue

# d5={"roll":11,"name":"raj","marks":{"math":67,"english":89,"python":88},"per":89}
# d5["name"]="Mahesh"
# print(d5)
# d5["marks"]["english"]=95
# print(d5)

#______________________________________________________________________________________________________________________________

# How to delete data from dictionary ?
# using pop() and del
# syntax:
# var_name.pop(key)
# var_name del[key]

# d5={"roll":11,"name":"raj","marks":{"math":67,"english":89,"python":88},"per":89}
# print(d5.pop("roll"))                                       # 11
# print(d5["marks"].pop("english"))                           # 89
# del d5["per"]
# print(d5)
# del d5
# print(d5)
#____________________________________________________________________________________________________________________

# methods of dictionary:
# 1) keys():It will return list of all keys.
# synatx: var_name.keys()

# d5={"roll":11,"name":"raj","marks":{"math":67,"english":89,"python":88},"per":89}
# print(d5.keys())                                    # dict_keys(['roll', 'name', 'marks', 'per'])
# print(d5["marks"].keys())                           # dict_keys(['math', 'english', 'python'])

# 2) values(): It will return list of all values.
# syntax: var_name.values()

# d5={"roll":11,"name":"raj","marks":{"math":67,"english":89,"python":88},"per":89}
# print(d5.values())                                              # dict_values([11, 'raj', {'math': 67, 'english': 89, 'python': 88}, 89])
# print(d5["marks"].values())                                     # dict_values([67, 89, 88])

# 3) items():It will returns list of tuples of keys and values.
# syntax: var_name.items()

# d5={"roll":11,"name":"raj","marks":{"math":67,"english":89,"python":88},"per":89}
# print(d5.items())
# print(d5["marks"].items())

#___________________________________________________________________________________________________

# d={"name":"gayatri","course":"python","per":75,"city":"Nashik"}
# print(d)
# d={"name":"gayatri","course":"python","per":75,"city":"Nashik","marks":{"math":76,"english":67,"physics":78}}
# print(d)
# print(d["city"])
# print(d["marks"]["english"])


# #How to add data into dictionary:
# d={"name":"gayatri","course":"python","per":75,"city":"Nashik","marks":{"math":76,"english":67,"physics":78}}

# square={1:1,2:4,3:9}
# for i in square:
#     print(i)

# square={1:1,2:4,3:9}
# for i in square.values():
#     print(i)


# d={1:{"name":"raj","city":"nagpur"},2:{"name":"rajesh","city":"nashik"}}
# print(d.keys())
# print(d.values())
# print(d[2].keys())

# l={"rani":89,"ashu":76,"shru":87,"maya":34}
# print(l.values())
# print(l.keys())
# print(l.items())

#___________________________________________________________________________________________________________

# WAP to create dictionary of square of number from given tuple
# t=(1,2,3,4,5)
# d={}
# for i in t:
#     d[i]=i*i
# print(d)

# employee={"akshay":40000,"kunal":30000,"lalit":25000,"vijay":20000,"pranav":15000}if salary is greater than 21000,increase salary by 2000
# employee={"akshay":40000,"kunal":30000,"lalit":25000,"vijay":20000,"pranav":15000}
# for name,salary in employee.items():
#     if salary>21000:
#          employee[name]=salary+2000
# print(employee)


# WAP to create dictionry of cubes of numbers from 11-20.
# d1={}
# for i in range(11,21,1):
#     d1[i]=i*i*i
# print(d1)

# WAP to calculate percentage of student
# obtain_mark=0
# bhushan_result={"mar":30,"eng":40,"hindi":50,"math":60,"sci":70}
# for i in bhushan_result.values():
#     obtain_mark=obtain_mark+i
# per=(obtain_mark/(100*len(bhushan_result)))*100
# print(per)

# result={"mar":30,"eng":40,"hindi":50,"math":60,"sci":70}
# print(result.get("mar"))
# add={"chem":52,"physics":45,"eng":43}
# result.update(add)
# print(result)
# print(result.pop("hindi"))
# print(result.popitem())            # ('physics', 45)
# result.fromkeys


# l=list()
# for num in range(1,11,2):
#     l.append(num**3)
# print(l)

# result={"om":67,"suraj":78,"karan":23,"omkar":32}
# new_dict={}
# for name,per in result.items():
#     if per>=40:
#         new_dict[name]=per
# print(new_dict)

# dict1={}
# for num in range(30,19,-2):
#     if num%2==0:
#         dict1[num]=num*num
# print(dict1)

## create two list l1 and l2,if number is prime add in l2,otherwise in l1.
# L={27,54,34,65,1,44,87,26,18,98,76,59}
# prime=[]
# composite=[]
# for num in L:
#     for n in range(2,num):
#         if num%n!=0:
#             prime.append(num)
#             break
#         else:
#             composite.append(num)
#             break
# print(prime)
# print(composite)


# l=[2,3,4,5,6,7,8,9,10,11]
# l={27,54,34,65,1,44,87,26,18,98,59}
# l1=[]
# l2=[]
# for n in l:
#     for i in range(2,n):
#         if n%i==0:
#             l2.append(n)
#             break
#         else:
#             l1.append(n)
#             break
# print(l1)
# print(l2)



# l={"name":"ashu","corse":"python","per":89}
# l['name']="rani"
# print(l)
# l["city"]="nsk"
# print(l)
# print(l.keys())
# print(l)
# print(l.values())
# print(l.items())


# l={"rani":89,"ashu":76,"shru":87,"maya":34}
# dict={}
# for name,per in l.items():
#     if per<=40:
#         dict[name]=per
# print(dict)

# l={"rani":89,"ashu":76,"shru":87,"maya":34}
# for name,per in l.items():
#     if per>=40:
#         l[name]=per-2
# print(l)

# l={"rani":89,"ashu":76,"shru":87,"maya":34}
# dict={}
# for name,per in l.items():
#     if per<=40:
#         dict[name]=per
# print(dict)

# l={"rani":89,"ashu":76,"shru":87,"maya":34}
# print(l['rani'])
# print(l["ashu"])
# l["raj"]=26
# print(l)
# l["rani"]=98
# print(l)
# print(l.pop("rani"))

# l={"rani":89,"ashu":76,"shru":87,"maya":34}
# del l["maya"]
# print(l)
# l.pop("rani")
# print(l)

# employee={"akshay":40000,"kunal":30000,"lalit":25000,"vijay":20000,"pranav":15000}
# for name,salary in employee.items():
#     if salary<20000:
#         employee[name]=salary+23986
#         print(employee)

# employee={"akshay":40000,"kunal":30000,"lalit":25000,"vijay":20000,"pranav":15000}
# new={}
# for name,salary in employee.items():
#     if salary>=20000:
#         new[name]=salary
# print(new)
            






