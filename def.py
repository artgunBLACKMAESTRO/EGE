import sys
sys.setrecursionlimit(999999)
v=[-1]*99999999
b=[-1]*99999999
def f(n):
    if n==0:
        return 0
    if n>=1000000000:
        print(n)
        print(len(b))
        print(n-1500000001)
        if b[n-1500000001]==-1:
            if n%3!=0:
                b[n - 1500000001] = f(n - 1)+1
                return b[n - 1500000001]
            if n>0 and n%3==0:
                b[n - 1500000001]=f(n / 3)
                return b[n-1500000001]
    else:
        if a[n]==-1:
            if n%3!=0:
                a[n] = f(n - 1)+1
                return a[n]
            if n>0 and n%3==0:
                a[n]=f(n / 3)
                return a[n]
f(1000000000)