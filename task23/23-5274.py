def f(n):
    if n == 1:
        return 1
    result = f(n - 1)
    if n % 3 == 0 and (str(n)[-1]=='1'):
        result += f((n-1)//10)
    if n % 5 == 0:
        result += f(n // 5)
    return result


print(f(410))
