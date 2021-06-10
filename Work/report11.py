import csv

def read_portfolio(filename):
    ''' 
    Read a stock portfolio file into a list of dictionaries with keys name, shares, and price.
    '''
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        
        for row in rows:
            types = [str, int, float]
            stock = { header: func(val) for header, func, val in zip(headers, types, row)}
            portfolio.append(stock)        
    
    return portfolio  

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]]= float(row[1])
            except IndexError:
                pass      
    return prices

def make_report(portfolio, prices):
    '''
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    '''
    report = []
    for s in portfolio:
        summary = (s['name'], s['shares'], prices[s['name']], float(prices[s['name']])- float(s['price']))
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
    
    for name, shares, price, change in report:
        price = '$' + str(f'{price:0.2f}') # 在price前面加上$
        print(f'{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}')
    
    
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
    