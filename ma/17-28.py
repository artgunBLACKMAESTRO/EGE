a=open('17-28')
d=a.read()
a.close()
m=-999999
d=list(map(int,d.split('\n')))
m=max(d)
b=[]
c=0
for i in d:
    if abs(i)%100==0:
        c+=1
for i in range(len(d)-1):
    if (str(d[i])[0]=='-' or str(d[i+1])[0]=='-')  and (d[i]+d[i+1])<c:
        print(d[i],d[i+1],c)
        b.append(d[i]+d[i+1])
print(len(b),abs(max(b)))