# **1. Write a program to find the length of the string without using inbuilt function (len)**
word = "hello"
count = 0
for item in word:
    count+=1
# print(count)
#################################################################################
# **2. Write a program to reverse a string without using any inbuilt functions.**
word = "hello"
result = ""
for item in word:
    result = item + result
# print(result)
###################################################################################
# **3. Write a program to replace one string with another. e.g. "Hello World" replace "World" with "Universe".**
word = "Hello World"
s_list = word.split()
result = ""
for item in s_list:
    if item == "World":
        result += "Universe"
    else:
        result += item + " "
# print(result)
##############################################################################################
# **4. How to convert a string to a list and vice-versa.**
word = "hello"
# a=word.split()
# print(a)
# print("".join(a))

################################################################################################

# **5. Covert the string "Hello welcome to Python" to a comma separated string.**
sentence = "Hello welcome to Python"
# print(",".join(sentence))
################################################################################################
# **6. Write a program to print alternate characters in a string.**
sentence = "Hello welcome to Python"
# print(sentence[::2])
# for index,item in enumerate(sentence):
#     if index % 2 == 0:
#         print(item)
###########################################################################################
# **7. Write a Program to print ascii values of the characters present in a string.**
sentence = "Hello welcome to Python"
# for item in sentence:
#     print(item,ord(item))
##########################################################################################
# **8. Write program to convert upper case to lower case and vice-versa without using inbuilt method.**
sentence = "Hello Welcome To Python"
result = ""
for item in sentence:
    if ord("a") <= ord(item) <= ord("z"):
        result = result + chr(ord(item) - 32)
    elif ord("A") <= ord(item) <= ord("Z"):
        result = result + chr(ord(item) + 32)
    else:
        result = result + item
# print(result)
############################################################################
# **9. Write program to swap two numbers without using 3rd variable.**
a=10
b=20
a,b=b,a
# print(a,b)
##################################################################################
# **10. Write program to merge two different lists.**
a=[1,2,3]
b=[4,5,6]
# print(a+b)
# a.extend(b)
# print(a)
#################################################################################

# **11. Write program to read a random line in a file. (ex. 50, 65, 78th line)**
from itertools import islice
def read_random(n):
    with open("text1.txt") as file:
        for index,line in enumerate(file):
            if index == n:
                return line
# print(read_random(2))
# **12. Write program to read a random lines in a file. (ex. I want read all lines 10th to 15th line)**
def read_lines(start,end):
    with open ("text1.txt") as file:
        lines = islice(file,start,end)
        for item in lines:
            print(item)

# print(read_lines(1,3))
# **13 Program to print last "N" lines of a file.**
from collections import deque
def read_last(n):
    with open("text1.txt") as file:
        lines = deque(file,n)
        for item in lines:
            print(item)
# print(read_last(3))
# **14. Write a program to check if the given string is Palindrome or not without using reversed method.
word = "aabaa"
rev = ""
for item in word:
    rev = item + rev
# if rev == word:
#     print("its a palindrom")
# else:
#     print("its not a palindrom")
####################################################################################################
# **15 Write a program to search for a character in a given string and return the corresponding index.**
word = "hello"
def search_(n):
    for index,item in enumerate(word):
        if item == n:
            return index
# print(search_("o"))
######################################################################################################
# **16 Write a program to get the below output**
sentence = "hello world welcome to python programming hi there"
# d = {'h': ['hello', 'hi'], 'w': ['world', 'welcome'], 't': ['to', 'there'], 'p': ['python', 'programming'] }
d = {}
s_list = sentence.split()
for item in s_list:
    if item[0] not in d:
        d[item[0]] = [item + " "]
    else:
        d[item[0]] += [item]
# print(d)
###################################################################################################
# **17 Write a to replace all the characters with - if the character occurs more than once in a string**
sentence = "hello world welcome to python programming hi there"
res = ""
for item in sentence:
    if sentence.count(item) > 1:
        res = res + "-"
    else:
        res = res + item
# print(res)
##################################################################################################
# **18 write a decorator that returns only positive values of subtraction**
def positive_only(some_func):
    def wrapper(*args):
        res = some_func(*args)
        return abs(res)
    return wrapper
@positive_only
def sub(a,b):
    return a-b
# print(sub(10,20))
# **19 How to get the count of number of instances of a class that is being created.**
class Demo:
    count = 0
    def __init__(self):
        Demo.count += 1
obj1 = Demo()
obj2 = Demo()
# print(Demo.count)


# **20 Write a function which takes a list of strings and integers.If the item
# is a string it should print as is and if the item is integer of float it should reverse it.**
def demo(some_list):
    for item in some_list:
        if isinstance(item,str):
            print(item[::-1])
        else:
            print(item)
# print(demo([100.9,"hello", 1.98]))
#############################################################################################


# **23 Write a python program to get the below output**
sentence = "Hi How are you"
# o/p should be "iH woH era uoy"
rev = []
s_list = sentence.split()
for item in s_list:
    rev.append(item[::-1])
# print(" ".join(rev))

# **25 Write a lambda function to add two numbers (a, b)**
add = lambda a,b:a+b
# print(add(10,20))
#######################################################
# **26 What is the output of the following**
sentence = "Hi How are you"
# 	o/p should be "ouy era woH iH"
res = []
s_list = sentence.split()
for item in s_list:
    res.append(item[::-1])
a=res[::-1]
# print(" ".join(a))

# **27 How to remove duplicates from the list without using inbuilt functions**
items = [1, 2, 3, 4, 1, 2, 3, 4, 5]
item = set(items)
res = list(item)
# print(res)


# **28 Find the longest word in the sentence**
sentence = "Hello world. Welcome to Python"
s_list = sentence.split()
d = {}
for item in s_list:
    if item not in d:
        d[item] = len(item)
res = (sorted(d,key=len,reverse=True))
# print(res[0])

# **29 write a program to reverse the values in the dictionary if the value is of type String**
d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}

# for key,value in d.items():
#     if isinstance(value,str):
#         print(value[::-1])
####################################################################################
# **30 write a program to get 1234**
t = ('1', '2', '3', '4')
res = ""
for item in t:
    res += item
