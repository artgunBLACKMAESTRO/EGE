import sys
sys.setrecursionlimit(3000)
def f(n):
    print(n)
    if n==3000:
        return 8130
    if n==3001:
        return 4066
    if n==3002:
        return 4064
    if n==3003:
        return 8122
    if n>3456:
        return n+1
    if n<=3456 and n%3==0:
        return f(n+1)+f(n+2)
    if n<=3456 and n%3!=0:
        return f(n+n%3)+2
print(f(12)-f(17))