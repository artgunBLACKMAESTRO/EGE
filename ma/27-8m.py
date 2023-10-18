def masha():
    f=open('27-8test')
    data=f.read().strip().split('\n')
    a=list(map(int,data))
    s=[]
    for i in range(80):
        s.append([])
    for i in a:
        s[i%80].append(i)
    t=6

    for i in range(1,40):
        for j in s[i]:
            for k in s[80-i]:
                if not(j<=50 and k<=50):
                    t+=1

    print(t)
def tema():
    with open('27-8test') as f:
        a = f.read()
    a = a.split('\n')
    a.pop(0)
    a = list(map(int, a))
    c = 0
    d = [[] for _ in range(80)]
    for i in range(len(a)):
        d[a[i] % 80].append(a[i] > 50)

    for i in range(1, 40):
        for k in d[i]:
            for l in d[80 - i]:
                if k or l:
                    c += 1

    for i in range(len(d[0]) - 1):
        for z in range(i + 1, len(d[0])):
            if d[0][i] or d[0][z]:
                c += 1

    for i in range(len(d[40]) - 1):
        for z in range(i + 1, len(d[40])):
            if d[40][i] or d[40][z]:
                c += 1
    print(c)
masha()
tema()