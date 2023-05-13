print('x y z w ans')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((((not y) and ((x<=w)!=z))==0) and (x+y+z+w)<=1) or ((((not y) and ((x<=w)!=z))==1) and (x+y+z+w)>=1):
                    print(x,y,z,w,((not y) and ((x<=w)!=z)))