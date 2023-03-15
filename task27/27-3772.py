with open('27-3772B') as f:
    a=f.read()
a=a.split('\n')
a.pop(0)
a=list(map(int,a))
n=min(a)
a.remove(n)
b=min(a)
a.remove(b)
c=n+b
k=[99999999999]*3
for i in a:
    k[i%3]=min(i,k[i%3])
print(k[2],b,n)
print(c+k[2])
#A - 963
#B - 302658