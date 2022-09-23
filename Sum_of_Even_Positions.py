N=int(input())
l=list(map(int,input().split()))[:N]
even=odd=0
for i in range(0,len(l)):
    if(i % 2==0):
        even+=l[i]
    else:
        pass
print(even)