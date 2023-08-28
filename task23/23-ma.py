def f(n):
    if n==51:
        return 1
    if n>51:
        return 0
    return f(n+2)+f(n+7)
print(f(7))