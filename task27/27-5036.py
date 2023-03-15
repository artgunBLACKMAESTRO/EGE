with open('27-5036A') as f:
    a=f.read()
a=list(map(int,a.split('\n')))
c=0
a.pop(0)
result=999999
for i in range(len(a)):
    c+=a[i-len(a)//2]*len(a)//2
    for j in range(1,len(a)//2):
        c+=a[(i+j)%len(a)]*j+a[i-j]*j
    if c<result:
        result=c
        lk=i
    c=0
print(lk+1)


