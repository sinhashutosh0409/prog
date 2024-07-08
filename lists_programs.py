#1. Write program to merge two different lists

a = [1,2,3,4,5]
b = [6,7,8,9]

a.extend(b)
# print(a)




###########################################################################################
#2.# Write a program to replace all the characters with - if the character occurs more than once in a string**

greet = "hello python"
new_ = ""
for g in greet:
    if greet.count(g) >1 :
        new_ =  new_ + "_"

    else:
        new_ = new_ + g

# print(new_)

##################################################################################################
##3.# Write a python program to get the below output**
#type 1
sentence = "Hi How are you"
# o/p should be "iH woH era uoy"

sen_list = sentence.split()
_list = ""
for sen in sen_list:
    _list = _list + sen[::-1]+ " "
    # print(_list)

# print(_list)

# type 2
# sentence = "Hi How are you"
#
# s_list_ = sentence.split()
# new_ = []
#
# for s_ in s_list_:
#     new_.append(s_[::-1])
# # print(new_)
#
# _new_ = " ".join(new_)
# print(_new_)
################################################################################################################

#4 What is the output of the following**
a = [1, 2, 3]
b = [4, 5, 6]

# print([a, b]) #[[1, 2, 3], [4, 5, 6]]
# print((a,b))    #([1, 2, 3], [4, 5, 6])
# print([*a, *b])   #[1, 2, 3, 4, 5, 6]
# print((*a, *b))    #(1, 2, 3, 4, 5, 6)
# print({*a, *b})     #{1, 2, 3, 4, 5, 6}


###############################################################################################################
# 4 How to remove duplicates from the list without using inbuilt functions**
items = [1, 2, 3, 4, 1, 2, 3, 4, 5]

dup = []
for item in items:
    if item not in dup:
        dup.append(item)
# print(dup)

#############################################################
#5  #  write a program to get 1234**
t = ('1', '2', '3', '4')

numbers =int( "".join(t))
# print(numbers)

####################################################################################
#6 36 Sum all the numbers in the below string.**
# s = "Sony12India567Pvt2ltd"
# sum = 0
# for char in s:
#     if char.isdigit():
#         sum = sum+int(char)

# print(sum)

#########################################################################################################
# 7  **38 Print all the numbers in the below list**
# a = ['abc', '123', 'hello', '23', "12.5"]
#
#
# for num in a:
#     if num.isdigit():
        # print(num)

###############################################################################################
# 8  Program to print the number of occurrences of characters
# in a String without using inbuilt functions.**
# s = 'helloworld'
# d = {}
# for num in s:
#     d[num]=s.count(num)

# print(d)

##########################################################################################################3
#9  # #Program to print only the repeated characters and
# # count of the same.**
s = 'helloworld'
d = {}

for num in s:
    if s.count(num)>1:
        print(num,s.count(num))

















##########################################################################################








