n=int(input())
k=0
p=0
for i in range(n+1,2*n):
    for j in range(2,i-1):
        if i%j==0:
            k=k+1
            #print(k)
    if k==0:
        p=p+1
        #print(i,j)
        k=0
    k=0
print(p)