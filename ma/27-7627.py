with open('27_B_7627.txt') as f:
    a=f.read().strip()
a=list(map(int,a.split('\n')))
k=a.pop(0)
a.pop(0)
sum=0
m=0
for i in range(k,len(a)):
    m=max(m,a[i-k])
    sum=max(sum,a[i]+m)
print(sum)