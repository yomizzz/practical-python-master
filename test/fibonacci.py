"""
生成斐波那契数列的前20个数

Version: 0.1
Author: yomi
Date: 2021-04-06
"""

x = 1
y = 1
print(x, end='\t')
print(y, end='\t')
for i in range(18):
    x, y = y, x + y
    print(y, end='\t')


"""
# 答案
a = 0
b = 1
for _ in range(20):
    a, b = b, a + b
    print(a, end=' ')
"""

# 利用生成器生成斐波那契数列
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a

def main():
    for val in fib(20):
        print(val)
    
if __name__ == '__main__':
    main()