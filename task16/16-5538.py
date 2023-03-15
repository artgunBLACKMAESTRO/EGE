import sys
import functools
sys.setrecursionlimit(9999)
d=[0]*99999
def op(n):
    result = 1
    while n != 1:
        result *= (2 * n - 1)
        n -= 1
    return result

@functools.lru_cache()
def f(n):
    if n==1:
        return 1
    if n>1:
        return (2*n-1)*f(n-1)
print(f(20))
print(op(3516)/op(3513))
