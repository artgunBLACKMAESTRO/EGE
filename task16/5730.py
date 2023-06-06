import sys

sys.setrecursionlimit(9999)


def F(n):
    if n == 5:
        return n
    if n < 10000 and n % 6 == 0:
        return n / 6 + F(n / 6 + 2)
    if n < 10000 and n % 6 != 0:
        return n + F(n + 2)



print(F(264))
