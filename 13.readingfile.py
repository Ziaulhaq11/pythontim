file = open('file.txt', 'r')
f = file.readlines()
t = file.truncate
print(t)


print(f)
newlist = []
for line in f:
    if line[-1] == '\n':
        newlist.append(line[:-1])
    else:
        newlist.append(line)
print(newlist)

#default \n will be pint
#after using for loop we remove \n but last digit excluded (not in my case)
#for that we use if condition

newlist2=[]
for line in f:
    newlist2.append(line)

print(newlist2)

#other method
newlist1=[]
for line in f:
    newlist1.append(line.strip())

print(newlist1)
