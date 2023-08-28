def f(n,c):
    if n==2 and c==1:
        return 1
    if n<2:
        return 0
    if n==6:
        c=1
    return f(n-2,c)+f(n//3,c)
print(f(200,0))