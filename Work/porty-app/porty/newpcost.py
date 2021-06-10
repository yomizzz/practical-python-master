'''     
调用newreport模块里的read_portfolio()函数，
该函数返回的就是由一个个字典组成的列表，
字典里是每一个股票的名字，股数和价格。
'''
from .newreport import read_portfolio
from . import stock
from . import portfolio

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    portfolio = read_portfolio(filename)
    return portfolio.total_cost
    


# main() function 
def main(args):
    if len(args) != 2:
        raise SystemExit(f'Usage: {args[0]}' 'portfile')
    
    portfile = args[1]
    print('Total cost:', portfolio_cost(args[1]))
    

if __name__ == '__main__':
    import sys
    main(sys.argv)
