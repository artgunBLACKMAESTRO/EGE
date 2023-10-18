with open('26-ma') as f:
    a=f.read()
a=a.split('\n')
a.pop(0)
a=list(map(int,a))
b=[]
for i in range(len(a)-1):
    f=a[i]%2
    for z in range(i+1,len(a)):
        if f!=(a[z]%2) and ((a[z]+a[i]) in a):
            b.append(a[i]+a[z])
print(len(b),max(b))