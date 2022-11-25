# Aniruddha

#  Factorial approaches
#  by using reduce with lambda function.

from functools import reduce

# x = 5
# v = reduce(lambda x, y: x*y, [1, 1] if x == 0 else range(1, x+1))
# print(v)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# res = reduce(lambda x, y: x*y, range(1, 6))
# print(res)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# factorial of a number provided by the user
# using recursion


# def factorial_(x):
#     if x == 1:
#         return 1
#     else:
#         return x * factorial_(x - 1)
#
#
# num = int(input("Enter a number: "))
# result = factorial_(num)
# print("The factorial of", num, "is", result)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# factorial by recursion method
# def fact_(func):
#     if func == 1:
#         return 1
#     else:
#         return func * fact_(func - 1)
#
#
# num = int(input("Enter the number to find the factorial: "))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# n = int(input("enter the number: "))
# fact = lambda n: 1 if n == 0 else n * fact(n-1)
# print(fact(n))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
