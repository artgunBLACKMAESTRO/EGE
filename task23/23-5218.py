def complete(n: int,count: int):
    if n==200 and count<=3:
        return 1
    if count>3 or n>200:
        return 0
    return (complete(n+2, count) + complete(n*3, count + 1) + complete(n*5, count + 1))
print(complete(2,0))