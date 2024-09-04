#make a class iterable

class Iterable:

    def __init__(self,a):
        self.a = a
    def __iter__(self):
        return iter(self.a)
# i = Iterable("hello")
# for item in i:
#     print(item)
######################################################
#implement range in a class
class Custom_Range:

    def __init__(self):
        self.start = 1
        self.end = 5

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        number = self.start
        self.start += 1
        return number


# c = Custom_Range()
# for item in c:
#     print(item)











# iterator class to traverse through even numbers

class Demo:
    def __init__(self,start,end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise ValueError

        next_number = self.start
        self.start += 1
        if self.start %2 ==0:
            return self.start


# d=Demo(1,11)
# for item in d:
#     if item:
#         print(item)

############################################################
#make class iterable based on index

class Iterable_Index:

    def __init__(self,sequence):
        self.sequence = sequence
        self.index=0
        self.length = len(self.sequence)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.length:
            raise StopIteration

        char = self.sequence[self.index]
        self.index += 1
        return char

# obj = Iterable_Index("hello12345")
# for item in obj:
#     print(item)


