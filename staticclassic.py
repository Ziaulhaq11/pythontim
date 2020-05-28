class Dog:
	dogs = []

	def __init__(self,name):
		self.name = name
		self.dogs.append(self)

	@classmethod   #decorators
	def num_dogs(cls):
		return len(cls.dogs)

	@staticmethod
	def bark(n):
		"""barks n times"""
		for _ in range(n):
			print("Bark")

tim = Dog('Tim')
jim = Dog('Jim')
#print(Dog/tim.dogs)   #without using an instance also you can call the class
print(Dog.num_dogs())   #in static you dont need to assign self, __init etc.
Dog.bark(5) 
