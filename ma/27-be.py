import math
with open('27-be') as f:
    a=f.readlines()
def soch(n):
    return (math.factorial(n))/(math.factorial(2)*math.factorial(n-2))
a=list(map(int,a))
k=5
d=3
ost=[[] for _ in range(k)]
s=sum(a)
prefix=[a[0]]
for i in range(1,len(a)):
    prefix.append(prefix[-1]+a[i])
for i in range(len(a)):
    ost[prefix[i]%k].append(prefix[i])
otv=[0]*5
for i in range(len(ost)):
    for z in range(len(ost[i])-1):
        for n in range(z+1,len(ost[i])):
            if (ost[i][n]-ost[i][z])%d==0:
                otv[i]+=1
c=0
for i in otv:
    c+=soch(i)
print(c)