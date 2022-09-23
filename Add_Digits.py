n=int(input())
s=n
while s>=9:
    s=0
    while n:
        r=n%10
        s+=r
        n=n//10
    n=s
print(n)