a=9**9999
s=''
while a!=0:
    s=str(a%7)+s
    a=a//7
print(s)
