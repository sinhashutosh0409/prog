# **74 Triangle Patterns**
"""
*
* *
* * *
* * * *
* * * * *
"""
n=5
# for row in range(1,n+1):
#     # print("* " * row)


###################################
"""
        *
      * *
    * * *
  * * * *
* * * * *
"""
# n=5
# for row in range(1,n+1):
#     print(f'{"* " * row:>10}')


#######################################
"""
    *
   * *
  * * *
 * * * *
* * * * *
"""
# n=5
# for row in range(1,n+1):
#     print(f'{"* " *row:>10}')
#######################################

"""
* * * * * *
* * * * *
* * * *
* * *
* *
*
"""
# n=5
# for row in range(n,0,-1):
#     print("* " * row)
##############################################

"""
* * * * * *
  * * * * *
    * * * *
      * * *
        * *
          *
"""
# n=5
# for row in range(n,0,-1):
#     print(f'{"* " * row:>10}')
################################################
"""
 * * * * * *
  * * * * *
   * * * *
    * * *
     * *
      *
"""
# n=6
# for row in range(n,0,-1):
#     print(f'{"* " * row:^12}')

##############################################
# Number Pattern in triangle (Left Justified)
"""
1
12
123
1234
12345
"""
# n=""
# for num in range(1,6):
#         n = n + str(num)
#         print(n)


######################################################
# Number Pattern in triangle (Right Justified)
"""
    1
   12
  123
 1234
12345
"""
# n=""
# for num in range(1,6):
#     n=n + str(num)
#     print(f'{n:>5}')

##############################################################

# Number Pattern in triangle (Centre)
"""
     1
    1 2
   1 2 3
  1 2 3 4
 1 2 3 4 5
"""
# n=""
# for num in range(1,6):
#     n=n + str(num)+ " "
#     print(f'{n:^10}')
##############################################################
# **88 Write a program to get the below output**
"""
*
*
*
* *
*
* * *
*
* * * *
*
* * * * *
"""

# for num in range(1,6):
#     print("*")
#     print("* " * num)


###################################################################

# **143 write a program to get the below output using while loop**

"""
1
12
123
1234
"""
# n=""
# count = 1
# while count <=4:
#     n=n+str(count)
#     count = count+1
#     print(n)



#################################################################
# **148 write a program to print the below pattern**
"""
1 2 3 *
1 2 * 4
1 * 3 4
* 2 3 4
"""

# for num in range(5,0,-1):
#     for i in range(1,5):
#         if num == i:
#             print("*",end= " ")
#         else:
#             print(i ,end= " " )
#     print()





###################################################################
# **89 Write a program to get the below output**
#
# >>> [1, 2]
#     [3, 4]
#     [5, 6]
#     [7, 8]
#     [9]

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in range(0,len(a),2):
#     print(a[i:i+2])

####################################################################
# **105 Find the range from the following string**
# >>> # Output Should be [0, 4, 5, 6, 7, 8, 20, 43, 44, 45, 46]

sentence = '0-0, 4-8, 20-20, 43-45'
result = []
r=sentence.split(",")
for item in r:
    a,b=item.split("-")
    ran_= range(int(a),int(b)+1)

    result.extend(list(ran_))
# print(result)

##########################################################################

"""
a 
a b
a b c
a b c d
"""




#################################################################################################################################
n=""
for num in range(4,0,-1):
    n=n+str(num)
    print(n)










