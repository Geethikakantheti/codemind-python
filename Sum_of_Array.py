N=int(input())
l=list(map(int,input().split()))[:N]
sum=0
for i in range(0,len(l)):
    sum+=l[i]
print(sum)