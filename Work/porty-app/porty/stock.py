from .typedproperty import typedproperty, String, Integer, Float


class Stock:
	'''
    An instance of a stock holding consisting of name, shares, and price.
    '''
    # 使用闭包来快速生成相同的代码
	'''
	name = typedproperty('name', str)
	shares = typedproperty('shares', int)
	price = typedproperty('price', float)
	'''
	name = String('name')
	shares = Integer('shares')
	price = Float('price')

	# __slots__ = ('name','_shares','price')
	def __init__(self, name, shares, price):
		self.name = name
		self.shares  = shares
		self.price = price
	
	# 使Stock(args)打印结果更清晰
	def __repr__(self):
		return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'

	@property
	def cost(self):
		'''
        Return the cost as shares*price
        '''
		return self.shares * self.price

	def sell(self, nshares):
		'''
        Sell a number of shares
        '''
		self.shares -= nshares

	'''
	@property
	def shares(self):
		return self._shares

	@shares.setter
	def shares(self, value):
		if type(value) != int:
			raise TypeError('Expected int')
		self._shares = value
	'''



	
	


		
