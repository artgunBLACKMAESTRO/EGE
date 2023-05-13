with open('27-4278B') as f:
    a=f.read()
a=a.split('\n')
a.pop(0)
a=list(map(int,a))
sum=0
d=71
k=0
l=[[] for i in range(d)]
for i in range(len(a)):
    sum+=a[i]
    if sum%d==0:
        k+=1
    if not(l[sum%d]):
        l[sum%d].append(1)
    else:
        k+=l[sum%d][0]
        l[sum%d][0]+=1
print(k)
