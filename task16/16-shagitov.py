import sys
sys.setrecursionlimit(9999)
def h(x):
    if x>=4040:
        return x
    if x<4040:
        return x+4+h(x+4)
print(h(3)-h(15))