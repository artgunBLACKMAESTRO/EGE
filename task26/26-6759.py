with open('26-6759') as f:
    a=f.read()
a=a.split('\n')
a.pop(0)
a=list(map(int,a))
c=len(a)//3
a.sort()
print(len(a))
print(c)
for i in range(0,c):
    print(a[i])
    a.pop(i)
sum=sum(a)
print(sum)