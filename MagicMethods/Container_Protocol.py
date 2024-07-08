class Point:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __contains__(self, p):
        if p == self.a or p == self.b:
            return True

    def __getitem__(self, index):
        if index == 0:
            return self.a
        elif index ==1:
            return self.b
        else:
            return "invalid index"

    def __setitem__(self,index,value):
        if index ==0:
            self.a = value
        if index ==1:
            self.b = value
class PointPositive(Point):

    def __setitem__(self, index, value):
        if value <= 0:
            raise Exception("index out of range")
        super().__setitem__(index,value)



class RangePoint(Point):

    def __setitem__(self, index, value):
        if index == 0:
            if value > 100 or value < 0:
                raise ValueError(" value not in range")
            else:
                super().__setitem__(index,value)

        if index == 1:
            if value >50 or value < 0:
                raise ValueError("value not in range")
            else:
                super().__setitem__(index,value)

p = RangePoint(10,20)
p[0]=10
print(p.b)
