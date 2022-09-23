N=int(input())
s=N
while s>=9:
    s=0
    while N:
        r=N%10
        s+=r
        N=N//10
    N=s
print(N)