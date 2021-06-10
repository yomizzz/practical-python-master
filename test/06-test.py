"""
06 函数和模块的使用 练习

Version: 0.1
Author: yomi
Date: 2021-04-06
"""

# 实现计算求最大公约数和最小公倍数的函数
def gcd(x, y):
    """
    求最大公约数
    """
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor

def lcm(x, y):
    """
    求最小公倍数
    """
    return x * y // gcd(x, y)


# 实现判断一个数是不是回文数的函数
# 将需判断的数反转，看其是否和原数相等
def is_palindrome(num):
    """
    判断一个数是不是回文数
    """
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num 

# 实现判断一个数是不是素数的函数
def is_prime(num):
    """
    判断一个数是不是素数
    """
    for factor in range(2, int(num ** 0.5) + 1):
        if num % factor == 0:
            return False
    return True if num != 1 else False

# 判断输入的正整数是不是回文素数
if __name__ == '__main__':
    num = int(input('请输入正整数：'))
    if is_palindrome(num) and is_prime(num):
        print('%d是回文素数。' % num)