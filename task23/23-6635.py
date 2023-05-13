k=0
b=set()
def f(n,c):
    global b
    if n<0 and c==13:
        b.add(n)
        return 0
    if c>13:
        return 0
    return f(n-3,c+1)+f(n*(-3),c+1)
f(333,0)
print(len(b))