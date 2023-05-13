with open('26-6759') as f:
    a=f.read()
a=a.split('\n')
a.pop(0)
a=list(map(int,a))
c=len(a)//3
a.sort(reverse=True)
for i in range(0,c):
    a.pop(i)
sum=sum(a)
print(sum)