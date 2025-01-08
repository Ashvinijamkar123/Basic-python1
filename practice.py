# # How do you convert two lists into a dictionary?.....by using zip fuction.
# keys = ['name', 'age', 'city']
# values = ['John', 30, 'nashik']
# my_dict = dict(zip(keys, values))
# print(my_dict)



# l={'name': 'John', 'age': 30, "mark":87,'city': 'nashik'}
# last_item = my_dict.pop('name')
# print(last_item)
# 


# #select large number.
# l=[2,5,8,9,6]
# l.sort()
# print(l[-1])
# print(l[0])






# #find large and small no
# no=[3,6,7,4,3,6,8,9]
# max1=max(no)
# print("maximum no", max1)
# min1=min(no)
# print("minimum no",min1)

# #sum of digite number
# numbers = [1, 2, 3, 4, 5]
# sum_of_list = sum(numbers)
# print(sum_of_list)


# #cheK polidron present or not.
# def poli(s):
#     return  s ==s[::-1]
# print(poli("true"))
# print(poli("false"))

#remove whight space.
# s="ashu jam kar"
# l=s.strip()# strip() will remove all occurrences of the specified characters from the start and end of the string,
# # but it does not remove characters from the middle of the string.
# print(l)


# s = "xxxxHello World xxxx"
# s_stripped = s.strip("x")
# print(s_stripped)



# def remo(a):
#     out=" "
#     for i in a:
#         if i!= " ":
#             out=out+i
#     return out
# print(remo("ashu jamkar"))

# #Check If List is Empty 





# # Remove Duplicates from List
# numbers = [1, 2, 2, 3, 4, 4]
# unique_numbers = list(set(numbers))
# print(unique_numbers)


# numbers=[1,2,2,3,3,4,4]
# remo=set(numbers)
# print(list(remo))



# # Find Index of Element in List
# numbers = [1, 2, 3, 4]
# index = numbers.index(2)
# print(index)


# # Merge Two Dictionaries
# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}
# merged = {**dict1, **dict2}
# print(merged)


# Sort List in Descending Order
# numbers =[4, 3, 1, 5, 2]
# a=numbers.sort(reverse=True)
# print(a)



# #  Convert List to String
# lst = ['a', 'b', 'c']
# s = ''.join(lst)
# print(s)


# # Flatten a Nested List
# l=[(1,2,3),(3,4,5),(5,6,7)]
# s=[a for b in l for a in b]
# print(s)


# # Random Number Generation
# import random
# random_number = random.randint(1, 100)
# print(random_number)




# # Generate Current Date
# import datetime
# current_date = datetime.datetime.now().date()
# print(current_date)

# # Generate Current time
# import datetime
# current_date = datetime.datetime.now().time()
# print(current_date)