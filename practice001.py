class A:
    count = 0

    def __init__(self):
        A.count += 1
        if A.count == 1:
            pass
        else:
            raise Exception("You cannot create more than one object ")

a = A()