def func(x=1):   #now this is an opt parameter if we dont assign value also it will execute
	return x **2

call = func(5)
print(call)

def fun(word,add= 5,freq = 4):
	print(word*(freq+add))

calls = fun('tim')

