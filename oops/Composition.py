class ConsoleLogger:

    def log(self,message):
        print(message)

class Filtered:
    def __init__(self, some_word, obj):
        self.some_word = some_word
        self.obj = obj

    def log1(self,message):
        if self.some_word in message:
            self.obj.log(message)

d=ConsoleLogger()
e=Filtered("hello", d)
e.log1("hello there how are you")

#
# l = Filtered("hello", logger)
# class Salary:
#     def __init__(self,pay):
#         self.pay = pay
#     def annual_pay(self):
#         return self.pay * 12
# e1 = Salary(1000)
# res = e1.annual_pay()
# # e1.annual_pay()
# print(res)
#
# class Emp:
#     def __init__(self,name,bonus , pay):
#         self.name = name
#         self.bonus = bonus
#         self.pay = pay
#         self.sal_obj = Salary(self.pay)
#
#     def total_pay(self):
#         return self.sal_obj.annual_pay() + self.bonus
#
# e2 = Emp("steve", 500, 1000)
# # print(e2.total_pay())
# # print(e2.__dict__)
##############################################################
# class Numbers:
#
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#
#     def add(self):
#         return self.a + self.b
#
#     def sub(self):
#         return self.a - self.b
#
#     def mul(self):
#         return self.a * self.b

# class Calculator:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#         self.class_obj = Numbers(self.a,self.b)
#
#     def calculation(self):
#         return self.class_obj.mul()
# n1 = Calculator(12,5)
#
# res = n1.calculation()
# print(res)
# ########################################################################################
##aggregation example

# class ConsoleLogger:
#
#     def log(self,message):
#         print(message)
#
# class FilterConsole:
#
#     def __init__(self,some_word):
#         self.some_word = some_word
#         self.obj = ConsoleLogger()
#
#     def log1(self,message):
#         if self.some_word in message:
#             self.obj.log(message)
#
# a = FilterConsole("hello")
# a.log1("hell there how are you")

class TextFile:

    def __init__(self, file_object):
        self.file_object = file_object

    def log(self, message):
        self.file_object.write(message)
        self.file_object.write("\n")
        self.file_object.flush()
class Filter:
    def __init__(self,some_word,file_object):
        self.file_object = file_object
        self.some_word = some_word
        self.obj = TextFile(self.file_object)

    def log1(self,message):
        if self.some_word in message:
            self.obj.log(message)
#
# f = open("text1.txt", "w")
# d = Filter("hello",f)
# d.log1("hello there how are  you")
# from csv import writer
#
# class Csv:
#     def __init__(self,file_object):
#         self.file_object = file_object
#
#     def log(self,message):
#         csv_writer = writer(self.file_object)
#         csv_writer.writerow(message)
#
# class Filter:
#     def __init__(self,some_word, some_func):
#         # self.file_object = file_object
#         self.some_word = some_word
#         self.some_func = some_func
#
#     def log1(self,message):
#         if self.some_word in message:
#             self.some_func.log(message)
#
#
# f = open("text1.csv", "w")
# d = Csv(f)
# f = Filter("hello",d)
# f.log1("hello how hello")
######################################################################################
################Aggregation
# class Emp:
#     def __init__(self, name ,salary):
#         self.name = name
#         self.salary = salary
#
#     def annual_sal(self):
#         return self.salary * 12
#
# class Bonus:
#     def __init__(self, bonus,name,salary):
#         self.bonus = bonus
#         self.obj = Emp(name,salary)
#
#     def total_sal(self):
#         return self.obj.annual_sal() + self.bonus
#
# d = Bonus(2000,"steve", 15000)
# print(d.total_sal())
#######################################################################################
class Emp:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def annual(self):
        return self.pay * 12

class Bonus:
    def __init__(self, bonus,obj):
        self.bonus = bonus
        self.obj = obj

    def annual_bonus(self):
        return self.obj.annual() + self.bonus

d = Emp("steve", 15000)
e=Bonus(1000,d)
print(e.annual_bonus())









































