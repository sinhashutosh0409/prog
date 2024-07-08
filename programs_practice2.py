# # ######################################################################
# # #1 Write a program to find the length of the string without using inbuilt function (len)**
# #
# s = "hello"
#
# count = 0
# for i in s:
#     count = count + 1
# # print(count)
#
# # #####################################################################
# # 2 Write a program to reverse a string without using any inbuilt functions.**
# #
# s = "hello world"
#
# rev_s = ""
#
# for i in s:
#     rev_s = i + rev_s
# # print(rev_s)
#
# #####################################################################
# # 3 Write a program to replace one string with another. e.g. "Hello World" replace "World" with "Universe".**
# #
# s = "hello world"
# list_s = s.split()
# replaced_ = ""
#
# for i in list_s:
#     if i == "world":
#         replaced_ = replaced_ + "universe"
#     else:
#         replaced_ = replaced_ + i + "  "
#
# # print(replaced_)
# ####################################################################################################
# # # 4How to convert a string to a list and vice-versa
# #
# # s = "hello world"
# # s_list = s.split()
# # print(s_list)
# #
# # s_str = "".join(s_list)
# # print(s_str)
# ##########################################################################################
#
# # # 5   Covert the string "Hello welcome to Python" to a comma separated string
# s = "hello world"
# s_new = ",".join(s)
# # print(s_new)
#
# ############################################################################################
#
# # # 6 # # Write a program to print alternate characters in a string
# # #
# s = "hello world"
#
# # print(s[::2])
#
# ###########################################################################################
#
#
# # # Write a Program to print ascii values of the characters present in a string.
# #
# s = "hello"
#
# # for i in s:
#     # print(ord(i),i)
#
# ##############################################################################
# # # Write program to convert upper case to lower case and vice-versa without using inbuilt method.**
# #****************
# #Type1
# sentence = "HeLlo WOr12lD"
#
# result = ""
# for letter in sentence:
#     if letter in "aeiou":
#         result=result + letter.upper()
#     else:
#         result = result + letter.lower()
#  print(result)

# Type2
#***************
# sentence = "HeLlo WOr12lD"
# res = ""
# for char in sentence:
#     if ord("a") <= ord(char) <= ord("z"):
#         res = res + chr(ord(char)-32)
#     elif ord("A") <= ord(char) <= ord("Z"):
#         res = res + chr(ord(char)+32)
#     else:
#         res = res + char
# print(res)
#########################################################################################################
## Write program to swap two numbers without using 3rd variable

# a = 10
# b = 20
#
# a,b=b,a
#
# print(a)
# print(b)

###################################################################################################
# # Write a program to check if the given string is Palindrome or not without using reversed method
#
# s = "momm"
#
# print(s[::-1] == s)

#####################################################################################################
# # Write a program to search for a character in a given string and return the corresponding index.
# # linear search
#
# s = "hello world"
# key = "w"
#
# for index,letter in enumerate(s):
#     if letter == key:
#         print(f"the index of {letter } is {index}")
#         break
#
# else:
#         print("the key is not found")

#########################################################################################################3

#  Write program to merge two different lists
# lis_ = [1, 2, 3, 5, 8, 10]
# lis__ = [10, 20, 30, 40]
#
# # lis_.extend(lis__)
# print(lis_)
# print(lis_ + lis__)

#######################################################################################################3


# # Write a to replace all the characters with - if the character occurs more than once in a string**
#
# words = "hello world"
#
# res = ""
#
# for word in words:
#     if words.count(word)==1:
#         res = res + word
#     else:
#         res = res + "-"
#
# print(res)


######################################################################################
# # Write a python program to get the below output**
# #
# sentence = "Hi How are you"
# # o/p should be "iH woH era uoy"
# res = []
# s_list = sentence.split()
# for s_ in s_list:
#     res.append(s_[::-1])
#
# print(" ".join(res))

###############################################################################################
# # How to remove duplicates from the list without using inbuilt functions**
# items = [1, 2, 3, 4, 1, 2, 3, 4, 5]
# res = []
# for item in items:
#     if items.count(item) >=1:
#         res.append(item)
# print(res)  # it will give only 5 as output

# type2
# for i in items:
#     if i not in res:
#         res.append(i)
# print(res)

###############################################################################################
# #  write a program to get 1234**
# t = ('1', '2', '3', '4')
#
# res =int( "".join(t))
# print(res)

###############################################################################################

# # 36 Sum all the numbers in the below string.**
# sentence= "Sony12India567Pvt2ltd"
# total = 0
#
# for i in sentence:
#     if i.isdigit():
#         total = total + int(i)
# print(total)

