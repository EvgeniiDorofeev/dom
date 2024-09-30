with open('lorem.txt', mode='r', encoding='utf-8') as file:
    words={}
    res = file.read().upper().split()
    #print(res)
    for i in res:
        words.setdefault(i, 0)
        words[i] += 1
    print(words)