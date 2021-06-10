from fileparse import parse_csv

def read_portfolio(filename):
    ''' 
    Read a stock portfolio file into a list of dictionaries with keys name, shares, and price.
    '''        
    return parse_csv(filename, select=['name', 'shares', 'price'], types=[str, int, float]) 

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    return dict(parse_csv(filename, types=[str, float], has_headers=False))
    
def make_report(portfolio, prices):
    '''
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    '''
    report = []
    for s in portfolio:
        summary = (s['name'], s['shares'], prices[s['name']], prices[s['name']]- s['price'])
        report.append(summary)  
    
    return report

def print_report(report):
    '''
    Print stock name, shares, price, and change.
    '''
    headers = ('Name', 'Shares', 'Price', 'Change')
    # 在函数里用print()函数也是ok的
    print('%10s %10s %10s %10s' % headers) 
    print(('-' * 10 + ' ') * len(headers))
    
    for row in report:
        print('%10s %10d %10.2f %10.2f' %row)
    
    
def portfolio_report(portfoliofile, pricefile):
    '''
    Make a stock report given portfolio and price data files.
    '''
    # Read data files 
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)
    
    # Create the report data
    report = make_report(portfolio, prices)
    
    # Print it out
    print_report(report)
 
# main() function 
def main(args):
    if len(args) != 3:
        raise SystemExit(f'Usage: {args[0]} ' 'portfile pricefile')
    portfolio_report(args[1], args[2])
    
if __name__ == '__main__':
    import sys
    main(sys.argv)
    