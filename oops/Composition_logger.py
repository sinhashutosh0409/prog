# Console_Logger_Example
# class Console:
#     def log(self,message):
#         print(message)
#
# class Filter:
#     def __init__(self, some_word, obj):
#         self.some_word = some_word
#         self.obj = obj
#
#     def log1(self, message):
#         if self.some_word in message:
#             return self.obj.log(message)
#
# c = Console()
# d = Filter("info", c)
# d.log1("hello world are you there how are you")


############################################################################################
#Text FileLogger Example
#
# class Text:
#     def __init__(self,file_object):
#         self.file_object = file_object
#
#     def log(self,message):
#         self.file_object.write(message + "\n")
#         self.file_object.flush()
#
# class Filter:
#     def __init__(self, some_word,obj):
#         self.some_word = some_word
#         self.obj = obj
#
#
#     def log1(self,message):
#         if self.some_word in message:
#             self.obj.log(message)
#
# f = open("text2.txt", "w")
# d= Text(f)
# e = Filter("hello", d)
# e.log1("hello steve are you feeling well")
################################################################################################################3
##CSV File Logger Example
from csv import writer

class Csv:
    def __init__(self, file_object):
        self.file_object = file_object

    def log(self,message):
        csv_writer = writer(self.file_object)
        csv_writer.writerow(message)

class Filter:

    def __init__(self,some_word,obj):
        self.some_word = some_word
        self.obj = obj

    def log1(self,message):
        self.obj.log(message)
f= open("text2.csv", "w")
d = Csv(f)
e = Filter("hello",d)
e.log1("hello java")






























