N=int(input())
l=list(map(int,input().split()))[:N]
odd=0
for i in range(0,len(l)):
    if(i%2==0):
        pass
    else:
        odd+=l[i]
print(odd)
        