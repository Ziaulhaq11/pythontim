class Vehicle(object):
	def __init__(self,price,gas,color):
		self.price  = price
		self.gas = gas
		self.color = color

	def filluptank(self):
		self.gas = 100
	def emptytank(self):
		self.gas = 0
	def gasleft(self):
		return self.gas


class Car(Vehicle):
	def __init__(self,price,gas,color,speed):
		super().__init__(price,gas,color)
		self.speed = speed

	def beep(self):
		print('beep beep')

class Truck(Vehicle):
	def __init__(self,price,gas,color,tires):
		super().__init__(price,gas,color)
		self.tires = tires

	def honk(self):
		print('honk honk')

p1 = Car(25,3,'blue',2)
print(p1.gasleft())
print(p1.color)
p1.beep()		


