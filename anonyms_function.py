# #1. write a lambda expression to check if a number is even
#
# # even = lambda num : num %2 ==0
# # print(even(1))
#
# #2  write a lambda expression to return last element of a sequence
# # a=[1,2,3,4,5]
# #
# # last_=lambda a:a[-1]
# # print(last_(a))
#
# ####################################################################
# # data = [(1, 2), (3, 4), (5, 6)]
# # add = lambda a,b:a+b
# # res = []
# # for a,b in data:
# #     res.append(add(a,b))
# # print(res)
#
# ##########################################################################
# # check for even in list of numbers
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
#
# is_even = lambda num :num **2 if num % 2 == 0 else None
#
# # # for num in numbers:
# # #     print(is_even(num),num)
# #
# # s_map = map(is_even,numbers)
# # print(list(s_map))
#
# ########################################################################################
# # square the numbers of the list using map class
# # numbers = [1,2,3,4,5,6]
# #
# # square = lambda num : num ** 2
# #
# # # for num in numbers:
# # #     print(square(num))
# #
# # map_ = map(square,numbers)
# # print(list(map_))
#
# #########################################################################
# # return the length of all values
#
# d = {"a": "apple", "b": "big basket"}
#
# # print(d.items())
# # def len_value(item):
# # 	return len(item[-1])
# # a = map(len_value,d.items())
# # print(list(a))
#
# ########################################################################################
# # squares of only even numbers
#
# # res = lambda num:num **2 if num%2 == 0 else None
# #
# # print(res(10))
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# res = lambda num:num ** 2 if num %2 ==0 else None
#
# # a=filter(res,numbers)
# # print(list(a))
#
#
#
# ###################################################################################################
# def even_odd(num):
# 	if num % 2 == 0:
# 		return "even"
# 	else:
# 		return "odd"
#
#
# numbers = [1, 2, 3, 4]
# a = map(even_odd,numbers)
# b = filter(even_odd,numbers)
#
# print(list(a))
# print(list(b))

#######################################################################################################################
#########################################################################################################################3

# a=(1,2,3,4,5,6)
#
# print(sorted(a,reverse=True))

# greet = "hello"
#
# b=sorted(greet,reverse=True)
# a="".join(b)
# print(a)

#####################################################################################
#sorting item of a list based on length
#
# names = {"rakesh":98, "raj":10, "sundar":16, "aakash":15, "anand":2}
#
# name_list = names.items()
#
# # def name_(n):
# # 	return n[1]
# a=lambda n: n[0]
#
# x=sorted(name_list,key=a)
# print(x)

###########################################################################

data = [(1,2),(3,4),(4,5)]
# new=[]
# for n1,n2 in data:
#     new.append(n1+n2)
# print(new)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

#     if num %2 ==0:
#         even_.append(num)
# print(even_)

is_even = lambda num :num%2 ==0

res = map(is_even,numbers)
# print(list(res))

##############################################################
numbers=[1,2,3,4,5,6]
# num=[]
# for n in numbers:
#     num.append(n**2)
# print(num)

# res=lambda num:num **2
# def square(num):
#     return num ** 2
# result = map(square,numbers)
# print(list(result))
#####################################################################

# names = {"a":"aakash","s":"sonu"}
#
# name_=names.items()
#
# def len_(item):
#     return len(item[1])
#
# res =map(len_,name_)
# print(list(res))


########################################################################################3
numbers = [1,2,3,4,5]
#
# def square_(item):
#     if item % 2== 0:
#         return item ** 2
res = lambda num:num**2 if num %2==0 else None

r = map(res,numbers)
# res1 = filter(square_,numbers)
#
print(list(r))
print(list(res1))














