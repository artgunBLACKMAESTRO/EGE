import math
n=2
e=float(input())
x=float(input())
sum=0
an=((x**(n*2-1))/(2*n-1))*((-1)**(n-1))
print(an)
while abs(an)>=e:
    sum+=an
    n+=1
    an=((x**(n*2-1))/(2*n-1))*((-1)**(n-1))
print(sum,math.atan(x))