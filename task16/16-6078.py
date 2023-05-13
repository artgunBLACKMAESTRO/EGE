import functools
import sys
sys.setrecursionlimit(9999)
@functools.lru_cache()
def f(a,b):
    if a==0 and b==0:
        return 0
    if a>b:
        return f(a-1,b)+b
    else:
        return f(a,b-1)+a
k=0
for a in range(1000):
    for b in range(100):
        if f(a,b)==333396000:
            k+=1
            break
print(k)