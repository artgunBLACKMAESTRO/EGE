c=0
for x in range(100):
    for y in range(100):
        for z in range(100):
            a='0'+x*'1'+y*'2'+z*'3'+'0'
            while '00' not in a:
                a=a.replace('01','210',1)
                a=a.replace('02','3101',1)
                a=a.replace('03','2012',1)
            c+=1
            if (a.count('1')==56) and (a.count('2')==44) and (a.count('3')==19):
                print(x,y,z)
