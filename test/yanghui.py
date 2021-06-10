"""
打印杨辉三角

Version: 0.1
Author: yomi
Date: 2021-04-19
"""

def main():
    num = int(input('Number of rows: '))
    yh = [[]] * num #构建列表的列表，其中列表中的每个列表是杨辉三角的每一行
    for row in range(len(yh)): # 第几个列表就是杨辉三角的第几行
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])): #每个列表里的第一项，就是杨辉三角的第一列，以此类推
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()

if __name__ == '__main__':
    main()