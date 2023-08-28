from itertools import combinations
with open('27B-shastin') as f:
    a=f.read()
a=a.split('\n')
a=[list(map(int,i.split())) for i in a]
i=0
while i!=len(a):
    if a[i][0]%2==1:
        a.pop(i)
    else:
        i+=1
c=combinations(a,2)
i=len(a)-2
otvet=0
while i!=0:
    c = combinations(a, i)
    i-=1
    for z in c:
        summ = 0
        b=0
        m=0
        for k in z:
            summ+=sum(k)
            b+=max(k)
            m+=min(k)
        if bin(summ)[-4:]=='1111' and b%2==1 and m%2==0:
            otvet=max(otvet,summ)
            print(otvet)
print(otvet)

