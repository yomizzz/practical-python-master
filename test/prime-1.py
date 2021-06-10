"""
输出100以内所有的素数

Version: 0.1
Author: yomi
Date: 2021-04-06
"""

from math import sqrt

primes = []
for num in range(2, 100):
    is_prime = True
    for factor in range(2, int(sqrt(num)) + 1):
        if num % factor == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
for prime in primes:
    print(prime, end=' ')


"""
# 答案
import math

for num in range(2, 100):
    is_prime = True
    for factor in range(2, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')
"""