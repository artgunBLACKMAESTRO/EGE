def f(n):
    if n<3:
        return 1
    if n>2 and n%2==0:
        return f(n-1)+n
    if n>2 and n%2==1:
        return f(n-2)+2*n
print(f(23)-f(21))