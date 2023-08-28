f=open('1111')
m=open('2323.txt')
data1=f.read().strip().split('\n')
data2=m.read().strip().split('\n')
for i in range(len(data1)):
    data1[i]=list(map(int,data1[i].split('\t')))
for i in range(len(data2)):
    data2[i] = list(map(int, data2[i].split('\t')))
i = len(data2)-1
j = len(data2[i])-1
s=[]
x=0
while i!=-1 or j!=-1:
    a=0
    b=0
    c=0
    d=0
    if i-1>-1 and j+1<len(data1[i])-1:
        a=data2[i-1][j+1]
        b=data2[i-1][j]
    elif i-1>-1:
        b = data2[i - 1][j]
    if i-1>-1 and j-1>-1:
        c=data2[i-1][j-1]
        d=data2[i][j-1]
    elif j-1>-1:
        d = data2[i][j - 1]
    if a>b and a>d and a>c:
        s.append(data1[i-1][j+1])
        i=i-1
        j=j+1
    elif b>a and b>c and b>d:
        s.append(data1[i-1][j])
        i = i - 1
    elif d>a and d>c and d>b:
        s.append(data1[i][j-1])
        j = j - 1
    elif c>a and c>b and c>d:
        s.append(data1[i-1][j-1])
        i = i - 1
        j=j-1
    print(a, b, c, d)
    x+=1
    if x==100:
        break
print(s)
c=0
for i in s:
    if i%2==1:
        c+=1
print(c)