# print(res)
# **31 How to get the elements that are in list b but not in list a**
a = [1, 2, 3]
b = [1, 2, 3, 4]

# for item in b:
#     if item not in a:
#         print(item)
###################################################################################################
# **32 A function takes variable number of positional arguments as input.
# How to check if the arguments that are passed are more than 5**
def some_func(*args):
        if len(args) > 5:
            print("it is more than 5 arguments")
        else:
            print("it is less than 5 args")
# some_func(1,2,3)

######################################################################################################
# **33 Count the number of occurrences of "CRITICAL", "INFO" and "ERROR" lines in a log file.**
# # Assume Below is the contents of the log file
lines = """CRITICAL:Hello world
INFO: This is an info
ERROR: This is an error
CRITICAL: This is critical
CRITICAL:Hello world
INFO: This is an info
ERROR: This is an error
CRITICAL: This is critical
CRITICAL:Hello world
INFO: This is an info
ERROR: This is an error
CRITICAL: This is critical
CRITICAL:Hello world
INFO: This is an info
ERROR: This is an error
CRITICAL: This is critical"""

lines_list = lines.split("\n")
d={}
for line in lines_list:
    msg,info=line.split(":")
    if msg not in d:
        d[msg]=1
    else:
        d[msg]+=1
# print(d)


#########################################################################################
# **34 Write a function to reverse any iterable without using reverse function.**
a = [1, 2, 3, 4, 5]
def rev_(some_item):
    res = []
    for item in some_item:
        res = [item] + res
    print(res)

# print(rev_(a))



# **35 Write a function to print the below output.**
# func("TRACXN", 0)  # Should print RCN
# func("TRACXN", 1)  # Should print TAX
def func(some_string,pattern):
    if pattern == 0:
        return some_string[1::2]
    elif pattern ==1:
        return some_string[::2]


# print(func("TRACXN", 0))
# **36 Sum all the numbers in the below string.**
s = "Sony12India567Pvt2ltd"
res = 0
for item in s:
    if item.isdigit():
        res = res + int(item)
# print(res)
########################################################################

# **37 Write a program to sum all the numbers in below string.**
s = "Sony12India567Pvt2ltd" # eg.12+567+2
new_s = ""
for item in s:
    if item.isdigit():
        new_s += item
    else:
        new_s += " "

new_list = new_s.split()
res = 0
for item in new_list:
    res = res + int(item)
# print(res)

# **38 Print all the numbers in the below list**
a = ['abc', '123', 'hello', '23']
# for item in a:
#     if item.isdigit():
#         print(item)
# **39 Program to print the number of occurrences of characters in a String without using inbuilt functions.**
s = 'helloworld'
d = {}
for item in s:
    if item not in d:
        d[item] = 1
    else:
        d[item]+= 1
# print(d)

# **40 Program to print only the repeated characters and count of the same.**
s = 'helloworld'
d = {}
# for item in s:
#     if item not in d:
#         d[item] = 1
#     else:
#         d[item]+= 1
# for char,count in d.items():
#     if count > 1:
#         print(char)

# **41 Write a program to get alternate characters of a string in list format.**
s = 'hello world welcome to python'
# s_rev = s[::2]
# s_list = []
# for item in s_rev:
#     s_list.append(item)
# print(s_list)

# **42 Write a program to get square of list of number's using lambda function .**
a = [1, 2, 3, 4, 5]
# square = lambda num:num ** 2
# res = map(square,a)
# for item in res:
#     print(item)

# **43 Write a function that accepts two strings and returns True if the two strings are anagrams of each other.**
def anagrams(a,b):
    if "".join(sorted(a)) == "".join(sorted(b)):
        return True
# print(anagrams("ate","eat"))
# **44 Write a program to iterate through list and build a new list,only if the items of the list has even number of characters.
names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
new_names = []
for item in names:
    if len(item) % 2 ==0:
        new_names.append(item)
# print(new_names)

# **45 Write a program to iterate through list and build a new dictionary,
# only if the items of the list has even number of characters.**
names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
new_names = {}
for item in names:
    if len(item) % 2 ==0:
        if item not in new_names:
            new_names[item] = len(item)
# print(new_names)


# **46 Write a program which squares the numbers in a list using map object**
# a = [1, 2, 3, 4, 5]
# square = lambda num:num ** 2
# print(list(map(square,a)))

# **47 Count number of lines in a file without loading the file to the memory**
count = 0
with open("text1.txt") as file:
    for line in file:
        count+=1
# print(count)
########################################################################################################
# **48 Printing line and line no's**
# with open("text1.txt") as file:
#     for lineno,line in enumerate(file,start=1):
#         print(lineno,line)
#########################################################################################################
# **49 Write a Program to print the sum of entire list and sum of only internal list**
l = [[1,2,3],[4,5,6],[7,8,9]]
# new_l = []
# for item in l:
#     new_l.append(sum(item))
# print(new_l)
# print(sum(new_l))
# **50 Write a program to reverse the list as below**
words = ["hi", "hello", "python"]
# # o/p ['nohtyp', 'olleh', 'ih']
res = []
for word in words:
    res.append(word[::-1])
# print(res[::-1])

# **51 Write a program to update the tuple**
t1 = (1, 2, 3, 4)
t2 = (100, 200, 300)
# # o/p (1, 2, 3, 4, 100, 200, 300)
# print(t1 + t2)
##########################################################################
# **52 Write a program to replace value present in nested dictionary.**
d = {'a': 100, 'b': {'m': 'man', 'n': 'nose', 'o': 'ox', 'c': 'cat'}}
# # Replace "nose" with "net"
# d["b"]["n"]='net'
# print(d)
########################################################################
# **53 Write a program to count the number of white spaces in a file.**
count = 0
with open("text1.txt") as file:
    for line in file:
        for char in line:
            if char == " ":
                count +=1
# print(count)
#########################################################################################################
# **54 Grouping anagrams.**
words = ['eat', 'ate', 'tea', 'hello', 'silent', 'listen']
d = {}
for item in words:
    key = "".join(sorted(item))
    if key not in d:
        d[key] = item + " "
    else:
        d[key] += item + " "
