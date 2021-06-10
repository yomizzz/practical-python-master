import requests
import json

url = 'https://www.jisilu.cn/data/lof/stock_lof_list/'
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.53'
        }   

requests.packages.urllib3.disable_warnings()

source = requests.get(url, headers=headers, verify=False).content.decode()
source_json = source[source.find('{"'):]
stock_dict = json.loads(source_json)
stocks = stock_dict['rows']
headers = ('Name', '现价', '基金净值', '净值日期', '实时估值', '涨跌幅', '溢价率')
# tplt = "{0:>10}\t{1:>10}\t{2:>10}\t{3:>10}\t{4:>10}\t{5:>10}\t{6:>10}"
# tplt = "{0:^10}\t{1:^10}\t{2:^10}\t{3:^10}\t{4:^10}\t{5:^10}\t{6:^10}"
tplt = "{0:<10}\t{1:<10}\t{2:<10}\t{3:<10}\t{4:<10}\t{5:<10}\t{6:<10}"
print(tplt.format('Name', '现价', '基金净值', '净值日期', '实时估值', '涨跌幅', '溢价率', chr(12288)))
'''
for h in headers:
        print(f'{h:>10s}', end=' ')
print()
'''
# print('%10s %10s %10s %10s %10s %10s %10s' %headers)
# print(('-' * 10 + ' ') * len(headers))

report = []
for stock in (stocks[30]['cell'], stocks[52]['cell']):
        stock_rt = (float(stock['estimate_value']) - float(stock['fund_nav']))/float(stock['fund_nav']) * 100
        stock_rt = '%.2f' % stock_rt
        summary = (stock['fund_nm'],stock['price'], stock['fund_nav'], stock['nav_dt'], stock['estimate_value'], stock_rt, stock['discount_rt'])
        report.append(summary)

for row in report:
        # print('%10s %10s %10s %10s %10s %10.2f %10s' %row, chr(12288)) 
        # print(f'{row:>10s}', end=' ')
        # print()
        print(tplt.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], chr(12288)))