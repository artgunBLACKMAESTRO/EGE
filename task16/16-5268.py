d={}
def F(n):
    global d
    q = 0
    n = str(n)
    for i in range(len(n)):
        q += int(n[i])
    n = int(n)
    if n < 3:
        return 1
    if n > 2 and q%2==0:
        if n not in d:
            d[n]=F(n-1)-F(n-2)
        return d[n]
    if n > 2 and q%2==1:
        if n not in d:
            d[n]=F(n-1)+F(n//2)
        return d[n]
print(F(100))
