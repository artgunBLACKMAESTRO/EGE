with open('17-6902') as f:
    a=f.read()
a=list(map(int,a.split('\n')))
c=0
for i in a:
    if abs(i)%5==0:
        c+=1
print(c)
b=[]
for i in range(len(a)-1):
    if ((str(a[i])[0]=='-' and str(a[i+1])[0]!='-') or (str(a[i])[0]!='-' and str(a[i+1])[0]=='-')) and ((a[i]+a[i+1])<c):
        b.append(a[i]+a[i+1])
print(len(b),max(b))