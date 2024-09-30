def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

s=gcd (a, b)
print(s)