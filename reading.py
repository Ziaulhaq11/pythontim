v = open('file.txt','r')

f = v.readlines()
new = []
for line in f:
    new.append(line.strip())
print(new)
