class Dog(object):
    def __init__(self,name,age):
        self.age = age
        self.name = name
    def speak(self):
        print('hi i am ',self.name, self.age , 'years old')
    def talk(self):
        print('bark')
    def drink(self):
        print('drinking')

class Cat(Dog):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color = color
    def  talk(self):
        print('meow')  #we can overwrite dog but doesnt modify dog class

jim = Dog('jim',70)
jim.talk()
jim.speak()
jim.drink()

tim = Cat('tim',25,'blue')
tim.speak()  #tim is an object of cat class
tim.talk()
tim.drink()