# print(d)

# **55 What is the difference between defaultdict and normal dictionary.**
# """
# Defaultdict
# -----------
# 1. When each key is encountered for the first time, it will not be there in the mapping.
# 2. So an entry is automatically created with default value (an empty list in case of defaultdict of list and zero in case of defaultdict int).
# 3. When keys are encountered again, the look-up proceeds normally as like a normal dictionary.
# 4. So, in defaultdict, creation of key, initialisation will happen simultaneously.
#
# Normal Dictionary
# ------------------
# 1. In case of normal dictionary, if the key does not exist, "KeyError" is raised.
# 2. In order to work on the value, first the key needs to be created and initialised.
# """
# ```
# **56 Explain property decorator in python.**
# ```python
# #
# ```
# **57 What is Mutable and Immutable datatypes.**
# ```python
# """
# 1. Mutable datatypes are objects whose value can be changed after creation. e.g. list, dict, set, user defined classes.
# 2. Immutable datatypes are objects whose value can not be changed after creating. e.g. int, float, bool, tuple, namedtuple
# """
# ```
# **58 Explain get() method in dictionaries.**
# ```python
# """
# point =  {'a': 1, 'b': 2}
# 1. Values of dictionary can be accessed in two different ways. using square bracket syntax and the other one is using get() method.
# 2. When we try to access a key of a dictionary which does not exist using square bracket syntax (point['c']), "KeyError" exception is raised.
# 3. When we try to access a key of a dictionary which does not exist using get() method (point.get('c')), None is returned and no exception is raised.
# 4. We can pass a positional argument to get() method as custom message, so that get() method returns the custom message if the key does not exist.
#            e.g. profile.get('c', 'Sorry the key does not exist')
# """
# ```
# **59 Write a list comprehension to get a list of even numbers from 1-50**
res = [i for i in range(1,51) if i % 2 == 0]
# print(res)
###################################################################################
# **60 Find the longest non-repeated substring in the below string**

s = "This is a Programming language and Programming is fun"
s_list = s.split()
item_len = len(s_list[0])

for item in s_list:
    if s_list.count(item) ==1 and len(item) > item_len:
        item_len = len(item)
        # print(item)
# **61 Write a program to find the duplicate elements in the list without using inbuilt functions**
names = ['apple', 'google', 'apple', 'yahoo', 'google']
d = {}
# for item in names:
#     if item not in d:
#         d[item] = names.count(item)
# for key,value in d.items():
#     if value > 1:
#         print(key)

#################################################################################
# **62 Write a program to count the number occurrences of each item in the list without using any inbuilt functions**
names = ['apple', 'google', 'apple', 'yahoo', 'google', 'facebook', 'gmail', 'yahoo']
d = {}
for item in names:
    if item not in d:
        d[item] = 1
    else:
        d[item] += 1
# print(d)

# **63 Write a function to check if the number is Prime**
def is_prime(n):
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            count += 1
    if count == 2:
        print("it is a prime no")
    else:
        print("it is not a prime no")
# print(is_prime(6))
# **64 How to create a tuple using range function**
t = ()
for num in range(50):
    t = t + (num,)
# print(t)
################################################################################################
# **65 Write a program to find the largest number in the list without using any inbuilt functions**
numbers = [10, 20, 30, 40, 50]
largest_no = numbers[0]
for item in numbers:
    if item > largest_no:
        largest_no = item
# print(largest_no)

#66 Write a method that returns the last digit of an integer. For example, the call of get_last_digit(3572) should return 2.
def get_last_digit(n):
    item = str(n)
    return item[-1]
# print(get_last_digit(3456))

# **67 Write a program to find most common words in a given list.**
words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the',
'eyes', 'look', 'into','my', 'eyes', "you're", 'under'
]
d = {}
for word in words:
    if word not in d:
        d[word] = 1
    else:
        d[word] += 1

pair= d.items()
def most_common(item):
    return item[1]
res = (sorted(pair,key=most_common))
# print(res[-1])
################################################################################################
# **68 Make a function named tail that takes a sequence (like a list, string, or tuple) and a number n
# and returns the last n elements from the given sequence, as a list.**
def tail(some_seq,n):
    return some_seq[-n:]

# print(tail([1,2,3,4,5,6,7,8,9],3))

# **69 Write function named is_perfect_square that accepts a number and returns True if it's a perfect
# square and False if it's not.**
def is_perfect_square(n):
    if n < 0:
        return False
    else:
        root = n ** 0.5
        if root * root == n:
            print("it is a perfect square")
        else:
            print("not a perfect square")

# is_perfect_square(3)

# 70 Write a program to get all the duplicate items and the number of times the item is repeated in the list.**
names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'facebook', 'apple', 'gmail', 'gmail', 'gmail', 'gmail']
d = {}
# for name in names:
#     if name not in d:
#         d[name] = 1
#     else:
#         d[name] += 1
#
# for key,value in d.items():
#     if value > 1:
#         print(key)


# **71 Write a program to count the number of occurrences of each word in a file.**
with open("text1.txt") as file:
    count = 0
    for line in file:
        word= line.split()
        for w in word:
            count+=1
# print(count)

# **72 Write a program to count the number of occurrences of vowels in a file.**
with open("text1.txt") as file:
    count = 0
    for line in file:
        for char in line:
            if char in "aeiou":
                count +=1
# print(count)


# **73 Write a program to print all numeric values in a list**
items = ['apple', 1.2, 'google', '12.6', 26, '100']
# for item in items:
#     if isinstance(item,(int,float)):
#         print(item)

#####################################################################################################################
#
# **74 Triangle Patterns**
# *
# * *
# * * *
# * * * *
# * * * * *
# for i in range(6):
#     print("* " * i )
#####################################################################################################################
#         *
#       * *
#     * * *
#   * * * *
# * * * * *
# for i in range(6):
#     print(f"{" *" * i:>12} ")
###################################################################################################################
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
# for i in range(6):
#     print(f"{"* " * i :^12}")
###################################################################################################################
# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# for i in range(5,-0,-1):
    # print("* " * i)
