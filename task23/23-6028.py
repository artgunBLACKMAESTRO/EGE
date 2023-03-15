def f(n,c):
    if n==39 and c:
        return 1
    if n>39:
        return 0
    if n==26:
        return 0
    if n==11:
        c=True
    return f(n+1,c)+f(n*2,c)
print(f(2,False))