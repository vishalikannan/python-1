import sys,string, math,itertools

n = int(input())
L = [ int(x) for x in input().split()]
L2 = []
for i in range(0,n) :
    L2.append(sum(L[i:]))
print(*L2)