#####################################################################################################################
# * * * * * *
#   * * * * *
#     * * * *
#       * * *
#         * *
#           *
# for i in range(5,0,-1):
    # print(f"{"* " * i :>12}")

##################################################################################################################
#  * * * * * *
#   * * * * *
#    * * * *
#     * * *
#      * *
#       *
# for i in range(6,0,-1):
#     print(f"{"* " * i:^12}")



##################################################################################################################
# # Number Pattern in triangle (Left Justified)
#
# 1
# 12
# 123
# 1234
# 12345
res = ""
# for i in range(1,6):
#     res = res + str(i)
#     print(res)
################################################################################################################
# # Number Pattern in triangle (Right Justified)
#
#     1
#    12
#   123
#  1234
# 12345
res = ""
# for i in range(1,6):
#     res = res + str(i)
#     print(f"{res:>5}")


####################################################################################################################
# # Number Pattern in triangle (Centre)
#
#      1
#     1 2
#    1 2 3
#   1 2 3 4
#  1 2 3 4 5
# ```
res = ""
# for i in range(1,6):
#     res = res + str(i) + " "
#     print(f"{res:^10}")

########################################################################################################################
# **148 write a program to print the below pattern**
# ```python
# 1 2 3 *
# 1 2 * 4
# 1 * 3 4
# * 2 3 4
# for i in range(4,0,-1):
#     for j in range(1,5):
#         if i == j:
#             print("*", end = " ")
#         else:
#             print(j, end=" ")
#     print()

################################################################################################################
# **143 write a program to get the below output using while loop**
# 1
# 12
# 123
# 1234
n = 4
row = 1
res = ""
while row <= n:
    res = res + str(row)
    row = row + 1
    # print(res)

###################################################################################################################
# **88 Write a program to get the below output**
# *
# *
# *
# * *
# *
# * * *
# *
# * * * *
# *
# * * * * *
# for i in range(1,6):
#     print("* ")
    # print("* " * i)
#####################################################################################################################
# **89 Write a program to get the below output**
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# >>> [1, 2]
#     [3, 4]
#     [5, 6]
#     [7, 8]
#     [9]

# for i in range(0,len(a),2):
    # print(a[i:i+2])

#######################################################################################################################
# **75 Write a program count the occurrence of a particular word in the file**
def word_count(n):
    with open("text1.txt") as file:
        count = 0
        for line in file:
            word = line.split()
            for w in word:
                if n == w:
                    count +=1
    return count
# print(word_count("java"))
######################################################################################################
# **76 Write a program map a product to a company and build a dictionary with company and list of products pair**
# python
all_products = ['iPhone', 'Mac', 'Gmail', 'Maps', 'iWatch', 'Windows',
                'iOS', 'Google Drive', 'One Drive']
# Pre-defined products for different companies
apple_products = {'iPhone', 'Mac', 'iWatch'}
google_products = {'Gmail', 'Maps', 'Google Drive'}
msft_products = {'Windows', 'One Drive'}
from collections import defaultdict
d = defaultdict(list)

for product in all_products:
    if product in apple_products:
        d["apple_products"] += [product]
    elif product in google_products:
        d["google_products"] += [product]
    elif product in msft_products:
        d["msft_products"] += [product]

# print(d)

# **77 Write a program to rotate items of the list**
names = ["apple", "google", "yahoo", "gmail", "facebook", "flipkart", "amazon"]
# >>> _rotate(names, 1)
def _rotate(some_list,no_of_rotation):
    for _ in range(no_of_rotation):
        value = some_list.pop()
        some_list.insert(0,value)
    return some_list

# print(_rotate(names,2))

# >>> ['amazon', 'apple', 'google', 'yahoo', 'gmail', 'facebook', 'flipkart']
# >>>
# >>> _rotate(names, 2)
# >>> ['flipkart', 'amazon', 'apple', 'google', 'yahoo', 'gmail', 'facebook']
#
#################################################################################################
# **78 Write a program to rotate characters in a string**
# >>> rotate_string("helloworld", 1)
# >>> dhelloworl
# >>> rotate_string("helloworld", 1)
# >>> ldhellowor

word = "helloworld"

def rotate_(some_string,no_rotation):
    word_list = list(some_string)
    for _ in range(no_rotation):
        value = word_list.pop()
        word_list.insert(0,value)
    return "".join(word_list)

# print(rotate_(word,2))

# ```python
# # Rotating words in a sentence
# sentence = "Hello world welcome to python"
# >>> rotate(words, 1)
# >>> python Hello world welcome to
# >>> rotate(words, 2)
# >>> to python Hello world welcome
sentence = "Hello world welcome to python"
def _rotate(some_string,rotations):
    s_list = sentence.split()
    for _ in range(rotations):
        value = s_list.pop()
        s_list.insert(0,value)
    return " ".join(s_list)
# print(_rotate(sentence,4))

# **79 Write a program to count the number of white spaces in a given string**
sentence = "Hello world welcome to Python Hi  How are you. Hi how are you"
count = 0
for char in sentence:
    if char == " ":
        count+=1

# s = sentence.count(" ")
# print(s)

# from re import  findall
# print(len(findall(r"\s",sentence)))
# print(count)
###################################################################################
# **80 Write a program to print only non-repeated characters in a string**
s = 'helloworld'
# for letter in s:
#     if s.count(letter) ==1:
#         print(letter)
########################################################################################
# **81 What is the difference between a list and a tuple**
# ```python
# """
# 1. The main difference between a list and a tuple is that list's are mutable and tuples are immutable.
# 2. Python over allocates memory for lists. The reason for over allocation of memory is to support append operation.
# Where as in tuples, memory is not over allocated, as tuples does not support append operation.
# (Since tuples are immutable, it does not support append operation).
# 3. Tuples are more memory efficient than lists. (because in tuples no extra memory is allocated. It is fixed).
# 4. Tuples are negligibly faster than lists.
# """
# ```
# **82 Write a program to print all the consonants in a given string**
# >>> s = 'helloworld'
#
# **83 Write a program to count the number of commented lines in a text file**
with open("text1.txt") as file:
    count = 0
    for line in file:
        if line.startswith("#"):
            count +=1
