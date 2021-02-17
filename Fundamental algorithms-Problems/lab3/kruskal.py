from heapq import *

def citire(nume_fisier="graf.txt"):
    global n

    with open(nume_fisier) as f:
        linie = f.readline()
        n, m = (int(z) for z in linie.split())
        la=[]
        for linie in f:
            x, y, c = (int(z) for z in linie.split())
            la.append((x,y,c))
        la.sort(key=lambda x:x[2])
    return la,n


muchii_disp = []
c = citire()[0]
viz = []
tata = [0] * (citire()[1] + 1)
h = [0] * (citire()[1] + 1)
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



for i in c:
    if i!=[]:
         if Reprez(i[0]) != Reprez(i[1]):
                Reuneste(i[0],i[1])
                arbore.append(i)
                cost += i[2]
                nr_muchii += 1
                if nr_muchii == citire()[1]-1:
                    break
print(arbore)
print(cost)
'''
scirre fisier:
n-nr noduri m-numar muchii
muchii p-zis
6 9
1 2 10
1 3 11
2 5 10
5 3 8
2 4 3
2 6 5
5 6 20
3 6 9
4 6 2
'''
