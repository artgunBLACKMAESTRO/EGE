import sys
import functools
sys.setrecursionlimit(9999)
@functools.lru_cache(True)
def f(n):
    if n<2:
        return 7
    if n>1:
        return 7*f(n-2)
print(f(12950)/7**6473)