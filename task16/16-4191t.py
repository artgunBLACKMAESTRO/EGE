n = 100
k = 0
while n >= 0:
    if n == 0:
        k += 3
    if 0 < n <= 15:
        n = n - 1
        k += n
    if 15 < n < 100:
        n = 2.5 * (n - 3)
        k += n
    if n >= 100:
        n = 3.3 * (n - 2)
        k += n
print(k)
