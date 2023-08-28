with open('test') as f:
    a=f.read()
a='3k2553k52k235k3'
k=3
kmin=float('inf')
for i in range(len(a)):
    s=''
    for j in range(i,len(a)):
        s+=a[j]
        if s.count('k')==k:
            kmin=min(len(s),kmin)
            break
print(kmin)