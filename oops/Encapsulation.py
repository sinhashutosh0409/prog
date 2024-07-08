
########Bys using Set_attar
# class Demo:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#
#     def __getattribute__(self, item):    ## setattribute example
#         print("get attribute getting invoked")
#         return super().__getattribute__(item)
#
#
#     def __setattr__(self, key, value):
#         print("set Attr getting invoked")
#         if not isinstance(value,int):
#             raise Exception("is not of int type")
#         super().__setattr__(key, value)
# d = Demo(100,19)
# print(d.a)
# print(d.b)
#class Point:
#
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#
#     def __setattr__(self, key, value):
#         print(f"the key  is {key} the value is {value}")
#         super().__setattr__(key,value)


# p1 = Point(10,20)
# print(vars(p1))

##################################################
class Point:
    def __init__(self,a):
        self.a = a

    def __setattr__(self, key, value):
        if value > 0:
            super().__setattr__(key,value)
        else:
            raise Exception("negative integer not allowed")
#
# d = Point(19)
# print(vars(d))

#############################################################
# employee class should accept name, pay
# name > 4 characters
# pay > 1000
class Employee:

    def __init__(self, name , pay):
        self._name = name
        self._pay = pay

    def __setattr__(self, key,value):
        if key == "name":
            if len(value) < 4:
                raise Exception("name should be of four chars")
        elif value == "pay":
            if value< 1000:
                raise Exception("pay should be more than 1000")
        super().__setattr__(key, value)





############################################################################
##by using setteres and getters


# class Demo:
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     @property
#     def a(self):
#         return self.a
#     @a.setter
#     def a(self,value):
#         if not isinstance(value,int):
#             raise Exception("not a int type")
#         self._a = value
#
# d= Demo(10,20)
# print(vars(d))

###########################################################################
# check if the points are positive and values should not be deleted
class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    @property
    def a(self):
        return self._a
    @a.setter
    def a(self, value):
        if value < 0:
            raise Exception("negative not allowed")
        self._a = value

    @a.deleter
    def a(self):
        raise Exception("a cant be deleted")

# p = Point(10,20)
# print(vars(p))
# del p.a
##########################################################################
# employee class should accept name, pay
# name > 4 characters
# pay > 1000
class Employee:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) < 4:
            raise Exception("name should be more than 4 chars")
        self._name = value

    @property
    def pay(self):
        return self._pay

    @pay.setter
    def pay(self, value):
        if value < 1000:
            raise Exception("pay should be more than 1000")
        self._pay = value


e = Employee("mark", 2900)
# print(vars(e))
# print(e.name)

##################################################################################################################################################################################################
# make a class only readable/ immutable
class Demo:
    def __init__(self,a):
        super().__setattr__("a",a)


    def __setattr__(self, key, value):
        raise Exception(" class in read only")

# d = Demo(10)

############################
# count the number of instances created for a class
class Demo:

    count = 0
    def __init__(self, a):
        self.__class__.count +=1
d = Demo(1)
d1 = Demo(2)
d3 = Demo(998787)
print(Demo.count)









