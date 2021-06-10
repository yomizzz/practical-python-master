from .newfileparse import parse_csv
from . import stock
from . import tableformat
from .portfolio import Portfolio

def read_portfolio(filename, **opts):
    ''' 
    Read a stock portfolio file into a list of dictionaries with keys name, shares, and price.
    '''
    with open(filename) as lines:
        return Portfolio.from_csv(lines, **opts)

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    with open(filename) as lines:
        return dict(parse_csv(lines, types=[str, float], has_headers=False))
    
def make_report(portfolio, prices):
    '''
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    '''
    report = []
    for s in portfolio:
        summary = (s.name, s.shares, prices[s.name], prices[s.name]- s.price)
        report.append(summary)
    
    return report

# 通过类，实现不同格式的输出
def print_report(reportdata, formatter):
    '''
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    '''
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])

    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)
    
    
def portfolio_report(portfoliofile, pricefile, fmt='txt'):
    '''
    Make a stock report given portfolio and price data files.
    '''
    # Read data files 
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)
    
    # Create the report data
    report = make_report(portfolio, prices)
    
    # Print it out
    # 每次修改要打印的类型，只要修改此处即可
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)
 
# main() function 
def main(args):
    if len(args) != 4:
        raise SystemExit(f'Usage: {args[0]}' 'portfile pricefile formatter')
    portfolio_report(args[1], args[2], args[3])
    
if __name__ == '__main__':
    import sys
    main(sys.argv)
    
