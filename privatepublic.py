class _Private:
	def __init__(self,name):
		self.name = name
		print(name)

class NotPrivate:
	def __init__(self,name):
		self.name = name
		self.last = _Private(name)

	def _display(self):
		print('hello')

	def display(self):
		print('hi')

i = _Private('jl')
j = NotPrivate('zia')

