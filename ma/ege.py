with open('test') as f:
    a=f.read()
a=list(map(int,a.split('\n')))
p=a.pop(0)
dp=[-1000000000]*len(a)
mx=[a[0]]*len(a)
for i in range(1,len(a)):
    mx[i]=max(mx[i-1],a[i])
for i in range(p,len(a)):
    dp[i]=max(dp[i-1],a[i]+mx[i-p])
an=-1000000000000
for i in range(p,len(a)):
    an=max(an,a[i]+dp[i-p])
print(an)