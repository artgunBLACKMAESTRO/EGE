with open('27test-lshastin') as f:
    a=f.read()
a=a.split('\n')
a.pop(0)
a=list(map(int,a))
k=a.pop(0)
c=0
a=[x%2 for x in a]
for i in range(len(a)):
    b=[]
    for z in range(i,len(a)):
        b.append(a[z])
        if (b.count(1)==b.count(0)) and (len(b)>=k):
            c+=1
print(c)