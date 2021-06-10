# 计算买股票一共花了多少钱？
'''
total_cost = 0
with open('Data/portfolio.csv', 'rt') as f:
    headers = next(f)
    for line in f:
        #line = line.strip() # 去掉字符串末尾的换行符
        linelist = line.split(',')
        total_cost = total_cost + int(linelist[1]) * float(linelist[2])
    print(f'Total cost {total_cost:0.2f}')
'''

'''
# 将上述语句修改为了函数，并增加了debug模块
def portfolio_cost(filename):
    total_cost = 0
    with open(filename, 'rt') as f:
        headers = next(f)
        for line in f:
            linelist = line.split(',')
            try:
                total_cost = total_cost + int(linelist[1]) * float(linelist[2])
            except ValueError:
                print("Couldn't parse", line)
        return round(total_cost, 2)
        
cost = portfolio_cost('Data/portfolio.csv')
print('Total cost: ', cost)
'''

# 利用python内建的csv模块处理数据
'''
import csv
import sys

def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        # 利用enumerate()函数同时迭代输出row和其对应的行数
        for n, row in enumerate(rows, start=1): 
            try:
                total_cost = total_cost + int(row[1]) * float(row[2])
            except ValueError:
                print(f'Row {n}: Bad row: {row}')
        return round(total_cost, 2)
''' 

'''     
修改上述代码，利用zip()函数将表头和对应的值构成元组，然后将其转换为字典，在不需要知道各表头所在列数的情况下直接调用。
调用newreport模块里的read_portfolio()函数，该函数返回的就是由一个个字典组成的列表，字典里是每一个股票的名字，股数和价格。
'''
import csv
import sys
from report import read_portfolio

def portfolio_cost(filename):
    total_cost = 0.0
    rows = read_portfolio(filename)
    # 利用enumerate()函数同时迭代输出row和其对应的行数
    for n, row in enumerate(rows, start=1):
        try:
            nshares = row['shares']
            price = row['price']
            total_cost += nshares * price 
        except ValueError:
            print(f'Row {n}: Bad row: {row}')
    return round(total_cost, 2)


# main() function 
def main(args):
    if len(args) != 2:
        raise SystemExit(f'Usage: {args[0]}' 'portfile')
    
    portfile = args[1]
    print('Total cost:', portfolio_cost(args[1]))
    

if __name__ == '__main__':
    import sys
    main(sys.argv)


'''
#判断执行py文件时输入的参数个数，如为两个，则将第二个参数作为函数的参数输入
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost: ', cost)           
'''    
