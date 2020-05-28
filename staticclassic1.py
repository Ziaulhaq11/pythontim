class person(object):
	population = 50
	def __init__(self,name,age):
		self.name = name
		self.age = age

	@classmethod
	def getpopulation(cls,x):  #you dont need an object to access the methods and you dont need self parameter
		return cls.population,x

	@staticmethod
	def isadult(age):
		return age >=18

	def display(self):
		print(self.name, 'is' , self.age, 'years old')


newperson = person('tim',18)
print(person.getpopulation(5))
print(person.isadult(5))
#main difference is class method can use variables which are declared in classes while static cant 
#static doesnt need any variable its optional but in class method it must has to be a variable
print(newperson.display())
person('tim',25)
#print(person.display())  we cant do this bc its not static or classic




