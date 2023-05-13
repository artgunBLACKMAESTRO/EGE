with open('27-4280A') as f:
    a=f.read()
a=[int(i) for i in a.split('\n')]
a.pop(0)
sum=0
D=39
a2=[0]*D
a1=[0]*D
l=0
for i in range(len(a)):
    sum+=a[i]
    ostat=sum%D
    if ostat!=0 and a1[ostat]==0:
        a1[ostat]=sum
        a2[ostat]=i
    elif (i-a2[ostat])<=20:
        l+=1

print(l)