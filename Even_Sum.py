N=int(input())
l=list(map(int,input().split()))
even=odd=0
for i in range(0,len(l)):
    if(l[i]%2==0):
        even+=l[i]
    else:
        pass
print(even)