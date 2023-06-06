with open('27b_8483.txt') as f:
    a=f.read().strip()
def test(ind,i):
    return a[i-k]!=p and abs(ind-(i-k))>=(k)
a=a.split('\n')
a.pop(0)
k=int(a.pop(0))
mx=0
sum=0
a=list(map(int,a))
p=max(a[k:])
ind=a.index(p)
for i in range(k,len(a)):
    if test(ind,i):
        mx=max(mx,a[i-k])
    if a[i]!=p and abs(ind-i)>=(k):
        sum=max(sum,mx+a[i])
print(sum+p)