# print(count)
#
# **84 Write a program to check if the year is leap year or not**
def is_leapyear(year):
    if year % 4 == 0 and year % 100 != 0:
        print("it is a leap year")
    elif year % 400 == 0:
        print("it is a leap year")
    else:
        print("it is not a leap year")

# print(is_leapyear(1900))
# **85 Liner Search**
#
#
# **86 Difference between xrange and range**
# ```python
# """
# python2- xrange
# python3- range
#
# 1. xrange does not stop, start and step attributes. But range object has start, stop and step attributes.
#   Python-3
#   r = range(0, 10)
#   r.start
#   r.stop
#   r.step
#
#   r = xrange(0, 10)
#   In Python-2 The above attributes are not supported.
#
# 2. range Object supports slicing! But xrange does not support slicing
#
# 3. range object has __contains__ method implemented. So it supports membership testing.
#    But xrange does not implement __contains__ method.
#    So Python will iterate over each and every item in the range xrange object until it finds a match.
#    (So if you are searching for a number in range is faster than xrange)
#
# 4. range will accept integer of any size. But xrange objects accepts integer size equivalent to C long!
# """
# ```
# **87 Write a program to count no of capital letters in a string**
sentence = "Hi How are You WelCome to PytHon"
count = 0
for letter in sentence:
    if ord("A") <= ord(letter) <= ord("Z"):
        count  += 1
# print(count)

# for i in range(0,len(a),2):
#     print(a[i:i+2])

# **90 Write a program to check if the elements in the second list is series of continuation of the items in the first list**
a = [10, 12, 14, 16, 18]
b = [20, 22, 24, 26, 28]

difference = a[1]-a[0]
c = a + b

for i in range(len(c)-1):
    if c[i] + difference == c[i+1]:
        pass
    else:
        print("it is not a series")


# a = [0, 5, 10, 15]
# b = [20, 25, 30, 35, 40]
#
# x = [10, 20, 30, 40]
# y = [50, 40, 60, 70]
# **91 What is the difference between append() and extend() method in list**
#
# ```python
# """
# 1. append() method appends one item at the end of the list.
# 2. extend() method appends all the items of the iterable to the end of the list.
# 3. Both append() and extend() method's mutates the existing list.
#
# e.g.
# >>> a = [1, 2, 3]
# >>> b = (4, 5, 6)
# >>> a.extend(b)
# >>> a
# [1, 2, 3, 4, 5, 6]
#
# >>> c = {7, 8, 9}
# >>> a.extend(c)
# >>> a
# [1, 2, 3, 4, 5, 6, 8, 9, 7]
#
# >>> d = {'a': 1, 'b': 2, 'c': 3}
# >>> a.extend(d)
# >>> a
# [1, 2, 3, 4, 5, 6, 8, 9, 7, 'a', 'b', 'c']
#
# The list "a" is getting mutated each time when it is extended.
# """
# ```
# **92 Write a program to find the first repeating character in a string**
s = 'helloworld'
# for item in s:
#     if s.count(item) > 1:
#         print(item)
#         break

################################################################################################################
# **93 Write a program to find the index of nth occurrence of a sub-string in a string**
# ```python
sentence = "hello world welcome to python hello hi how are you hello there"
import re
def nth_occurances(pattern,n):
    matches = re.finditer(pattern,sentence,n)

    res = list(matches)[n-1]
    # print(res.start(),res.end())

    # for match in matches:
    #     print(match.start(),match.end())

nth_occurances("hello",2)
##############################################################################
# **94 Write a program to print prime numbers from 1 to 50**
# for num in range(51):
#     count = 0
#     for i in range(1,num +1):
#         if num % i ==0:
#             count += 1
#     if count ==2:
#         print(num)

# **95 Write a program to sort a list which has mix of both odd and
# even numbers, the sorted list should have odd numbers first
# and then even numbers in sorted order**
a = [3, 4, 1, 7, 2, 12, 8, 6, 9, 11]
odd = []
even = []
for item in a:
    if item % 2 == 1:
        odd.append(item)
    else:
        even.append(item)

# print(sorted(odd) + sorted(even))

# **96 Write a program to sort a list which has mix of both
# odd and even numbers, in the sorted list,
# odd numbers should be in ascending order and even
# numbers should be in descending order**
a = [3, 4, 1, 7, 2, 12, 8, 6, 9, 11]
odd = []
even = []
for item in a:
    if item % 2 == 1:
        odd.append(item)
    else:
        even.append(item)
# print(sorted(odd) + sorted(even,reverse=True))

# **97 Write a program to count the number of occurrences
# of non-special characters in a given string**
s = 'hello@world! welcome!!! Python$ hi how are you & where are you?'
count = 0
for char in s:
    if char.isalpha() or char.isdigit():
        count +=1
# print(count)


# **98 Grouping Flowers and Animals in the below list**
items = ['lotus-flower', 'lilly-flower', 'cat-animal', 'sunflower-flower', 'dog-animal']

d = {}
for item in items:
    pair = item.split("-")
    if pair[1] not in d:
        d[pair[1]] = pair[0] + " "
    else:
        d[pair[1]] += pair[0] + " "

# print(d)
# **99 Grouping files with same extensions**
files = ['apple.txt', 'yahoo.pdf', 'gmail.pdf', 'google.txt', 'amazon.pdf', 'facebook.txt', 'flipkart.pdf']
d={}
for file in files:
    pair = file.split(".")
    if pair[1] not in d:
        d[pair[1]] = pair[0] + " "
    else:
        d[pair[1]] +=  pair[0] + " "
# print(d)
##########################################################################################################
# **100 Filter only those characters except digits**
s = '@hello12world34welcome!123'
# for item in s:
#     if item.isdigit():
#         pass
#     else:
#         print(item)
################################################################################
# **101 Count number of words in a sentence. ignore special characters.**
import re
sentence = "Hi there! How are you:) How are you doing today!"
res = re.findall(r'[a-zA-Z0-9]+',sentence)
d = {}
for word in res:
    if word not in d:
        d[word] = res.count(word)
