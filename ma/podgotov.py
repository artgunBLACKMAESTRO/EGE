import sys
sys.setrecursionlimit(9999)
def f(n):
    if n>=2222:
        return n
    if n<2222:
        return n**3+f(n+2)
print(f(4)-f(10))