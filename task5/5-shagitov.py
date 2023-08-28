c=0
for n in range(1,3000):
    a=oct(n)[2:]
    if n%7==0:
        a=a+a[-2:]
    else:
        a=a+oct((n%7)*7)[2:]
    if (int(a,8))<3000:
        c+=1
print(c)