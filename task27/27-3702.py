with open('27-3702B') as f:
    a=f.read()
a=a.split('\n')
a.pop(0)
a=[list(map(int,a[i].split(' '))) for i in range(len(a))]
minresult=0
diff=[]
chet=0
nechet=0
for i in range(len(a)):
    minresult+=min(a[i])
    if min(a[i])%2==0:
        chet+=1
    else:
        nechet+=1
    if (max(a[i])-min(a[i]))%2==1:
        diff.append(max(a[i])-min(a[i]))
print(minresult+min(diff))
#A-62276
#B-190343719
