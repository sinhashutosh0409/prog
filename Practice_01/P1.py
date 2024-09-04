#write a decorator to add dealy of 5 sec

from time import sleep
#
# def delay(some_func):
#     def wrapper(*args):
#         sleep(3)
#         return some_func(*args)
#     return wrapper
#
# @delay  # add=delay(add)
# def add(a,b):
#     return a+b
#
# def sub(a,b):
#     return a-b
#
# # print(delay(add))
# # print(add(10,5))
#
# ###################################################################################
# #write a decorator to give 3sec delay in function
#
# def delay(some_func):
#     def wrapper(*args):
#         sleep(3)
#         return some_func(*args)
#     return wrapper
# @delay
# def add(a,b):
#     return a+b
# @delay
# def sub(a,b):
#     print("Executing sub function")
#     return a-b
# # print(sub(20,10))
#
# #write a decorator for getting only positive output
#
# def only_positive(some_func):
#     def wrapper(*args):
#         return abs(some_func(*args))
#     return wrapper
# @only_positive
# def add(a,b):
#     return a+b
# @only_positive
# def sub(a,b):
#     return a-b
#
# # print(sub(20,30))
# ##Write a decorator to reverse the output
#
# def reverse(some_func):
#     def wrapper():
#         res = some_func()
#         return res[::-1]
#     return wrapper
# @reverse
# def greet():
#     return "hello"
#
# # print(greet())
# ###########################################################################
# #write a decorator to print the name of function which is called
#
# def name(some_func):
#     def wrapper():
#         print(f"executing {some_func.__name__} function")
#         return some_func()
#     return wrapper
# @name
# def greet():
#     return "good morning"
#
# # print(greet())
#
# ######################################################################################
# class Sample:
#     def __init__(self,a):
#         self.a = a
#
#     def spam(self):
#         return "hello"
#
# # print(vars(Sample))
# ################################################################################
# #adding a count attribute in all the classes
#
# def cls_decorator(cls):
#     setattr(cls,"count",1)
#     return cls
#
# @cls_decorator
# class Sample:
#     def demo(self):
#         return "hello"
#
# # print(vars(Sample))
# ###################################################################
# ## adding a function into a class
#
# def cls_(cls):
#     def add_(self):
#         return self.a
#     setattr(cls,"add",add_)
#     return cls
# @cls_
# class Demo:
#     def __init__(self,a):
#         self.a = a
#
# # print(vars(Demo))
# #################################################################
#
# def cls_(cls):
#     def __init__(self,a):
#         self.a=a
#     setattr(cls,"__init__",__init__)
#     return cls
#
#
# @cls_
# class Demo:
#     def greet(self):
#         return "hello"
#
# ####################################################################################
# #intercepting data beforing storing in instance dict
#
# def intercept(cls):
#     def new_setattr(self,key,value):
#         if value < 0:
#             raise ValueError("value should not be negative")
#         super().__setattr__(key,value)
#     setattr(cls,"__setattr_",new_setattr)
#     return cls
# @intercept
# class Demo:
#
#     def __init__(self,a):
#         self.a = a


# d=Demo(-10)
#########################################################################################
#write a class decorator to give delay of 3 second before executing any function
# from time import sleep
# def delay(some_func):
#     def wrapper(*args):
#         sleep(3)
#         return some_func(*args)
#     return wrapper
#
#
# def new_func(cls):
#     dict_=cls.__dict__
#     for key,value in dict_.items():
#         if callable(value):
#             setattr(cls,key,delay(value))
#     return cls
# @new_func
# class Demo:
#     def __init__(self):
#         pass
#
#     def add(self):
#         return 10 + 6
#
# d=Demo()
# print(d.add())
##########################################################################################################

def get_name(some_func):
    def wrapper(*args):
        print(f"executing {some_func.__name__}")
        return some_func(*args)
    return wrapper

def cls_decorator(cls):
    for key,value in cls.__dict__.items():
        if callable(value):
            setattr(cls,key,get_name(value))
    return cls
@cls_decorator
class Demo:
    def __init__(self,a,b):
        self.a = a
        self.b = b



    def add(self):
        return self.a + self.b
#
# d=Demo(10,15)
# print(d.add())

#######################################################################################################

def log(cls):
    original_add=cls.add
    def new_add(self):
        print("executing add")
        return original_add(self)
    setattr(cls,"add",new_add)

    return cls

@log
class Demo:

    def add(self):
        pass

    def mul(self):
        pass
# print(vars(Demo))
# d=Demo()
# d.mul()
#######################################################################################################
# parameterised function decorator

def log(message):
    def outer(some_func):
        def wrapper(*args):
            print(message)
            return some_func(*args)
        return wrapper
    return outer

@log("hello")
def greet():
    return "good morning"


# print(greet())

################################################################################################
# parameterised class decorator
def log_message(message):
    def log(cls):
        # original_greet = cls.greet
        def new_greet(self):
            print(message)
            return new_greet(self)
        
        setattr(cls,"greet_new",new_greet)
        return cls
    return log
@log_message("in greet")
class Demo:

    def __init__(self,a):
        self.a = a

    def greet(self):
        return "hello"
# print(vars(Demo))
# d = Demo(10)
# print(d.greet())

#############################################################################################
#adding functionality to a single function of a class
def log_message(message):
    def log(cls):
        original_add= cls.add

        def new_add(self):
            print(message)
            return original_add(self)
        setattr(cls,"add",new_add)
        return cls
    return log
@log("hello")
class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a- self.b
c=Calculator(20,10)
print(c.sub())






























