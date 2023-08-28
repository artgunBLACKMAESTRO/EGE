f = open("27-8491A")
n = int(f.readline())
k = int(f.readline())
m = int(f.readline())

a = [int(i) for i in f.readlines()]
b = list(range(n))

for i in range(n - 1):
    for j in range(i + 1, n):
        if a[i] < a[j]:
            a[i], a[j] = a[j], a[i]
            b[i], b[j] = b[j], b[i]

ans = [a[0]]
ans_ind = [b[0]]
for i in range(n):
    flag = True
    for j in ans_ind:
        if abs(b[i] - j) < 93:
            flag = False
    if flag:
        ans.append(a[i])
        ans_ind.append(b[i])

print(ans)
print(sum(ans) - min(ans))