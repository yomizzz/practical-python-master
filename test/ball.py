"""
双色球选号

Version: 0.1
Author: yomi
Date: 2021-04-19
"""

from random import randrange, randint, sample

def display(balls):
    """
    输出列表中的双色球号码
    """
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print('%02d' % ball, end=' ')
    print()

def random_select():
    """
    随机选择一组号码
    """
    red_balls = [x for x in range(1, 34)] # 生成包含1到33共33个数的列表
    selected_balls = []
    selected_balls = sample(red_balls, 6) # 从列表中选出6个不重复的数字
    selected_balls.sort() # 对选出的数字进行排序
    selected_balls.append(randint(1, 16)) # 在列表最后添加一个随机数字
    return selected_balls

def main():
    n = int(input('机选几注：'))
    for _ in range(n):
        display(random_select())

if __name__ == '__main__':
    main()