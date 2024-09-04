# adding class variable to a class
# def outer(cls):
#     setattr(cls,"number", 0)
#     return cls
#
# @outer
# class Demo:
#
#     def func1(self):
#         print("in func1")
#
#     def func2(self):
#         print("in func2")
#
# obj1 = Demo()
# print(vars(Demo))
#####################################
# adding function to a classd
from time import sleep


# def add_function(cls):
#     def add(self):
#         return self.a + self.b
#
#     setattr(cls, "add", add)
#     return cls
#
# @add_function
# class Calculator:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#
# print(vars(Calculator))

############################################################
# adding constructor to a function
# def add_init(cls):
#     def __init__(self, a,b):
#         self.a = a
#         self.b = b
#
#     setattr(cls, "__init__", __init__)
#     return cls
# @add_init
# class Demo:
#     def add(self):
#         return self.a + self.b
#
#     def sub(self):
#         return self.a - self.b
#
# print(vars(Demo))
########################################################################
# adding __setattr__ function to a class using class decorator
#that intercepts the data before storing in instance dictionary

# def datainterceptor(cls):
#     def __setattr__(self, key, value):
#         if value < 0:
#             raise Exception("negative not allowed")
#         object.__setattr__(self,key,value)
#
#     setattr(cls , "__setattr__", __setattr__)
#     return cls
#
# @datainterceptor
# class Spam:
#
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#
# s = Spam(100,20)
# print(vars(Spam))

###########################################################
# log message with function name on execution

# def logger(func):
#     def wrapper(*args, **kwargs):
#         print(f"executing {func.__name__}")
#         return func(*args , **kwargs)
#     return wrapper
#
# def log(cls):
#     d = cls.__dict__
#     for key,value in d.items():
#         if callable(value):
#             setattr(cls, key ,logger(value))
#     return cls
#
#
#
# @log
# class Demo:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def add(self):
#         return self.a + self.b
#
#     def sub(self):
#         return self.a - self.b
#
# obj = Demo(18,89)
# print(obj.add())

################################################################
# write a class decorator to give delay of 3 seconds in between methods
# def delay(func):
#     def wrapper(*args,**kwargs):
#         sleep(3)
#         return func(*args, **kwargs)
#     return wrapper
# def class_delay(cls):
#     d = cls.__dict__
#     for key,value in d.items():
#         if callable(value):
#             setattr(cls , key , delay(value))
#     return cls
# @class_delay
# class Sample:
#     def func1(self):
#         print("in func1")
#     def func2(self):
#         print("in func2")
#
# s = Sample()
# s.func1()
# s.func2()
##################################################################################################
# singleton class
# class Singleton:
#     count = 0
#     def __init__(self,a,b):
#         Singleton.count +=1
#         self.a = a
#         self.b = b
#         if Singleton.count >1:
#             raise Exception("not allowed")

# s = Singleton(10,20)
# d=Singleton(20,89)
###########################################################################
# singleton class using class decorator













