"""
探讨变量的作用域
Python查找一个变量时会按照“局部作用域”、“嵌套作用域”、“全局作用域”和“内置作用域”的顺序进行搜索。
对于函数1中的函数2来说，函数1里定义的变量b属于嵌套作用域，函数2自己内部定义的变量c属于局部作用域，而函数1之外定义的变量a属于全局作用域。

Version: 0.1
Author: yomi
Date: 2021-04-06
"""

def foo():
    b = 'Hello'

    def bar():
        c = True
        print(a)
        print(b)
        print(c)
    
    bar()
    # print(c)  # NameError: name 'c' is not defined

if __name__ == '__main__':
    a = 100
    # print(b) # NameError: name 'b' is not defined
    foo()


# 无法在函数中修改全局变量的值
def foo():
    a = 200
    print(a) # 200

if __name__ == '__main__':
    a = 100
    foo()
    print(a) # 100


# 如何在函数中修改全局变量的值
def foo():
    global a 
    a = 200
    print(a) # 200

if __name__ == '__main__':
    a = 100
    foo()
    print(a) # 200


# 如何在函数的函数中修改嵌套作用域中变量的值
def foo():
    b = 200

    def bar():
        nonlocal b # 声明后，可以修改
        b = 100
        print(b) # 100
    
    bar()
    print(b) # 100

if __name__ == '__main__':
    foo()