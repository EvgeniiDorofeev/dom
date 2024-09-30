def generate_fizz_buzz_list(n):
    k=[]
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            k.append('FizzBuzz')
        elif i%3==0:
            k.append('Fizz')
        elif i%5==0:
            k.append('Buzz')
        else:
            k.append(i)
    return k

n=int(input())
print(generate_fizz_buzz_list(n))
