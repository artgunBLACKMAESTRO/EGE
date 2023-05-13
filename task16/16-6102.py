import functools
@functools.lru_cache()
def f(n):
    if n<10:
        return n
    if 10 <= n < 1000:
        return f(n//10)+f(n%10)
    if n>=1000:
        return f(n//1000)-f(n%1000)
k=0
for i in range(10**6+1):
    if f(i)==0:
        k+=1
print(k)