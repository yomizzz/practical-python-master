"""
验证私有属性

Version: 0.1
Author: yomi
Date: 2021-04-23
"""

class Test:
    def __init__(self, foo):
        self.__foo = foo
    
    def __bar(self):
        print(self.__foo)
        print('__bar')

def main():
    test = Test('hello')
    test._Test__bar()
    print(test._Test__foo)

if __name__ == '__main__':
    main()