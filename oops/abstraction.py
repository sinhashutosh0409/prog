from abc import ABC,abstractmethod

# class Vehicle(ABC):
#     def __init__(self, company, cc):
#         self.company = company
#         self.cc = cc
#
#     @abstractmethod
#     def engine(self):
#         pass
#
# class Bike(Vehicle):
#      def engine(self):
#          return f"{self.company} has {self.cc}cc"
#
# class Car(Vehicle):
#
#     def engine(self):
#         return f"{self.company} has {self.cc}cc"
#
# b = Bike("yamaha", 153)
# c = Car("alto", 800)
# print(b.engine())
# # print(c.engine())


########################################################################################################################
from abc import ABC,abstractmethod

# class Demo(ABC):
#
#     @abstractmethod
#     def spam(self):
#         print("hello spam")
#
#     def spam1(self):
#         print("hello spam1 in parent")
#
# class Demo1(Demo):
#     def spam(self):
#         print("Demo1 spam")
#
# d = Demo1()
# d.spam()

###############################################
# class BaseLogger(ABC):
#     @abstractmethod
#     def log(self):
#         pass
#
# class ConsoleLogger(BaseLogger):
#
#     def log(self,message):
#         print(message)
#
# class TextFileLogger(BaseLogger):
#
#     def __init__(self,file_object):
#         self.file_object = file_object
#
#     def log(self,message):
#         self.file_object.write(message)
#         self.file_object.write("\n")
#
# class FilteredLogger:
#     def __init__(self,pattern,logger_obj):
#         self.pattern = pattern
#         self.logger_obj = logger_obj
#     def log(self,message):
#         if self.pattern in message:
#             self.logger_obj.log(message)
# d = ConsoleLogger()
# f = open("text1.txt" , "w")
# d=FilteredLogger("hello")
# print(vars(d))
# tfl = TextFileLogger(f)



# e= FilteredLogger("hello", d)
# e.log("hello i am in the console logger")

##############################################################################################################
from abc import ABC

class Base(ABC):
    @abstractmethod
    def log(self):
        pass

class ConsoleLogger(Base):
    def log(self,message):
        print(message)

class FilteredLogger:
    def __init__(self,pattern,logger_object):
        self.pattern = pattern
        self.logger_object = logger_object

    def log(self,message):
        if self.pattern in message:
            self.logger_object.log(message)

# c = ConsoleLogger()
# f = FilteredLogger("hello", c)
# f.log("hello python how are you")
##############################################################
##duck Typing
class Base(ABC):
    @abstractmethod
    def move(self):
        pass
    @abstractmethod
    def display(self):
        pass

class Point(Base):

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def move(self,da,db):
        self.a = self.a + da
        self.b = self.b + db

    def display(self):
        print(self.a,self.b)
class Point2(Base):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def move(self,dx,dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def display(self):
        print(self.x,self.y)


# p = Point(10,20)
# # p.move(5,5)
# p.display()
##########################################################################################################























