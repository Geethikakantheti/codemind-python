N=int(input())
k=N*N
s=0
for i in range(N):
    r=k%10
    s+=r
    l=k//10
if s==N:
    print("Neon Number")
else:
    print("Not Neon Number")