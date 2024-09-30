with open('words.txt', mode='r', encoding='utf-8') as file:
    words=[]
    res = file.read().upper().split()
    #print(res)
    for i in res:
        if i[-2:]=='ЕЯ':
            words.append(i)
s=set(words)
t=list(s)
s=sorted(t, key=lambda x:(len(x),x))

for j in s:
    print(j)
