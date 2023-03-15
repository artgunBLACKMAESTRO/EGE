a=5*216**155+4*36**156-4*6**157-2023
b=[]
while a:
    b.append(a%6)
    a=a//6
print(b)