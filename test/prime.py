"""
输入一个正整数判断其是否为素数

Version: 0.1
Author: yomi
Date: 2021-04-05
"""

from math import sqrt

num = int(input('请输入一个正整数：'))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是一个素数。' % num)
else:
    print('%d不是一个素数。' % num)