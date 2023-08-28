def f(n,c):
    if n==100 and c==1:
        return 1
    if n>100:
        return 0
    if n==40:
        return 0
    if n==20:
        c=1
    return f(n+1,c)+f(n*3,c)+f(n*5,c)
print(f(1,0))