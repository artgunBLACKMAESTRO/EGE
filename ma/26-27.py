with open('26-27') as f:
    a=f.read()
a=a.split('\n')
k=int(a[0].split()[1])
a.pop(0)
boxes= []
for i in range(k):
    boxes.append([int(a[i].split()[0]),'R'])
    boxes.append([int(a[i].split()[1]),'B'])
for i in range(k,len(a)):
    boxes.append([int(a[i]), 'R'])
boxes=sorted(boxes,key=lambda x: -x[0])
b=[boxes[0]]
for i in range(1,len(boxes)):
    if (b[-1][0]-boxes[i][0])>=5 and boxes[i][1]!=b[-1][1]:
        b.append(boxes[i])
print(len(b),min(b))