##############################################################################################
# **37 Write a program to sum all the numbers in below string.**
# s = "Sony12India567Pvt2ltd"     # eg.12+567+2
# res = ""
#
# for i in s:
#     if i.isdigit():
#         res = res + i
#     else:
#         res = res + " "
#
# total = 0
# items = res.split()
# for item in items:
#     if item.isdigit():
#         total = total + int(item)
# print(total)



############################################################################################################
# # **38 Print all the numbers in the below list**
# items = ['abc', '123', 'hello', '23', "12.5"]
# res = []
#
# for item in items:
#     if item.isdigit():
#         res.append(item)
# print(res)

##########################################################################################################
# # **39 Program to print the number of occurrences of characters
# # in a String without using inbuilt functions.**
# sentence = 'helloworld'
# dict = {}
# #Type1
# # for letter in sentence:
# #     dict[sentence.count(letter)]=letter
# # print(dict)
#
# ##Type2
#
# for letter in sentence:
#     if letter not in dict:
#         dict[letter]=1
#     else:
#         dict[letter]=dict[letter]+1
# print(dict)

######################################################################################################
# # # **40 Program to print only the repeated characters and
# # # count of the same.**
# sentence = 'helloworld'
# dict={}
# for s in sentence:
#     if sentence.count(s)>1:
#         dict[s]=sentence.count(s)
# print(dict)

##############################################################################################################
# # **41 Write a program to get alternate characters of a string
# # in list format.**
# s = 'hello world welcome to python'
# res = list(s[::2])
# print(res)

###################################################################################################3
# # 44 Write a program to iterate through list and build a new list,
# # only if the items of the list has even number of characters.**
# names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
#
# res = []
# for name in names:
#     if len(name)%2 ==0:
#         res.append(name)
# print(res)

##################################################################################################
# # **45 Write a program to iterate through list and
# # build a new dictionary, only if the items of the list
# # has even no of characters.**
# names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
# dict_names = {}
# for name in names:
#     if len(name)%2==0:
#         dict_names[name]=len(name)
# print(dict_names)


##############################################################################################################
# # 49 Write a Program to print the sum of entire list and
# # sum of only internal list**
list_= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# total_sum =0
#
# for l in list_:
#     inner_sum = 0
#     for inner_ in l:
#         inner_sum = inner_sum + inner_
#         total_sum = total_sum + inner_
#     print(f"the inner sum is {inner_sum}")
# print(f"the outer sum is {total_sum}")
#**********

#by using comprehension

# new_ = [sum(l) for l in list_]
# print(new_)
# print(sum(new_))


####################################################################################################
# # 50 Write a program to reverse the list as below**
# words = ["hi", "hello", "python"]
# #o/p ['nohtyp', 'olleh', 'ih']
#
# words_ = words[::-1]
# words_new = []
# for i in words_:
#     words_new.append(i[::-1])
# print(words_new)


###########################################################################################################
# # **51 Write a program to update the tuple**
# t1 = (1, 2, 3, 4)
# t2 = (100, 200, 300)
# #o/p (1, 2, 3, 4, 100, 200, 300)
#
# print((*t1, *t2))
# t3 = t1 + t2
# print(t3)

##############################################################################################################
# # 59 Write a list comprehension to get a list of even numbers
# # from 1-50**

# list_even = [i for i in range(1,51) if i %2==0]
# print(list_even)

##############################################################################################################
# # 60 Find the longest non-repeated substring in the below string**
# s = "This is a Programming language and Programming is fun"
# s_list = s.split()
# dict_l={}
#
# for item in s_list:
#     if s_list.count(item)==1:
#         dict_l[item]=len(item)
#
# longest_non_repeated = sorted(dict_l)
# print(longest_non_repeated[-1])

#################################################################################################################
# # **61 Write a program to find the duplicate elements in
# # the list without using inbuilt functions**
# names = ['apple', 'google', 'apple', 'yahoo', 'google']
# names_dup = []
# dup = []
#
# for name in names:
#     if name not in names_dup:
#         names_dup.append(name)
#     else:
#         dup.append(name)
#
# print(names_dup)
# print(dup)
############################################################################################################3
# # **62 Write a program to count the number occurrences of each
# # item in the list without using any inbuilt functions**
# names = ['apple', 'google', 'apple', 'yahoo', 'google', 'facebook', 'gmail', 'yahoo']
# dict_= {}

# for name in names:
#     if name not in dict_:
#         dict_[name]=1
#     else:
#         dict_[name]+=1
# print(dict_)

