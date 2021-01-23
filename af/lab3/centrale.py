from heapq import *
from math import sqrt

def citire(nume_fisier="graf.txt"):
    global n
    a = []
    with open(nume_fisier) as f:
        linie = f.readline()
        n, m,e = (int(z) for z in linie.split())
        blocuri=[]
        centrale=[]
        muchii=[]
        i=0
        for i in range(m+n+e):
            lini=f.readline().split()
            linie=[int(z) for z in lini]
            if linie=='':
                return (centrale, blocuri, muchii)
            i+=1
            if i<=n:
                blocuri.append(linie)
                centrale.append(linie)
            elif i<=n+m:
                blocuri.append(linie)
            elif i>n+m:
                muchii.append(linie)

    return ( blocuri,muchii,centrale)

a=citire()
#print(a[0])
#print(a[1])

centrale=a[0] #nu sunt centrale, sunt toate cladirile
cladiri=a[1]
centrale_adv=a[2]

for i in cladiri:
    if i[0]<=len(centrale_adv) and i[1]<=len(centrale_adv):
        i.append(0)#hardcodat
    i.append(sqrt((centrale[i[1]-1][1]-centrale[i[0]-1][1])**2+(centrale[i[1]-1][0]-centrale[i[0]-1][0])**2))

viz = []
tata = [0] * (len(centrale)+1)
h = [0] * (len(centrale)+1)
arbore = []
cost = 0
nr_muchii = 0
def Reprez(u):
    while (tata[u] != 0):
        u = tata[u]
    return u


def Reuneste(u, v):
    ru = 0
    rv = 0
    ru = Reprez(u)
    rv = Reprez(v)
    if (h[ru] > h[rv]):
        tata[rv] = ru
    else:
        tata[ru] = rv
        if (h[ru] == h[rv]):
            h[rv] = h[rv] + 1


cladiri.sort(key=lambda x:x[2])
print(cladiri)
for i in cladiri:
    if i!=[]:
         if Reprez(i[0]) != Reprez(i[1]):
                Reuneste(i[0],i[1])
                arbore.append(i)
                cost += i[2]
                nr_muchii += 1
                if nr_muchii == len(cladiri)-1:
                    break
print(arbore)
print(cost)
#centrale=cladiri!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''
2 5 9
0 0
0 4
1 4
1 3
1 1
1 0
3 0
1 2
2 3
3 4
4 5
5 6
1 6
3 5
5 7
6 7

'''
