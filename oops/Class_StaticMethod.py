# class Demo:
#     num = 10
#
#     def __init__(self,a):
#         self.a = a
#     @classmethod
#     def change_num(cls,new_no):
#         cls.num = new_no
#
# obj1=Demo(5)
# Demo.change_num(89)
# print(vars(Demo))

#################################################################################
# class Employee:
#
#     def __init__(self,fname,lname):
#         self.fname = fname
#         self.lname = lname
#
#     def email(self):
#         return f"{self.fname}.{self.lname}@gmail.com"
#
#     @classmethod
#     def alternate_cons(cls,name):
#         fname,lname = name.split()
#         obj = cls(fname,lname)
#         return obj
#
# name = "john kumar"
# e1 = Employee.alternate_cons(name)
# print(e1.email())
###########################################################

# class Circle:
#     def __init__(self,radius):
#         self.radius = radius
#
#     def circumference(self):
#         return 2 * 3.14 * self.radius
#     @classmethod
#     def through_diameter(cls,diameter):
#         radius = diameter/2
#         circle_obj = cls(radius)
#         return circle_obj
#
# c1= Circle(4)
# print(c1.circumference())
#
# c2 = Circle.through_diameter(8)
# print(c2.circumference())

##############################################################################


# static methods

class Demo:
    a = 10

    def __init__(self, value):
        self.value = value

    def display(self):
        print(self.value, Demo.a)
    @staticmethod
    def print_something():
        print("sample print statement")


# d = Demo(1)
# d.display()
# d.print_something()
# Demo.print_something()

###################################################################


# class StringUtilities:
#
# 	def __init__(self, string):
# 		self.string = string
#
# 	def join_(self, new_string):
# 		return new_string.join(self.string)
#
# 	@staticmethod
# 	def is_palindrome(string):
# 		return string == string[::-1]
#
# 	@staticmethod
# 	def reverse(string):
# 		return string[::-1]
#
# 	@staticmethod
# 	def concatenate(string1, string2):
# 		return string1 + string2
#
# print(StringUtilities.reverse("hello"))
##########################################
