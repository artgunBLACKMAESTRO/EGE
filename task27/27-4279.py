with open('27-4279B') as f:
    a=f.read()
a=[int(i) for i in a.split('\n')]
a.pop(0)
sum=0
mxsum=0
mxlen=0
D=93
a2=[0]*D
a1=[0]*D
for i in range(len(a)):
    sum+=a[i]
    ostat=sum%D
    if a1[ostat]==0 and ostat!=0:
        a1[ostat]=sum
        a2[ostat]=i
    elif mxsum<(sum-a1[ostat]) and (sum-a1[ostat])%2==1:
        mxsum=sum-a1[ostat]
        mxlen=i-a2[ostat]
    elif mxsum==sum-a1[ostat] and (sum-a1[ostat])%2==1:
        mxlen=max(mxlen,i-a2[ostat])
print(mxsum)