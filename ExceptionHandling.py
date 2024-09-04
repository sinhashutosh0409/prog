# from csv import reader
# from csv import writer
#
# path = r"C:\Users\Rudra\PycharmProjects\Program001\oops\text1.csv"
#
# with open(path,"r") as file:
#     total = 0
#     rows=reader(file)
#     header = next(rows)
#     # print(header)
#     for row in rows:
#         try:
#             total = total + float(row[3])
#         except ValueError:
#             print(f"the bad data{row}")
#             continue
# print(total)

#####################################################################
names = ["apple", "google", "yahoo", "gmail", "yahoo", "apple","facebook"]
# d={}
# for name in names:
#     try:
#         d[name] = d[name] + 1
#     except KeyError:
#         d[name] = 1
# print(d)

########################################################################3
# numbers = [(1,"h"), (1,6), (3,0), (3,1), (7,10), (1,9), (8,4)]
#
# def div(item):
#     n1,n2 = item
#
#     try:
#         return n1/n2
#     except (ZeroDivisionError,TypeError):
#         print(f"the data is bad data")
#         return item
#
#
#
# for item in numbers:
#     result = div(item)
#     print(result)

################################################################################
# def div(n1,n2):
#     try:
#         print("try block getting executed")
#         result= n1/n2
#         return result
#     except ZeroDivisionError:
#         print("except getting executed")
#         print(f"it is a bad data")
#     else:
#         print("executing else block")
#         # return result
#     finally:
#         print("finally block getting executed")
#
# print(div(10,5))

#################################################################################
##custom exception clSS
class InsufficientFundsException(Exception):
    pass

# def withdraw(amount):
#     if amount > 1000:
#         raise InsufficientFundsException("insufficient funds")
#
# print(withdraw(2000))

##############################################
class AuthError(Exception):
    pass

def admin(id,pwd):
    if id =="admin1" and pwd=="admin123":
        print("login successfull")
    else:
        raise AuthError("invalid credentials")


admin("admin","admin123")
