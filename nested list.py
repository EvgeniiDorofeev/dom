a = []
k = 0
s = 0
o = 0
r = 0
p = 0
q = 0
n, m = map(int, input().split())
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        s = s + a[i][j]
        if a[i][j] > k:
            k = a[i][j]
            # print('q=',q)
    # print('s=',s)
    # print('i=',i)
    # print('k=',k)
    if k > p:
        q = i
        p = k
        r = s
    elif k == p and s > r:
        q = i
    # print('q=',q)
    # r=s
    # p=k
    s = 0
    k = 0
    # print(p)

# print(k)
print(q)
