with open('test') as f:
    a=f.read()
a=list(map(int,a.split('\n')))
k=a.pop(0)
a.pop(0)
mx=[a[0]]*len(a)
dp=[10**10]*len(a)
for i in range(1,len(a)):
    mx[i]=min(mx[i-1],a[i])
print(mx)
for i in range(k,len(a)):
    if a[i]!=10**10:
        dp[i]=min(dp[i-1],a[i]*mx[i-k])
    else:
        dp[i]=min(dp[i-1])
print(dp)
z=10**10
for i in range(k,len(a)):
    if dp[i-k]!=10**10:
        z=min(z,dp[i-k]*a[i])
print(z)