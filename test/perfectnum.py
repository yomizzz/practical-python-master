"""
找出10000以内的完美数
完美数又称为完全数或完备数，它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身。例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美数。

Version: 0.1
Author: yomi
Date: 2021-04-06
"""

from math import sqrt

for num in range(2, 10000):
    factors = []
    for factor in range(1, int(sqrt(num) + 1)):
        if num % factor == 0:
            factors.append(factor)
            if factor > 1 and num // factor != factor:
                factors.append(num // factor)
    if sum(factors) == num:
        print('%d是一个完美数！' % num)


"""
# 答案 有瑕疵，会把1也当成完美数
import math

for num in range(1, 10000):
    result = 0
    for factor in range(1, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            result += factor
            if factor > 1 and num // factor != factor:
                result += num // factor
    if result == num:
        print(num)
"""