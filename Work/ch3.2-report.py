import csv

def portfolio_report(filename1, filename2):
    portfolio = []
    with open(filename1) as f:
        rows = csv.reader(f)
        headers = next(rows)
        
        for row in rows:
            types = [str, int, float]
            stock = { header: func(val) for header, func, val in zip(headers, types, row)}
            portfolio.append(stock)  
     
    prices = {}
    with open(filename2) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass

    report_list = []
    for s in portfolio:
        report = (s['name'], s['shares'], prices[s['name']], float(prices[s['name']])- float(s['price']))
        report_list.append(report)  
    
    headers = ('Name', 'Shares', 'Price', 'Change')
    a = '%10s %10s %10s %10s' % headers
    b = ('-' * 10 + ' ') * len(headers)
    
    finalreport = [a, b]
    for name, shares, price, change in report_list:
        price = '$' + str(f'{price:0.2f}') # 在price前面加上$
        finalreport.append(f'{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}')
    
    # return finalreport
