p,r,t=map(int,input().split())
f=(1+r/100)**t
g=f*p
print("{0:.2f}".format(g))