# print(d)


# **102 Grouping even and odd numbers**
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd = [num for num in numbers if num % 2 ==1]
even = [num for num in numbers if num % 2 ==0]
# print(odd)
# print(even)
# **103 Find all max numbers from the below list**
numbers = [1, 2, 3, 0, 4, 3, 2, 4, 2, 1, 0, 4]
# max_ = numbers[0]
# for num in numbers:
#     if num > max_:
#         max_ = num
# for item in numbers:
#     if item == max_:
#         print(item)
#######################################################################################

# **104 Find all max length words from the below sentence**
sentence = "hello world hi apple you yahoo to you"
s_list = sentence.split()
max_len = max(s_list,key=len)

# for word in s_list:
#     if len(word) == len(max_len):
#         print(word)
######################################################################
# **105 Find the range from the following string**
sentence = '0-0, 4-8, 20-20, 43-45'
# Output Should be [0, 4, 5, 6, 7, 8, 20, 43, 44, 45, 46]
ranges = sentence.split(",")
res = []
for item in ranges:
    start,end = item.split("-")
    nums=range(int(start),int(end) + 1)
    res += list(nums)
# print(res)
########################################################################
# **106 Can we override a static method in python?**
# class Parent:
#     @staticmethod
#     def demo():
#         print('Running demo in Parent')
#
# class Child(Parent):
#     @staticmethod
#     def demo():
#         print('Running demo in Child')
############################################################################
# **107 Write a function which returns the sum of lengths of all the iterables**
#
# def total_length(*some_iter):
#     count = 0
#     for item in some_iter:
#         count +=  len(item)
#     return count
#
# print(total_length([1, 2, 3], (4, 5)))
# # 5
# print(total_length([1, 2, 3], (4, 5), ['apple', 'google', 'yahoo', 'gmail', 'flipkart']))
# # 10
# print(total_length([1, 2, 3], (4, 5), ['apple', 'google', 'yahoo', 'gmail', 'flipkart'], {1, 2, 3}))
# # 13
# print(total_length([1, 2, 3], (4, 5), ['apple', 'google', 'yahoo', 'gmail', 'flipkart'], {1, 2, 3}, {'a': 1, 'b': 2}))
# 15
# ```
# **108 Replace whitespaces with newline character in the below string**
sentence = "Hello world welcome to python"
for char in sentence:
    if char == " ":
        res =sentence.replace(char,"\n")
# print(res)

# **109 Replace all vowels with "*"**
sentence = "hello world welcome to python"
for char in sentence:
    if char in "aeiou":
        res = sentence.replace(char,"*")
# print(res)
# **110 Replace all occurrences of "Java" with "Python" in a file**
#updating in new file
with open("text1.txt") as file1:
    with open("text2.txt","w") as file2:
        for line in file1:
            replaced = line.replace("java","python")
            file2.write(replaced)
#updating in same file

with open("text1.txt", "r+") as file:
    new_list = []
    for line in file:
        replaced = line.replace("java", "python")
        new_list.append(replaced)

    file.seek(0)
    file.writelines(new_list)





# **111 Maximum sum of 3 numbers and Minimum sum of 3 numbers**
numbers = [10, 15, 20, 25, 30, 35, 40, 15, 15]

numbers_sorted = sorted(numbers)
# print(sum(numbers_sorted[:3]))
# print(sum(numbers_sorted[-3:]))




# **112 Write a program to get the output as below**
a = "python@#$%pool"
# # o/p should be ['PYTHON', 'POOL']
res = ""
for item in a:
    if item.isalpha():
        res = res + item
    else:
        res = res + " "
res_list = []
res_ = res.split()
for item in res_:
    res_list.append(item.upper())
# print(res_list)


# **113 Write a program to print all the number which are ending with 5**
numbers = ['1', '12', '123', '12345', '125', '905', '55', '5', '95655', '55555']
# for num in numbers:
#     if num[-1] == '5':
#         print(num)
# **114 Write a program to get the indexes of each item in the below list**
names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'google', 'gmail', 'gmail', 'gmail']
d = {}
for index,name in enumerate(names):
    if name not in d:
        d[name] = [str(index)]
    else:
        d[name] += [str(index)]
# print(d)

# output should be -  {'apple': [0, 2], 'google': [1, 5], 'yahoo': [3, 4], 'gmail': [6, 7, 8]}
#
# **115 Write a program to print "Bangalore" 10 times without using "for" loop**
# print("Bangalore\n" * 10)
##################################################################################
# **116 Write a program to print all the words which starts with letter 'h' in the given string**
string = 'hello world hi hello universe how are you happy birthday'
from re import findall
res = findall(f"[a-z]+",string)
# print(res)

# string_list = string.split()
# for item in string_list:
#     if item[0] == "h":
#         print(item)
#####################################################################################################################

# **117 Write a program to sum all even numbers in the given string**
sentence = 'hello 123 world 567 welcome to 9724 python'
# res = findall(f"[0-9]",sentence)
# total = 0
# for num in res:
#     if int(num) % 2 == 0:
#         total += int(num)
# print(total)


# **118 Write a program to add each number in word1 to number in word2**
# e.g. 1 + 5, 2 + 6, 3 + 7, 4 + 8, 5 + 9
# word1 = 'hello 1 2 3 4 5'
# word2 = 'world 5 6 7 8 9'
# for w1,w2 in zip(word1,word2):
#     if w1.isdigit() and w2.isdigit():
#         print(int(w1) + int(w2))

################################################################################################################
# **119 Write a program to filter out even and odd numbers in the given string**
sentence = 'hello 123 world 456 welcome to python498675634'
res = findall(r"[0-9]" , sentence)
new_res = []
for item in res:
    new_res.append(int(item))

