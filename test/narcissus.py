"""
找出所有的水仙花数

Version: 0.1
Author: yomi
Date: 2021-04-05
"""

for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)