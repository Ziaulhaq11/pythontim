import random

def generaterandom(upper):

    r = random.randint(1,upper)
    return r


def main():

    run = True
    num1 = generaterandom(10)
    num2 = generaterandom(10)
    result = num1*num2

    while run:
        ans = input('what is ' + str(num1) +'x' +str(num2) + '?')

        if ans.isdigit():   #i think isdigit returns True that means positive no so negative no return else func
            if int(ans) == result:
                print('Correct')
                run = False
            else:
                print("Incorrect Try again")
        else:
            print('Answer must be positive number try again')

times = 10

for x in range(times):
    main()



