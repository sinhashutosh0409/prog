# **1. Write a program to find the length of the string without using inbuilt function (len)**
s = "hello"
count = 0
for item in s:
    count+=1
# print(count)
##########################################################################################
# **2. Write a program to reverse a string without using any inbuilt functions.**
s = "hello"
rev_s=""
for item in s:
    rev_s = item + rev_s
# print(rev_s)
#######################################################################################

# **3. Write a program to replace one string with another. e.g. "Hello World" replace "World" with "Universe".**
a = "hello World"
res = ""
a_list = a.split(" ")
for item in a_list:
    if item == "World":
        res +="Universe"
    else:
        res = res + item + " "
# print(res)

# **4. How to convert a string to a list and vice-versa.**
a = "hello"
a_list = a.split()
# print(a_list)
# print("".join(a_list))

# **5. Covert the string "Hello welcome to Python" to a comma separated string.**
# a = "Hello welcome to Python"
# a_= ",".join(a)
# print(a_)
# l = a.split()
# print(",".join(l))

# **6. Write a program to print alternate characters in a string.**
a = "hello"
for index,key in enumerate(a):
    if index % 2 ==0:
        pass
        # print(key)

# **7. Write a Program to print ascii values of the characters present in a string.**
# a = "hello"
# for item in a:
#     print(ord(item))
#
# **8. Write program to convert upper case to lower case and vice-versa without using inbuilt method.**
a = "HelloPython"
res = ""
for letter in a:
    if ord("a") <= ord(letter) < ord("z"):
        res = res + chr(ord(letter)-32)
    elif ord("A") <= ord(letter) < ord("Z"):
            res = res + chr(ord(letter) + 32)

# print(res)
# **9. Write program to swap two numbers without using 3rd variable.**
a=10
b=20
a,b = b,a
# print(a,b)

#
# **10. Write program to merge two different lists.**
a=[1,2,3,4,5]
b=[2,6,7,8,9]
res = a+ b
# print(res)
res = a.extend(b)
# print(a)

############################################################
# **11. Write program to read a random line in a file. (ex. 50, 65, 78th line)**
# with open("demo1.txt","w") as file:
#     file.writelines("hello there\nhow are you\nare you doing good\n how is you work going on\nhave u completed your work tome\nhiii there")

    # for line_no, line in enumerate(file, start=1):
    #     if line_no == 2:
    #         # print(line)



# **12. Write program to read a random lines in a file. (ex. I want read all lines 10th to 15th line)**
# with open("demo1.txt") as file:
#     count = 0
#     target_line = 1
#     for line in file:
#         count +=1
#         if target_line == count:
#             print(line)
#             # break

###################################
from itertools import islice
# def get_lines(start,end):
#     with open("demo1.txt") as file:
#         for lineno,line in enumerate(file,start=1):
#             if lineno in range(start,end+1):
#                 print(line)
#
# get_lines(1,4)

######
# with open("demo1.txt") as file:
#     data=islice(file,5)
#     for item in data:
#         print(item)

# **13 Program to print last "N" lines of a file.**

# with open("demo1.txt") as file:
#     count = 0
#     for item in file:
#         count = count+1
#     file.seek(0)
#     data = islice(file,count-2,count)
#     for item_ in data:
#         print(item_)

#
# **14. Write a program to check if the given string is Palindrome or not without using reversed method.
a = "aabqaa"
rev = ""
for item in a:
    rev = item + rev
# if rev == a:
#     print("it is a palindrom")
# else:
#     print("it is not a palindrom")

# **15 Write a program to search for a character in a given string and return the corresponding index.**
def some_func(n):
    a = "hello"
    for index,item in enumerate(a):
        if item == n:
            print(index,item)
# some_func("h")
# **16 Write a program to get the below output**
# sentence = "hello world welcome to python programming hi there"
#d = {'h': ['hello', 'hi'], 'w': ['world', 'welcome'], 't': ['to', 'there'], 'p': ['python', 'programming'] }

