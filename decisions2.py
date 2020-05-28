height = input()

if int(height) < 1:
    print("you cannot ride under")
elif int(height) == 5:    #here this condition is contradicting with next condition but as this is first so the next condition will not be a issue
    print("wow you are eligible")
elif int(height) > 2:
    print("you cannot ride over 2m")
else:
    print("you can ride")