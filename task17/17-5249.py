a=open('17-5249')
d=a.readlines()
a.close()
d=list(map(int,d))
average=0
count=0
for i in range(len(d)):
    if d[i]%50==0:
        count+=1
        average+=d[i]
average=average/count
b=[]
for i in range(len(d)-2):
    if ((len(str((d[i]+d[i+1])**(0.5)).split('.')[1]))==1) and ((len(str((d[i]+d[i+2])**(0.5)).split('.')[1]))==1) and ((len(str((d[i+1]+d[i+2])**(0.5)).split('.')[1]))==1) and (min(d[i+2]+d[i+1],d[i]+d[i+2],d[i]+d[i+1])>average):
        b.append(d[i]+d[i+1]+d[i+2])
print(len(b),min(b))