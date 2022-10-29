def reverse(num):
    sum=0
    while num>0:
        a=num%10
        sum=sum*10+a
        num=num//10
    return sum
a=int(input())
if a==reverse(a):
    print("True")
else:
    print("False")