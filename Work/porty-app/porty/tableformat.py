# tableformat.py

class Tableformatter:
	"""docstring for Tabelformat"""
	def headings(self, headers):
		'''
		Emit the table headings.
		'''
		raise NotImplementedError()

	def row(self, rowdata):
		'''
		Emit a single row of table data.
		'''
		raise NotImplementedError()

class TextTableFormatter(Tableformatter):
	'''
    Emit a table in plain-text format
    '''
	def headings(self, headers):
		for h in headers:
			print(f'{h:>10s}', end=' ')
		print()
		print(('-'*10 + ' ')*len(headers))

	def row(self, rowdata):
		for d in rowdata:
			print(f'{d:>10s}', end=' ')
		print()		

class CSVTableFormatter(Tableformatter):
	'''
	Output portfolio data in CSV format
	'''
	def headings(self, headers):
		print(','.join(headers))

	def row(self, rowdata):
		print(','.join(rowdata))

class HTMLTableFormatter(Tableformatter):
	'''
	Output portfolio data in HTML format
	'''
	def headings(self, headers):
		print('<tr>', end='')
		for h in headers:
			print('<th>' + h + '</th>', end='')
		print('</tr>')

	def row(self, rowdata):
		print('<tr>', end='')
		for d in rowdata:
			print('<td>' + d + '</td>', end='')
		print('</tr>')

class FormatError(Exception):
	pass

def create_formatter(name):
	if name == 'txt':
		return TextTableFormatter()
	elif name == 'csv':
		return CSVTableFormatter()
	elif name == 'html':
		return HTMLTableFormatter()
	else: 
		raise FormatError(f'Unknown table format {name}')

def print_table(portfolio, headers, formatter):
	'''
    Make a nicely formatted table from a list of objects and attribute names.
    '''
	formatter.headings(headers)
	# 使用动态属性访问的方法来实现更方便地访问属性
	for s in portfolio:
		rowdata = [ str(getattr(s, header)) for header in headers ]
		formatter.row(rowdata)
