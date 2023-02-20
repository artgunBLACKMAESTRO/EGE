def prost(x):
    return all([x%i!=0 for i in range(2,int(x**(0.5))+1)])
b=set()
def f(x,y,count):
    if count==5:
        if prost(x) and prost(y):
            a=(x,y)
            b.add(a)
            return 1
        else:
            return 0

    return f(x+3,y,count+1) + f(x*4,y,count+1) + f(x,y+5,count+1) + f(x,y*2,count+1)
f(2,3,0)
print(len(b))
