def f(n,c):
    if n==17 and c==1:
        return 1
    if n>17 or n==12:
        return 0
    if n==9:
        c=1
    return f(n+1,c)+f(n+2,c)+f(n*2,c)
print(f(2,0))