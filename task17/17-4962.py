with open('17-4962') as f:
    a=f.readlines()
a=[int(a[i]) for i in range(len(a))]
b=[]
for i in range(len(a)-1):
    m=abs(a[i]) + abs(a[i+1])
    if m>17043 and m%3==0:
       b.append(a[i]+a[i+1])
print(len(b),min(b))