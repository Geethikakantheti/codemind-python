N=int(input())
l=list(map(int,input().split()))[:N]
even=odd=0
for i in range(0,len(l)):
    if(l[i] % 2==0):
        pass
    else:
        odd+=l[i]
print(odd)