n=int(input())
x=len(str(n))
square=n**2
l=square%pow(10,x)
if l==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")