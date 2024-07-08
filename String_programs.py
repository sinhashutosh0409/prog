#1. Write a program to find the length of the string without using inbuilt function (len)**

s = "hello world"
count = 0

for _ in s:
    count = count + 1
# print(count)

###################################################################################################
#2. Write a program to reverse a string without using any inbuilt functions.**
# Type1
s = "hello world"
rev = ""
for reverse in s:
    rev = reverse + rev
# print(rev)


# type2
# print(s[::-1])

#################################################################################################
#3.# Write a program to replace one string with another. e.g. "Hello World" replace "World" with "Universe".**
# type1
greeting = "hello world"
# print(greeting.replace("world","universe"))

# type2
words = greeting.split()
new = ""
for word in words:
    if word == "world":
        new = new + "universe"
    else:
        new = word + new + " "
# print(new)

##########################################################################################################
#4. How to convert a string to a list and vice-versa

greet = "hello world"
g = greet.split()
# print(g)

h = " , ".join(g)
# print(h)

##########################################################################################################
#5 Covert the string "Hello welcome to Python" to a comma separated string

greeting = "hello welcome to python world"

greet = ",".join(greeting)
# print(greet)

##############################################################################################################
# 6 Write a program to print alternate characters in a string

greeting = "hello python welcome to the world of humans"

greet_odd =greeting[::2] # odd
greet_even =greeting[1::2]#even

# print(greet_odd)
# print(greet_even)

#########################################################################################################
#7 Write a Program to print ascii values of the characters present in a string.

greet = "hello python"

for g in greet:
    a = ord(g)
    # print(g,a)

#############################################################################################################

#8 Write program to convert upper case to lower case and vice-versa without using inbuilt method.**

greet = "hello WORLD"
result = ""
for char in greet:
    if ord("a") <= ord(char) <= ord("z"):
        result = result + chr(ord(char) - 32)

    elif ord("A") <= ord(char) <= ord("Z"):
        result = result + chr(ord(char) + 32)

    else:
        result = result + char

# print(result)
###################################################################################################
# 9.Write program to swap two numbers without using 3rd variable
a=10
b=20
a,b = b,a
# print(a)
# print(b)

#10 Write a program to check if the given string is Palindrome or not without using reversed method

# name= "mmomm"
#
# if name[::-1]==name:
#     print("it is a palindrome")
# else:
#     print("it is not a palindrome")

##################################################################################################################

# 11 Write a program to search for a character in a given string and return the corresponding index.

greet = "hello"
char = "u"
for index,key in enumerate(greet):
    if key == char:
        print(f"the index of the char {key} is {index}")
else:
    print("the key is not found")










