import functools
b=[]
@functools.lru_cache(True)
def f(n):
    if n==0:
        return 3
    if 0<n<=15:
        return f(n-1)
    if 15<n<100:
        return 2.5*f(n-3)
    if n>=100:
        return 3.3*f(n-2)
a=str(f(100))
for i in range(len(a)):
    if a[i]=='.':
        print(a[i+1])
        break