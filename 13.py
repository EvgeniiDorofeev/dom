file = open('lorem.txt', mode='r', encoding='utf-8')
#print(file.read())
s=[]
for i in file:
    words=i.lower().split()
    for word in words:
        if word in s:
            continue
        else:
            s.append(word)
print(len(s))