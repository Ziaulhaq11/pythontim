#try and except statements

text = input('Username : ')
try:
    number = int(text)
    print(number)
except :
    print('Enter non string')
    