#######################################################################################################################

# # 64 How to create a tuple using range function**
# t = ()
# for num in range(50):
#     t = t + (num,)
# print(t)
##################################################################################################
# # 70 Write a program to get all the duplicate items
# # and the number of times the item is repeated in the list.**
# names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'facebook', 'apple', 'gmail', 'gmail', 'gmail', 'gmail']
# dict_ = {}
#
# for name in names:
#     if name not in dict_:
#         dict_[name] = 1
#     else:
#         dict_[name] += 1
# print(dict_)
######################################################################################################
# # 73 Write a program to print all numeric values in a list**
# items = ['apple', 1.2, 'google', '12.6', 26, '100']
#
# for item in items:
#     if isinstance(item, (int, float)):
#         print(item)

########################################################################################################
# # 77 Write a program to rotate items of the list**
# names = ["apple", "google", "yahoo", "gmail", "facebook", "flipkart", "amazon"]
#
#
# def _rotate(iterable, no_rotation):
#     for _ in range(no_rotation):
#         value_ = iterable.pop()
#         iterable.insert(0,value_)
#
#     return iterable
# print(_rotate(names,2))

############################################################################################################
# # **78 Write a program to rotate characters in a string**

# sentence = " welcome to python world "
#
# s_list = list(sentence)
#
# def rotate_(iterable,no_rotation):
#     for letter in s_list:
#         for letter in range(no_rotation):
#             value = s_list.pop()
#             iterable.insert(0, value)
#         return iterable
#
# print("".join(rotate_(s_list,6)))

#############################################################################################################
# # # Rotating words in a sentence
# sentence = "Hello world welcome to python"
#
# s_items = sentence.split()
#
# def rotate_(iterable,no_rotation):
#     for item in s_items:
#         for item in range(no_rotation):
#             value = iterable.pop()
#             iterable.insert(0,value)
#
#         return iterable
# print(" ".join(rotate_(s_items,2)))

##############################################################################################################
# # 79 Write a program to count the number of white spaces in a
# # given string**
# #
sentence = "Hello world welcome to Python Hi  How are you. Hi how are you"

# count = 0
# for char in sentence:
#     if char == " ":
#         count = count + 1
# print(count)

#############################################################################################################
# # **80 Write a program to print only non-repeated characters in a string**
# s = 'helloworld'
#
# for char in s:
#     if s.count(char)==1:
#         print(char)

#########################################################################################################
# # 82 Write a program to print all the consonants in a given string**
# s = 'helloworld'
#
# for char in s:
#     if char not in "aeiouAEIOU":
#         print(char)

####################################################################################################
# #  Write a function which takes a list of strings and integers.
# #  If the item is a string it should print as is and if the item
# #  is integer or float it should reverse it.**

# def func_(some_list):
#     for item in some_list:
#         if isinstance(item, (int,float)):
#             print(str(item)[::-1])
#         else:
#             print(item)
#
# func_(["hello", 100, 100.2, "world", 96])

#################################################################################################
# # A function takes variable number of positional arguments as input.
# # How to check if the arguments that are passed are more than 5**

# def func_(*args):
#     count = 0
#     for arg in args:
#         count=count+1
#     if count <= 5:
#         print("args is less than or equal to 5 ")
#     else:
#         print("args is more than 5")
#     return count
#
# print(func_(12,34,56,78,98,12))
#############################################################################################################
# # Write a function to reverse any iterable without using reverse function.**
# a = [1, 2, 3, 4, 5]
#
# def func_(iterable):
#     rev = iterable[::-1]
#     return rev
# print(func_(a))

#################################################################################################################
# # Write a function to print the below output.**
# # func("TRACXN", 0)  # Should print RCN
# # func("TRACXN", 1)  # Should print TAX

# def func_(string, n):
#     if n==0:
#         return string[1::2]
#     elif n==1:
#         return string[::2]
#
# print(func_("TRACXN", 1))
##########################################################################################################
# # Write a function to check if the number is Prime

# def prime_no(num):
#     if num > 0:
#         for n in range(2,num):
#             if num % n ==0:
#                 return "it is not a prime no"
#             else:
#                 return "it is a prime no"
#
# print(prime_no(17))

#########################################################################################################
# # Make a function named tail that takes a sequence
# # (like a list, string, or tuple) and a number n and
# # returns the last n elements from the given sequence, as a list.**

# def tail(iterable,n):
#     return iterable[-n]
#
# print(tail([1, 2, 3, 4, 5],2))

########################################################################################################3


















































































































































###################################################################################################





