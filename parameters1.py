class car(object):
	def __init__(self,make,model,year,condtion='new',kms = 0):
		self.make = make
		self.model = model
		self.year = year
		self.condtion = condtion
		self.kms = kms

	def display(self,showall=True):
		if showall:
			print('this car is %s %s from %s, it is %s and has %s kms.' %(self.make, self.model, self.year, self.condtion,self.kms))
		else:
			print('this car is %s %s from %s '%(self.make, self.model, self.year))

whip = car('ford', 'fusion', 2012, 'new', 0)
whip.display(False)