even = [i for i in new_res if i % 2 == 0]
odd = [i for i in new_res if i % 2 == 1]
# print(even)
# print(odd)
#########################################################################################
# **120 Write a program to print all the number which are starting with 8**
numbers = ['857', '987', '8', '120', '888888', '547', '7674', '89', '589', '388888', '2889']
# for num in numbers:
#     if num[0] == "8":
#         print(num)
######################################################################################################################
# **121 Write a program to remove duplicates from the list without using set or empty list**
l1 = [1, 2, 3, 4, 1, 2, 3, 4, 3, 4, 4]
# new_l = []
# for item in l1:
#     if item not in new_l:
#         new_l.append(item)
# print(new_l)
#######################################################################################################
# **122 Print all the missing numbers from 1 to 10 in the below list**
# numbers = [1, 3, 6, 8, 10]
# for i in range(1,11):
#     if i not in numbers:
#             print(i)

####################################################################################################
# **123 Write a python program to get the below output**
l1 = [1, 2, 3]
l2 = ['a', 'b', 'c']
# >>> # o/p ['1a', '1b', '1c', '2a', '2b', '2c', '3a', '3b', '3c']
res_list = []
for num in l1:
    for letter in l2:
        res = str(num) + letter
        res_list.append(res)
# print(res_list)


###################################################################################################
# **124 Write a python program to get the below output**
word = "AAAAaaccYYY"
# >>> # o/p ['A4', 'a2', c2', Y3']
res = []
for w in set(word):
    count_ = word.count(w)
    res.append(w + str(count_))
# print(res)
######################################################################################################
# **125 What is the output of the below function call**
# class Demo:
#     def greet(self):
#         print("hello world")
#
#     def greet(self):
#         print("hello universe")
# o/p "hello universe"
#################################################################################################
# **126 In the list below, find all the number pairs which results in 10 either when added or subtracted**
a = [3, 5, -4, 8, 11, 1, -1, 6]
# for i in range(len(a)):
#     for j in range(i+1, len(a)):
#         if a[i] + a[j] == 10 or a[i] - a[j] == 10:
#             print(a[i],a[j])

#############################################################################################################
# **127 Write a decorator to prefix +91 to the original phone numbers**
# numbers = [1234567890, 123456790, 1234567890]
############################################################################################################
# **128 Write a program to get the below output**
d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
# >>> # o/p should be ['b', 'd']
res = []
for key,value in d.items():
    if value % 2 == 0:
        res.append(key)
# print(res)
#############################################################################################################
# **129 Can we have multiple __init__ methods in a class**
# ```python
# class Point:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
# yes,it will be overridden
################################################################################################
# **130 Why python is Object Oriented**
# ```python
# 	Python is object oriented because everything in python is an object (defined as class)
# ```
# **131 What are .pyc files**
# ```python
# 1. pyc files are python compiled.
# 2. Once .py file is compiled by python compiler, it generates .pyc file.
# 3. .pyc files contains byte code which is understandable by python virtual machine.
# 4. pyc files are generated when a python module is imported.
# 5. Python compiler will not compile a python module again and again unless there is a change in code.
# 6. This makes programs to run faster since byte code for a module is already generated.
# ```
###################################################################################################################
# **132 Reverse a list without using any built-in functions and slicing**
res = []
a = [1, 2, 3, 4, 5]
for item in a:
    res = [item] + res
# print(res)
##################################################################################################################
# **133 Write a program to get the below output**
a= "10.20.30.40"
# >>> # o/p = "40.30.20.10"
a_list = a.split(".")
res = []
for item in a_list:
    res = [item] + res
# print(".".join(res))
########################################################################################################################

# **134 What is the difference between while loop and for loop.**
# ```python
# The body of while loop gets executed until some condition is True.
# Once the condition if False, the control comes out of the while loop.
#
# The body of for loop get executed for some fixed number of iterations.
# ```
#########################################################################################################################
# **135 What are magic methods?**
# ```python
# Magic methods are special methods which starts and ends with double underscores.(they are also called as dunders)
# Magic methods are internally called by python. We can customize the behaviour of an object or class using magic methods.
# They are also called as protocols.
#
# e.g. when you ask for the length of the list len(names) internally python will call __len__ method on list object.
#
# e.g. when you check for membership "apple" in names python internally triggers __contains__("apple")
######################################################################################################################
# **136 Swap two variables without using 3rd variable in python.**
a=10
b=20
a,b=b,a
# print(a)
# print(b)
###################################################################################################################
# **137 What is pylint.**
# ```python
# Pylint is a plugin or extension that checks for syntax errors.
# Also, it tries to enforce coding standards according to PEP8 style guide.
# It can give recommendations/suggestions/hints about types.
###############################################################################################################
# **138 What is the output of the below program.**
# print([1, 2, 3, 4] * 2)
##################################################################################################################
# **139 What is the difference between the is and == operators**
# ```python
# "==" operator checks if both objects have same value.
# "is" operator checks if identity or memory address of two objects are same.
####################################################################################################################
# **140 What is "self" in class.**
# "self" is called as Instance or data.
# Every instance method of a class has "self" as first argument.
# During runtime, "self" will be replaced with object instance of the class.
# e.g.
# class Point:
#    def __init__(self, a, b):
#        self.a = a
#        self.b = b
#
# p1 = Point(1, 2)
# p2 = Point(3, 4)
#
# when you say, p1.a, "self" will be replaced with p1 and when you say p2.a, "self" will be replaced with p2.
# Internally p1 and p2 will be pointing to a dictionary which is also called instance dictionary.
# the instance dicitonary canbe accessed via __dict__ attribute.
# e.g. p1.__dict__ , p2.__dict__
#######################################################################################################################
# **141 What is assert statement. What is the difference between assert and if/else statement.**
# 1. An assert statement is used to validate the actual result against expected result.
# 2. If the actual result does not match with the expected result, AssertionError is raised.
# 3. if/else is not used for validating the actual result against expected result.
# 4. if/else statement will not raise any exception.
#########################################################################################################################
# **142 What is the difference between a module, a package, and a library**
#
# 1. A module is simply a Python file that’s intended to be imported into scripts or other modules.
# It contains functions, classes, and global variables.
#
# 2. A package is a collection of modules that are grouped together inside a folder to provide consistent functionality. Packages can be imported just like modules. They usually have an __init__.py file in them.
#
# 3. A library is a collection of packages.
####################################################################################################################################################
######################################################################################################################
# **144 write a program to get the below output**
items = ['$123.45', '$434.23', '$567.89']
# >>> # o/p [123.45, 434.23, 567.89]
res = []
for item in items:
    i = float(item.replace("$",""))
    res.append(i)