# **17 Write a to replace all the characters with - if the character occurs more than once in a string**
# s = "hello world"
# new_s = ""
# for item in s:
#     if s.count(item) > 1:
#         new_s += "-"
#     else:
#         new_s += item
# print(new_s)
# **18 write a decorator that returns only positive values of subtraction
#
# **19 How to get the count of number of instances of a class that is being created.**
#
# **20 Write a function which takes a list of strings and integers.If the item is a string it should print as is and if the item is integer of float it should reverse it.**
#
# **21 Write a class named Simple and it should have iteration capability.**
#
# **22 Write a Custom class which can access the values of dictionaries using d['a'] and d.a**
#
# **23 Write a python program to get the below output**
#
# sentence = "Hi How are you"
# # o/p should be "iH woH era uoy"
# sentence_list = sentence.split()
# res = []
# for item in sentence_list:
#     res.append(item[::-1])
# print(" ".join(res))

#########################################################
# **25 Write a lambda function to add two numbers (a, b)**


# **26 What is the output of the following**
sentence = "Hi How are you"
# 	o/p should be "ouy era woH iH"
# s_new = sentence.split()
# s_rev = s_new[::-1]
# s_list = []
# for item in s_rev:
#     s_list.append(item[::-1])
# print(" ".join(s_list))


# # **27 How to remove duplicates from the list without using inbuilt functions**
# items = [1, 2, 3, 4, 1, 2, 3, 4, 5]
# new_item = []
# for item in items:
#     if item not in new_item:
#         new_item.append(item)
# print(new_item)


# **28 Find the longest word in the sentence**
# sentence = "Hello world Welcome to Python"
# s_list = sentence.split()
# # print(s_list)
# res = ""
# for word in s_list:
#     if len(word) > len(res):
#         res = word
# print(res)



# **29 write a program to reverse the values in the dictionary if the value is of type String**

d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}
for key,value in 
# **30 write a program to get 1234**
# t = ('1', '2', '3', '4')
#
# **31 How to get the elements that are in list b but not in list a**
# a = [1, 2, 3]
# b = [1, 2, 3, 4]

# **32 A function takes variable number of positional arguments as input. How to check if the arguments that are passed are more than 5**
#
# **33 Count the number of occurrences of "CRITICAL", "INFO" and "ERROR" lines in a log file.**
# # Assume Below is the contents of the log file
#
# lines = """CRITICAL:Hello world
# INFO: This is an info
# ERROR: This is an error
# CRITICAL: This is critical
# CRITICAL:Hello world
# INFO: This is an info
# ERROR: This is an error
# CRITICAL: This is critical
# CRITICAL:Hello world
# INFO: This is an info
# ERROR: This is an error
# CRITICAL: This is critical
# CRITICAL:Hello world
# INFO: This is an info
# ERROR: This is an error
# CRITICAL: This is critical"""
#
# **34 Write a function to reverse any iterable without using reverse function.**
# >>> a = [1, 2, 3, 4, 5]
#
# **35 Write a function to print the below output.**
# # func("TRACXN", 0)  # Should print RCN
# # func("TRACXN", 1)  # Should print TAX
#
# **36 Sum all the numbers in the below string.**
# s = "Sony12India567Pvt2ltd"
#
# **37 Write a program to sum all the numbers in below string.**
# s = "Sony12India567Pvt2ltd" # eg.12+567+2
#
# **38 Print all the numbers in the below list**
# a = ['abc', '123', 'hello', '23']
#
# **39 Program to print the number of occurrences of characters in a String without using inbuilt functions.**
# >>> s = 'helloworld'
#
# **40 Program to print only the repeated characters and count of the same.**
# >>> s = 'helloworld'
#
# **41 Write a program to get alternate characters of a string in list format.**
# s = 'hello world welcome to python'



















