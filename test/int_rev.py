"""
正整数的反转

Version: 0.1
Author: yomi
Date: 2021-04-05
"""

num = int(input('num = '))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)