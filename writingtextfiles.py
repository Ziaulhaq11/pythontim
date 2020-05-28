f = open('sfile.txt', 'w')

f.write('python\n')
f.write('i am learing how to write')
#we overwrite hello in text file

f.close()

#.find, .count

string = 'hello i am zia zia zia'
print(string.find('zia'))
print(string.count('zia'))

text = input("etnter something")

if text.count('_')>0:
    print('not good')
else:
    print("good")


