# report.py
#
# Exercise 2.4

'''
# 将元组作为列表的元素存储数据
import csv

def read_portfolio(filename):
    portfolio = []
    
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)
            
    return portfolio
'''

# 将字典作为列表的元素存储数据
import csv
'''
def read_portfolio(filename):
    portfolio = []
    
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
         
            holding = {
                 'name'   : row[0],
                 'shares' : int(row[1]),
                 'price'   : float(row[2])
            }
            
            portfolio.append(holding)
            
    return portfolio
'''
# 将上述代码用zip() 函数修改,zip()函数会把整数和浮点数转换为字符串，要计算的时候需要转换格式；或者将zip()函数生成的元组形成的字典里的字符串重新转换为整数和浮点数，重新组成一个新的字典，后续代码就不用修改了。
def read_portfolio(filename):
    portfolio = []
    
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row))
            stock = {
                 'name'   : record['name'],
                 'shares' : int(record['shares']),
                 'price'   : float(record['price'])
                 }
            portfolio.append(stock)
            
    return portfolio  


def read_prices(filename):
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]]= float(row[1])
            except IndexError:
                pass
                
    return prices

           
portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

total_cost = 0.0
for s in portfolio:
    total_cost += s['shares'] * s['price']
    
total_value = 0.0
for s in portfolio:
    total_value += s['shares'] * prices[s['name']]

print('Current value', total_value)
print('Gain', total_value - total_cost)

def make_report(portfolio, prices):
    report = []
    for s in portfolio:
        stock = (s['name'], s['shares'], prices[s['name']], float(prices[s['name']])- float(s['price']))
        report.append(stock)
        
    return report

headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)

print('---------- ' * 4)

'''
report = make_report(portfolio, prices)
for r in report:
    print('%10s %10d %10.2f %10.2f' % r)
 '''   


# 这条语句输出内容格式同上， 换了f-strings来格式化字符串
report = make_report(portfolio, prices)
for name, shares, price, change in report:
    price = '$' + str(f'{price:0.2f}') # 在price前面加上$
    print(f'{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}')


