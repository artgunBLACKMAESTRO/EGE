def F(n):
    q = 0
    n = str(n)
    for i in range(len(n)):
        q += int(n[i])
    n = int(n)
    if n < 3:
        return 1
    if n == 60:
        return -1
    if n == 69:
        return 12
    if n == 70:
        return 14
    if n == 35:
        return 2
    if n > 2 and q%2==0:
        return F(n-1)-F(n-2)
    if n > 2 and q%2==1:
        return F(n-1)+F(n//2)
print(F(100))
