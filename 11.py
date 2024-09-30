file = open('numbers.txt', mode='r', encoding='utf-8')
#print(file.read())
k=0
s=0
for i in file:
    #print(i, len(i)-1)
    if len(i)==4:
        k=k+1
    if len(i)==3:
        s=s+int(i)
print(k)
print(s)