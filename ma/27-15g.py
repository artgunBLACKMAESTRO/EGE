def f(n):
    m=1
    for i in range(2,n+1):
        m=m*i
    return m

y=open('27-16_A.txt')
data=y.read().strip().split('\n')
a=list(map(int,data))
a.pop(0)
a.sort()
s=[]
for i in a:
    if i<0:
        s.append(-(abs(i)%43))
    else:
        s.append(i%43)
count=0
for i in range(len(s)-1):
    for h in range(i,len(s)):
        if (s[h]-s[i])%43==0:
            for j in range(1,h-i):
                count+=(f(h-i-1)//(f(j)*f(h-i-1-j)))
print(count)