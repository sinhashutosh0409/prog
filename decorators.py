# print the function's name
def positive_value(some_func):
    def wrapper(*args,**kwargs):
        print(f"{some_func.__name__} is called")
        return some_func(*args,**kwargs)
    return wrapper


@positive_value
def add(a,b):
    return a+b

@positive_value
def sub(a,b):
    return a-b

########################################################################################################################
# check if the result is an integer or not
def checking_integer(some_func):
    def wrapper(*args,**kwargs):
        res = some_func(*args,**kwargs)
        if isinstance(res,int):
            return f"the {res} is integer"
        else:
            return f"the {res} is not integer"
    return wrapper

@checking_integer
def add(a,b):
    return a+b

@checking_integer
def sub(a,b):
    return a-b
# print(sub(10,20))
# print(add(10,5))


###############################################################################################################
from time import sleep, time


def delay(some_func):
    def wrapper(*args):
        print("the function is sleeping for 2 seconds ")
        sleep(2)
        res = some_func(*args)
        return res
    return wrapper
@delay
def add(a,b):
    return a+b
@delay
def sub(a,b):
    return a-b
@delay
def mul(a,b,c):
    return a*b*c

# print(add(10,5))
# print(sub(10,5))
# print(mul(10,5,1))

##############################################################################################################################
# **18 write a decorator that returns only positive values of
# subtraction**
def only_positive_res(some_func):
    def wrapper(*args):
        res = some_func(*args)
        return abs(res)
    return wrapper
@only_positive_res
def subtrct(a,b):
    return a-b

# print(subtrct(10,29))

###########################################################################################################
# **127 Write a decorator to prefix +91 to the original phone numbers**
phone_numbers=([1234567890, 123456790, 1234567890])

# def outer(some_func):
#     def inner(*args):
#         update=["+91-"+str(num) for num in args]
#         return some_func(update)
#     return inner
#
# @outer
# def prefix(*args):
#     for n in args:
#         print(n)
#
#
#
# prefix(*phone_numbers)




###########################################################################################################
def outer(some_func):
    def inner(a,b):
        if a < b:
            a, b = b, a
            res = some_func(a,b)
            return res
    return inner


@outer
def divi_(a,b):
    return a/b
@outer
def subs_(a,b):
    return a-b

# print(divi_(10,20))
# print(subs_(10,20))
################################################################################################################3

phone_numbers = [1234567890, 123456790, 1234567890]

def outer(some_func):
    def inner(*args):
        [no] = args
        upd_no = ["+91-" + str(num) for num in no]
        return some_func(upd_no)
    return inner
@outer
def add_91(*args):
    for num in args:
        return num

# print(add_91(phone_numbers))
####################################################################################################################

# delay of n seconds

from time import sleep
import time

def delay(n):
    def outer(some_func):
        def inner(*args):
            time.sleep(2)
            some_func(*args)
        return inner
    return delay
@delay(2)
def add(*args):
    return "hello"

print(add())









