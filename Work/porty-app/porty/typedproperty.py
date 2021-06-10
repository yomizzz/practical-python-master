# typedproperty.py
# 利用闭包快速生成相同的代码

def typedproperty(name, expected_type):
	private_name = '_' + name

	@property
	def prop(self):
		return getattr(self, private_name)

	@prop.setter
	def prop(self, value):
		if not isinstance(value, expected_type):
			raise TypeError(f'Expected {expected_type}')
		setattr(self, private_name, value)

	return prop

# 以下语句的实质都是函数，所以调用也要以函数的形式func().
String = lambda name: typedproperty(name, str)
Integer = lambda name: typedproperty(name, int)
Float = lambda name: typedproperty(name, float)