#
# #case1 both classes having independent methods
# class Demo:
#     def __init__(self,name):
#         self.name = name
#
#     def apple(self):
#         print("in Demo apple")
#         print("in Demo apple called by super in Demo2")
#
#
#     def google(self):
#         print("in Demo google")
#
#
# # class Demo1(Demo):
# #     def m3(self):
# #         print("in Demo1 m3")
#
# # obj1 = Demo1("steve")
# # obj1 = Demo1()
# # print(vars(obj))
# # print(obj1.m3())
#
#
# ##############################################################################################################
# # parent and child have method having same name
# # this is child  over-riding parent class method
#
# # class Demo2(Demo):
# #
# #     def apple(self):
# #         print("in Demo2 apple")
# #         super().apple()
# #
# # d=Demo2("steve")
# # d.apple()
# ###########################################################################################################
# # child having their own constructor
#
# class Demo3(Demo):
#
#     def __init__(self,a):
#         self.a = a
#         super().__init__("hiii") # passing argument to parent class constructor
#
#     def apple(self):
#         print("hello i am in demo333")
#
# d = Demo3(10)
# print(d.__dict__)
############################################################################
#multiple inheritence

class Demo1:

    def __init__(self,a):
        self.a = a

    def apple(self):
        return "apple"

    def facebook(self):
        return "facebook in Demo1"

class Demo2:
    def __init__(self,name):
        self.name = name

    def google(self):
        return "google"

class Demo(Demo1,Demo2):
    def __init__(self,age,a,name):
        Demo1.__init__(self,a)
        Demo2.__init__(self,name)

    def facebook(self):
        return "facebook"


obj = Demo(18,12,"steve")
print(obj.facebook())
print(obj.google())
print(obj.apple())
print(Demo.__mro__)












