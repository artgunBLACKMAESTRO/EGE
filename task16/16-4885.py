def f(n):
    if n<=1:
        return 1
    if n>1 and n%2==0:
        return 11*n+f(n-1)
    else:
        return 11*f(n-2)+n
c=0
for i in range(35,51):
    m=f(i)
    if m%2==0:
        c+=m
print(len(str(c)))