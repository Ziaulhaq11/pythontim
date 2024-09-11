var  = 9
loop = True
newvar = 12
def fun(x):
    newvar = 7
    global loop  #using this we can change from local to global
    loop = 5   #now its not same variable its a new variable

    print(loop)
    if x == 5:
        return newvar
#print(newvar) error occured because its a local variable

def other():
    newvar = 9
    print(newvar)

other()
print(newvar)
print(fun(5))
print(loop)
