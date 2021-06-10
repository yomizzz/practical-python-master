# timethis.py

import time

def timethis(func):
	def wrapper(*args, **kwargs):
		start = time.time()
		r = func(*args, **kwargs)
		end = time.time()
		name = func.__name__
		module = func.__module__
		print('%s.%s: %f' % (module, name, end-start))
	return wrapper