f=open('26-11.txt')
lines=f.read().split('\n')
data=[]
for i in lines:
    s=[int(i.split()[0]),i.split()[1]]
    data.append(s)
data=sorted(data,key=lambda x:(x[0],x[1]))
su=0
a=0
data1=[]
for i in data:
    if i[1]=='A':
        data1.append(i)
i=0
while i!=(len(data)-2) and su+data[i][0]<=982000:
    if data[i][1]=='A':
        a+=1
    su+=data[i][0]
    i+=1
print(data[i],data[i+1],data[i-1])
print(su,i-1,a,data1[a])