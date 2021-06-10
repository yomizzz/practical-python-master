"""
输入两个正整数，计算它们的最大公约数和最小公倍数

Version: 0.1
Author: yomi
Date: 2021-04-05
"""

x = int(input('x = '))
y = int(input('y = '))
# 如果x > y，则交换x和y
if x > y:
    x, y = y, x
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公约数是：%d' % (x, y, factor))
        print('%d和%d的最小公倍数是：%d' % (x, y, x * y // factor))
        break