#Python program to interchange first and last elements in a list
#list = [12, 35, 9, 56, 24]
# list[0],list[-1] = list[-1],list[0]
# print(list[0],list[-1])
'''list = input("Enter the elements in the list : ").split(",")
for i in range(0,len(list)):
    list[i] = int(list[i])'''
# print(list)   
# temp_variable = list[-1:-2:-1]  
# list[-1:-2:-1] = list[0:1:1]
# list[0:1:1] = temp_variable 
'''list[0:1:1],list[-1:-2:-1] = list[-1:-2:-1],list[0:1:1] 
print(list)
'''
##################################################################################################
#Program to find maximum element in the list
# print(max(list))
# print(min(list))
# print(sum(list))
#print(list.count(list[1])) #check occurence of the number that given as argument
# --or--
# max = 0
# min = 99999999
# counter = 0
# sum = 0
# for i in list:
#     if max < i:
#         max = i
#     if min > i:
#         min = i
#     counter += 1
#     sum += i

# print("Maximum: ",max)
# print("Minimum",min)
# print("Sum: ",sum)
# print("Loop iteration : ",counter)


##################################################################################################

#Program to reverse a string.
#list.reverse()
#print("Reverse the list elements:",list)
#print(list[::-1])
##################################################################################################
#Program to concatenate two strings index wise
# list1 = ["M","na","i","Ke"]
# list2 = ["y","me","s","lly"]
# def concate(a,b):
#     return a+b
# # for i in range(0,len(list1)):
# #     list3.append(list1[i]+list2[i])
# # print(list3)
# list3 = map(concate,list1,list2)
# print(list(list3))
# list3 = [i + j for i, j in zip(list1, list2)]
# print(list3)
##################################################################################################
# Turn every item of a list into its square
# Given a list of numbers. write a program to turn every item of a list into its square.
# Given:
# numbers = [1, 2, 3, 4, 5, 6, 7]
# Expected output:
# [1, 4, 9, 16, 25, 36, 49]
# from calculation import my_square

# #print(list(map(my_square,range(11))))
# list3 = input("Enter the numbers: ").split(",")
# for i in range(len(list3)):
#     list3[i] = int(list3[i])
    
# print(list(map(my_square,list3)))
##################################################################################################
# # Exercise 4: Concatenate two lists in the following order
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# # # Expected output:
# def concate(l1,l2):
#     return l1+" "+l2
# # ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
# print(list(map(concate,list1,list2)))
##################################################################################################
# Exercise 5: Iterate both lists simultaneously
# Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.
# Given

# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]


# for i in range(0,len(list1)):
#     print(list1[i]," ",list2[len(list2)-i-1])
##################################################################################################
# Exercise 6: Remove empty strings from the list of strings
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

# Expected output:

# ["Mike", "Emma", "Kelly", "Brad"]
# for str in list1:
#     if str == "":
#       list1.remove(str)
# i = len(list1)
# for str in range(0,i):
#     if str == "":
#       #list1.remove(str)
#       del list1[str]
# print(list1)
####################################################################################################
# Exercise 7: Add new item to list after a specified item
# Write a program to add item 7000 after 6000 in the following Python List

# # Given:

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# # Expected output:
# list2 = list1[2][2]
# list2.append(700)
# print(list1)

# Exercise 10: Remove all occurrences of a specific item from a list.
# Given a Python list, write a program to remove all occurrences of item 20.

# Given:

# list1 = [5, 20, 15, 20, 25, 50, 20]
# # Expected output:

# # [5, 15, 25, 50]
# for i in range(list1.count(20)):
#     list1[list1.index(20)] = 2
# print(list1)
##############################################################################################
# Exercises on dictionary

# Exercise 1: Convert two lists into a dictionary
# Below are the two lists. Write a Python program to convert them into a dictionary in a way that item from list1 is the key and item from list2 is the value

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
# Expected output:

# # {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# res_dict = (dict(zip(keys,values)))
# print(res_dict)
# dict = {}
# for i in range(len(keys)):
#     dict[keys[i]] = values[i]

# print(dict)

# def create(key,value):
#     return (key,value)
# result = map(create,keys,values)
# print(dict(result))
##############################################################################################
# Exercise 2: Merge two Python dictionaries into one
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# # # Expected output:

# # # {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# dict1.update(dict2)
# print(dict1)
##############################################################################################
# # Exercise 3: Print the value of key ‘history’ from the below dict
# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
# # print(sampleDict.get("class").get("student").get("marks")["history"])
#                 #OR#
# print(sampleDict['class']['student']['marks']['history'])
##############################################################################################
# Exercise 4: Initialize dictionary with default values
# In Python, we can initialize the keys with the same values.

# Given:
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}


# # employee = {}

# employee = dict.fromkeys(employees,defaults)
# print(employee)

# Exercise 5: Create a dictionary by extracting the keys from a given dictionary
# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

# Given dictionary:

# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}

# # # Keys to extract
# # keys = ["name", "salary"]
# dictionary = {}
# keys = sample_dict.keys()

# for i in keys:
#     if i == "name":
#         dictionary.update({i:sample_dict["name"]})
#     if i == "salary":
#         dictionary.update({i:sample_dict["salary"]})
# print(dictionary)

# Exercise 9: Get the key of a minimum value from the following dictionary
# sample_dict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }

# print(min(sample_dict))
#      Both same
# print(min(sample_dict, key=sample_dict.get))

# Exercise 10: Change value of a key in a nested dictionary
# Write a Python program to change Brad’s salary to 8500 in the following dictionary.


# Given:

# sample_dict = {
#     'emp1': {'name': 'Jhon', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 500}
# }
# sample_dict['emp3']['salary'] = 8500
# print(sample_dict)
##################################################################################################
###############STRING###############################################################

# Exercise 1A: Create a string made of the first, middle and last character
# Write a program to create a new string made of an input string’s first, middle, and last character.

# Given:

# str1 = "James"

# first_char = str1[0]

# total_string = len(str1)

# mid_char = int(total_string/2)

# result1 = first_char + str1[mid_char]

# result =  result1 + str1[total_string-1]

# print(result)

# Exercise 2: Append new string in the middle of a given string
# Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.

# Given:









