x,y=map(int,input().split())
p=max(x,y)
while p>0:
    if p%x==0 and p%y==0:
        print(p)
        break;
    p=p+1
    