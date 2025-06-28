import random
import sys

# a = "     Abisheck    "
# print(a.upper())
# print(a.strip())
# print(a.replace("k", "K"))
# for x in a:
#     print (len(x))

# age = 21
# details = f"hi,this is abisheck and my age is {age}"#just simply we can put f infront of our str and we can use our int value inside our str
# print(details)

# list = ["abi","anandh"]

# list.insert(2,"Abi")
# list.append("ramani")
# print(list)

#to append to two list
# list1 = ["Abi","Dhiraj","Amma"]
# list2 = ["lakshmi"]

# list1.extend(list2)
# list1.remove("Dhiraj")

# print(list1)

# list = ["Abisheck","Ramani","Balasubramaniyam","subhaharini"]

# for i in range(len(list)):
#     print(list[i])

# fetching specific data from one list and putting in another list
dataset = ["Aanandh","abisheck","Arjun","deepak","devi","maharani","aalbin","binlaidin"]
newdataset = []

for x in dataset:
    if 'a' in x:
        newdataset.append(x)

newdataset.sort(reverse=True)


blt1 = ["Abisheck","achu", "messi","veni","renuga","ravi"]
copylist = blt1[:]
print(copylist)