# print(res)
######################################################################################################################
# **145 Generator function for Fibonacci series program**


######################################################################################################################
# **146 Write a program to print common character present in all the items of the below list**
items = [ "glory", "glass", "sight", "fight"]
res = []
common_chars = []
for item in items[0]:
    for char in items[1:]:
        if item not in char:
            break
    else:
        res.append(item)
# print(res)

######################################################################################################################
# **147 Function should accept a list and if any number divisible by 3 then modify to 33 or else keep it as it is**

def some_func(some_list):
    res = []
    for item in some_list:
        if item % 3==0:
            res = res + [33]
        else:
            res += [item]
    return res

# print(some_func([1,3,4,5,23,89,9]))
###################################################################################################################
# **149 write a program to map digits to its corresponding word**
d = {   "0": "ZERO", "1": "ONE", "2": "TWO", "3": "THREE", "4": "FOUR",
         "5": "FIVE", "6": "SIX", "7": "SEVEN", "8": "EIGHT", "9": "NINE"
     }
def find_num(number):
    for num in str(number):
        return(d[num])

# print(find_num(8))
###########################################################################################################################

# **150 validate if the list contains odd number at the beginning (0th index) and even numbers there after from 1st till end of the list**
# numbers = [1, 2, 4, 8, 6, 12] ----> the function should return True
# numbers = [1, 2, 4, 7, 6, 12] ----> the function should return False
# numbers = [2, 2, 4, 8, 6, 12] ----> the function should return False

def verify_odd_even(some_list):
    first_no = some_list[0]
    is_odd = (first_no % 2 == 1)

    is_even = True
    for num in some_list[1:]:
        if num % 2 != 0:
            is_even = False
            break

    return is_odd and is_even


# print(verify_odd_even([1,2,4,8,6,12]))

######################################################################################################################
# **151 sort the list of names based on lastname or first character of the lastname**
# ```python
names = ['steve jobs', 'bill gates', 'john doe', 'tim cook', 'laura turner', 'alex martin']
def sort_last_name(some_list):
    fname,lname = some_list.split()
    return lname

res = sorted(names,key=sort_last_name)
# print(res)
###############################################################################################################################################
# **152 get all the pairs whose sum is 8**
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for item in a:
#     for num in a:
#         if item + num ==8:
#             print(item,num)
######################################################################################
# **153 write unique characters to the file**
word = "aaabbbccc"
w = set(word)
with open("text3.txt", "w") as file:
    # file.writelines(w)
    for char in w:
        file.write(char + "\n")

###################################################################################################
# **154 extract characters at even indexes of the string**
items = (1, 2, 3, "bangalore", "mumbai")
# for item in items:
#     if isinstance(item,str):
#         print(item[::2])
######################################################################################################
# **155 Comparing two versions of the software**
# ```python
# from packaging.version import Version
# # packaing is a standard library
#
# a = "1.3.4"
# b = "2.4.5"
#
# v1 = Version(a)
# v2 = Version(b)
#
# v1 < v2     # returns True
# v1 > v2     # returns False
# v1 == v2    # returns False
# ###########################################################################################################################
# **156 Comparing two employee objects**
# ```python
# class Employee:
#     def __init__(self, name, experience):
#         self.name = name
#         self.experience = experience
#
# e1 = Employee('alex', 5)
# e2 = Employee('brain', 1)
###############################################################################################################################
# **157 Replace characters at odd index by 'x'**
# word = "example"
# for index,item in enumerate(word):
#     if index % 2 ==1:
#         res = word.replace(item,"x")
# print(res)


# **158 If the number is divisible by 2 it should print 'hi' if the no is divisible by 3 it should print 'hello' if the number is divisible
# by both 2 and 3 it should print 'bye'. using list comprehension**
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in numbers:
#     if num % 2 == 0:
#         print("hi")
#     elif num % 3 == 0:
#         print("hello")
#     else:
#         print("bye")

###########################################################################################################################
# **159 write a program to get the below output**
states = {'mysore':'karnataka','Bangalore':'karnataka','chennai':'TN','pune':'maharastra','coimbatore': 'TN'}
# # o/p {'karnataka': ['mysore', 'Bangalore'], 'TN': ['chennai', 'coimbatore'], 'maharastra': ['pune']}
d = {}
# for city,state in states.items():
#     if state not in d:
#         d[state] = city + " "
#     else:
#         d[state] += city + " "
# print(d)

##########################################################################################################
# **160 write a program to get the below output**
l1 = ['m', 'na', 'i', 'pyt']
l2 = ['y', 'me', 's', 'hon']
# >>> # o/p ['my', 'name', 'is', 'python']
# output = []
# for i,j in zip(l1,l2):
#     res = (i+j)
#     output.append(res)
# print(output)

#########################################################################################################
# **161 write a program to get the below output**
input={1:'a',2:'b',3:'c'}
# >>> output = {'a': 1, 'b': 2, 'c': 3}
d = {}
for key,value in input.items():
    if value not in d:
        d[value] = key
# print(d)
########################################################################################################
# **162 write a program to get the below output**
names = ['bangalore', 'chennai', 'mumbai', 'delhi']
# >>> ['ore', 'nai', 'bai', 'lhi']
# for name in names:
#     print(name[-3:])
###############################################################################################################
# **163 write a program to sort the given collection that contains uppercase, lowercase numeric and special
# character based on ASCII value**
items = ['a', 'b', 'C', 'D', 1, 8, '!']
def ascii_(item):
        return ord(str(item))

res = sorted(items,key=ascii_)
# print(res)
############################################################################################################
# **21 Write a class named Simple and it should have iteration capability.**

# **22 Write a Custom class which can access the values of dictionaries using d['a'] and d.a**# **21 Write a class named Simple and it
# have iteration capability.**




############################################################################################################################