li =[1,2,3,4,5,6,7,8,9,10]

def func(x):
	return x**x

newlist = []

'''for x in li:
	newlist.append(func(x))
	print(newlist)

print(newlist)'''

print(list(map(func,li)))  #map function

print([func(x) for x in li if x%2 ==0] ) 

'''list comprehension'''
