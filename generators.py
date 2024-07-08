#
#
#
# def gen_():
#     print("hello")
#     yield
#     print("uuuuu")
#     yield 2
#     print("uuuuu")
# res = gen_()

# print(next(res))
# print("_________")
# print(next(res))
# print("________")
# print(next(res))
# print(list(res))
# for i in res:
    # print(i)


#################################################################
###generate all even no from 1 to 10

def even_no(n):
    for i in range(1,n+1):
        if i%2 ==0:
            yield i

res = even_no(10)

# print(next(res))
#########################################################
#######################################################################
# generate vowels in the sentence

sentence = "hello world"

def vowel_(some_string):
    for word in sentence:
        if word in "aeiouAEIOU":
            yield word
res = vowel_(sentence)
# print(next(res))
#
# print("hello")

res = vowel_(sentence)
# for i in res:
    # print(i)
###################################################################################################################
# generate character and its occurrence pairs
character = "hello python"

def char_count_pair(some_string):
    for char in character:
        yield char,character.count(char)

res = char_count_pair(character)

# print(dict(res))

######################################################################################################################
# generate only even length names

names = ["mark", "henry", "harry", "mitchell", "nelson"]

# def name_len(some_thing):
#     for name in names:
#         if len(name)%2 ==0:
#             yield name
#
# res= name_len(names)
# # print(list(res))
# print(next(res))
#
# print("*" * 30)
# res= name_len(names)
# for i in res:
#     print(i)

####################################################################################################################

# generate names starting with vowels and their length

names = ["mark", "henry", "mitchell", "aditya", "eagle", "utsav"]

def vowel_names(some_string):
    for name in names:
        if name[0] in "aeiouAEIOU":
            yield name,len(name)

res = vowel_names(names)

# print(next(res))
# print(next(res))
# print(next(res))
# print("*" * 30)
# res = vowel_names(names)
# for i in res:
#     print(i)

################################################################################################################
# generate name and len pair
names = ["mark", "henry", "harry", "mitchell", "nelson"]

def name_len_(some_thing):
    for name in names:
        yield name,len(name)


res = name_len_(names)

# for i in res:
#     print(i)

##########################################################################################
# generator to reverse the item of a list if the item is of odd length string
names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']

def reverse_odd_len(some_thing):
    for name in names:
        if len(name)%2==1:
            yield name[::-1],len(name)

res = reverse_odd_len(names)

# for i in res:
#     print(i)

############################################################################################################
# generator to countdown the numbers from 10 to 1

def countdown():
    for i in range(10,0,-1):
        yield i
res = countdown()
# print(list(res))

##################################################################################################
# yield only the words which has even length
sentence = "python is a programming language"

words = sentence.split()

def word_even_len(some_word):
    for word in words:
        if len(word)%2 == 0:
            yield word
res = word_even_len(words)

# print(list(res))

######################################################################################################################
# yield name as it is if it is a palindrome else reverse it
names = ["steve", "John", "alex", "lara", "eve"]

def palindrome(some_names):
    for name in names:
        if name[::-1]==name:
            yield name

res = palindrome(names)

# print(list(res))

###################################################################################################################




















