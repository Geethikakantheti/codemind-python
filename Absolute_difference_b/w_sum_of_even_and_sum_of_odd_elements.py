n=int(input())
l=list(map(int,input().split()))[:n]
even=odd=0
for i in range(0,len(l)):
    if(l[i]%2==0):
        even+=l[i]
    else:
        odd+=l[i]
if even>odd:
    print(even-odd)
else:
    print(odd-even)