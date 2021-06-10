# following.py
# 读取实时的数据流，并将读取的数据与Data/portfolio.csv文件中的对比，如果股票名称一致，就打印输出。

import os
import time

def follow(filename):
	'''
    Generator that produces a sequence of lines being written at the end of a file.
    '''
	f = open(filename, 'r')
	f.seek(0, os.SEEK_END)
	while True:
		line = f.readline()
		if line == '':
			time.sleep(0.1) # Sleep briefly to avoid busy wait
			continue
		yield line

if __name__ == '__main__':
	import newreport

	portfolio = newreport.read_portfolio('Data/portfolio.csv')

	for line in follow('Data/stocklog.csv'):
		row = line.split(',')
		name = row[0].strip('"')
		price = float(row[1])
		change = float(row[4])

		if name in portfolio:
			print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')