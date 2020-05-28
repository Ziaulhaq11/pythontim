
class Dog(object):
    def __init__(self,name,age):  #init is a constructor when we create this object we dont need to call it manually
                                 #name is an argument/attributes all are methods
        self.name = name
        self.age = age
    def speak(self):
        print('hi i am ',self.name, self.age , 'years old')
    def change_age(self,age):
        self.age = age
    def add_weight(self,weight):
        self.weight = weight

tim = Dog('tim', 55)
fred = Dog('fred', 25)
tim.change_age(5)
tim.speak()  #tim is an instance of Dog
fred.speak()
tim.add_weight(70)
print(tim.name)
print(tim.age)
print(tim.weight)
#print(fred.weight)  error because i didnt call it from fred instance


