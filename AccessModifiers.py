#access modifiers
#public

class Sample:
    number = 10

    def __init__(self,a):
        self.a = a

    def display(self):
        return self.a

class Sample2(Sample):
    def spam(self):
        return self.a

# d = Sample2(100)
#
# print(d.number)

####################################################################
#private

class Demo1:
    __number = 100

    def __init__(self, a, b):
        self._a = a
        self.__b = b

    def __spam(self,a,b):
        print()

class Demo2(Demo1):
    def spam2(self):
        print(self._a, self._Demo1__b)

d= Demo2(10,20)
d.spam2()

# print(d._Demo1__number)
print(vars(d))






