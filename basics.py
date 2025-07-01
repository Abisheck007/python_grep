import random
import sys
import platform
import json
# a = "     Abisheck    "
# # print(a.upper())
# # print(a.strip())
# # print(a.replace("k", "K"))
# for x in a:
#     print (len(x))

# age = 21
# details = f"hi,this is abisheck and my age is {age}"#just simply we can put f infront of our str and we can use our int value inside our str
# # print(details)

# list = ["abi","anandh"]

# list.insert(2,"Abi")
# list.append("ramani")
# # print(list)


# list1 = ["Abi","Dhiraj","Amma"]
# list2 = ["lakshmi"]

# list1.extend(list2)
# list1.remove("Dhiraj")

# print(list1)

# list = ["Abisheck","Ramani","Balasubramaniyam","subhaharini"]

# for i in range(len(list)):
    # print(list[i])

# fetching specific data from one list and putting in another list
# dataset = ["Aanandh","abisheck","Arjun","deepak","devi","maharani","aalbin","binlaidin"]
# newdataset = []

# for x in dataset:
#     if 'a' in x:
#         newdataset.append(x)

# newdataset.sort(reverse=True)


blt1 = ["Abisheck","achu", "messi","veni","renuga","ravi"]
copylist = blt1[:]
#tuples concept
x = ("Abi","Anandh","Dhiraj","Amma")
y = list(x)
y[1] = "Aadhi"
x = tuple(y)
# print(x)

a1 = ("Abi","Anandh")
# print(a1)


#set concept

set1 = {"Abi","Anandh","Dhiraj","Amma"}
set1.add("Aadhi")
# print(set1)


a1 = {"Abi","Anandh"}
a2 = {"Abi","Anandh","Dhiraj","Amma"}
a3 = a1 | a2
# print(a3)

# dictionary concept
data = {
    "name": "Abi",
    "age": 21,
    "hobby": "coding"
}

#Nested dictionaries

# wholefamily = {
#     "fam1" : {
#         "fname" : "Balu",
#         "Mname" : "Ramani",
#         "sonname" : "Abisheck"
#     },
#     "fam2" : {
#         "fname" : "sivasankar",
#         "Mname" : "murugaveni",
#         "sonname" : "prabha"
#     }
# }
# print(wholefamily.items())

#if else concept in python

# a = 19
# b= 10
# if a > b: print("a is greater than b")
# elif a == b:print("a is equal to b")
# else: print("b is greater than a")


# match concept in python

# day = 9
# match day:
#         case 1:
#             print("Monday")
#         case 2:
#             print("Tuesday")
#         case 3:
#             print("Wednesday")
#         case 4:
#             print("Thursday")
#         case 5:
#             print("Friday")
#         case 6:
#             print("Saturday")
#         case 7:
#             print("Sunday") 
#         case _:
#             print("Invalid day")    

#we can also combine data in match concept

# day = 1
# match day:
#         case 1 | 2 | 3:
#                 print("starting of the week")
#         case 4 | 5:
#                 print("middle of the week")
#         case 6 | 7:
#                 print("end of the week")   
#         case _:
#                 print("Invalid day") 

#Functions in python

# def greetings(fname):
#     print("Hello, welcome to the Python basics tutorial! invited by", fname)

# greetings("Abisheck")

# x = platform.system()
# print(x)

x =  {
    "name": "Abi",
    "age": 21,
    "hobby": "coding"
}

y = json.dumps(x)
print(y)