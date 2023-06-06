def f(n,c,m):
    if n==2 and c==1 and m==1:
        return 1
    if n<2:
        return 0
    if n==50:
        return 0
    if n==73:
        c=1
    if n==22:
        m=1
    return f(n-5,c,m)+f(n-4,c,m)+f(n/2,c,m)
print(f(100,0,0))