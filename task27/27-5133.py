with open('27-5133A') as f:
    a=f.read()
a=a.split('\n')
a=list(map(int,a))
k=0
a.pop(0)
for i in range(len(a)):
    c=1
    for j in range(i,len(a)):
        c*=a[j]
        if c%858967!=0:
            k+=1
print(k)