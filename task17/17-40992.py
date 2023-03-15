with open('17-40992') as f:
    a=f.read()
a=list(map(int,a.split('\n')))
v=0
n=0
for i in range(len(a)):
    if a[i]%2==1:
        v+=a[i]
        n+=1
v=v/n
b=[]
for i in range(len(a)-1):
    if (a[i]%5==0 or a[i+1]%5==0) and (a[i]<v or a[i+1]<v):
        b.append(a[i]+a[i+1])
print(len(b),max(b))