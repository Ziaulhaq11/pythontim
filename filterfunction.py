def add7(x):
	return x+7

def isodd(x):
	return x%2 != 0

a = [1,2,3,4,5,6,7,8,9,10]

b = list(filter(isodd,a))  #if we use map it will show true or false
c = list(map(add7,b))
#c = list(map(add7,filter(isodd,a)))   both are same but it will save the time

