# numbers = [1, 2, 3, 4, 5]
#
# squares = []
#
# for num in numbers:
#     squares.append(num ** 2)
#
# print(squares)

# even_no = []
# for even in range(2,50):
#     if even % 2 == 0:
#         even_no.append(even)
# print(even_no)


# evens=[i for i in range(1,11) if i%2==0]
# print(evens)
#################################################################################
#####converting into negative no

# number=[1,2,3,4,5,6]
#
# neg_no = [num*-1 for num in number]
# print(neg_no)


######################################################################################
#seperate the names that starts with vowels

names = ["adam", "oampa", "ricky", "brian", "lara", "chris", "gayle"]
# vowels = []
# for name in names:
#     if name[0] not in "aeiou":
#         vowels.append(name)
#
# print(vowels)

# vowels = [name for name in names if name[0] in "aeiou"]
# print(vowels)


##############################################################################################3
#filter out those languages that are starting with p

# languages=["java","python","perl","php","python","cobra","js","nodejs","ruby","python"]
# repeated_lang = []
# for lang in languages:
#     if languages.count(lang) > 1:
#         repeated_lang.append(lang)
# print(repeated_lang)

# repeated_=[ lan for lan in languages if languages.count(lan)>1]
# print(repeated_)

#################################################################################################
#separate the languages tha starts with p
languages=["java","python","perl","php","python","cobra","js","nodejs","ruby","python"]
# repeated_p=[]
# for lan in languages:
#     if lan[0]=="p":
#         repeated_p.append(lan)
# print(repeated_p)

# repeated=[lang for lang in languages if lang[0]=="p"]
# print(repeated)

# repeated=[lang for lang in languages if lang.startswith("p")]
# print(repeated)

#########################################################################################################
# names = ["apple", "google", "facebook", "twitter", "videocon", "instagram", "dell", "hp"]
# _names = []
# for name in names:
#     if len(name) > 6:
#         _names.append(name)
# print(_names)
#
#
# names_=[name for name in names if len(name)>6]
# print(names_)

#####################################################################################################################
#filter out name that starts with consonants
# names = ["laura", "adams", "joe", "james", "scott", "alex","ive", "bill", "chris", "gayle"]
# name_=[]
# for name in names:
#     if name[0] not in "aeiou":
#         name_.append(name)
# print(name_)


full_names = ["steve job", "bill gates", "harry potter", "akash bhadra"]
# first=[]
# last=[]
# for name in full_names:
#     result=name.split()
#     first.append(result[0])
#     last.append(result[1])
#
# print(f"the first name is {first}")
# print(f"the last name is {last}")


# first_names=[name.split()[0] for name in full_names]
# last_names=[name.split()[1] for name in full_names]
#
# print(first_names)
# print(last_names)
##########################################################################################3


# names = ["apple", "google", "facebook", "twitter", "videocon", "instagram", "dell", "hp"]
# name_len=[]
# for name in names:
#     name_len.append((name,len(name)))
#
# # print(name_len)
#
# name_=[((name,len(name)))for name in names]
# print(name_)

##########################################################################################################


# companies = ["facebook", "twitter", "whatsapp", "gmail", "instagram", "meta", "zomato"]
#
# # company = []
# #
# # for comp in companies:
# #     company.append((comp,len(comp)))
# # print(company)
#
# company_=[(comp,len(comp)) for comp in companies]
# print(company_)


#############################################################################################################

# from math import factorial
# factor = []
# numbers = [1, 2, 3, 4, 5]
# for number in numbers:
#     factor.append(factorial(number))
# # print(factor)
#
#
# factor_ = [factorial(num) for num in numbers]
#
# print(factor_)

# names = ["apple", "google", "facebook", "twitter", "videocon", "instagram", "dell", "hp"]
# # name_ = []
# # for name in names:
# #     if len(name) % 2== 1:
# #         name_.append(name[::-1])
# #     else:
# #         name_.append(name)
# #
# # print(name_)
#
# names_=[name[::-1] if len(name) % 2 ==1 else name  for name in names ]
# print(names_)


# data = ["swiggy", 14, 1.9, True, "python"]
#
# data_= []
# for d in data:
#     if isinstance(d, str):
#         data_.append(d[::-1])
#     else:
#         data_.append(d)
# # print(data_)
#
#
# data_rev=[d[::-1] if isinstance(d, str) else d for d in data]
# print(data_rev)
###################################################################################
# a = [1,2,3,4,]
# b = [6,7,8,9,]
# sum = []
# for n1,n2 in zip(a,b):
#     sum.append(n1+n2)
# # print(sum)
#
# sum_ = [n1+n2 for n1,n2 in zip(a,b)]
# print(sum_)

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# single_list = []
# for mat in matrix:
#     for i in mat:
#         single_list.append(i)
# # print(single_list)
#
# single = [i for mat in matrix for i in mat]
# print(single)


# letters = "ABCDEFGH"
# numbers = [0, 1, 2, 3, 4, 5, 6, 7]
#
#
# new_list = []
# for n1,n2 in zip(letters,numbers):
#     new_list.append((n1,n2))
# print(new_list)































