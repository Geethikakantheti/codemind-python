n=int(input())
k=list(map(int,input().split()))[:n]
even=odd=0
for i in range(0,len(k)):
    if(i%2==0): #
        even+=k[i]
    else :
        odd+=k[i]
    
if even>odd:
    print(even-odd)
else:
    print(odd-even)
        
        