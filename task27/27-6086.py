with open('27-6086A') as f:
    a=f.read()
a=a.split('\n')
a=list(map(int,a))
k=0
a.pop(0)
for i in range(len(a)-18):
    for j in range(i+18,len(a)):
        if (a[i]+a[j])%6==0 and (a[i]*a[j])%3888==0:
            k+=1
print(k)
