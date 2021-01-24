from heapq import *


def citire(nume_fisier="graf.txt"):
    global n

    with open(nume_fisier) as f:
        linie = f.readline()
        n, m = (int(z) for z in linie.split())
        la = []
        for linie in f:
            x, y, c = (int(z) for z in linie.split())
            la.append((x, y, c))
        la.sort(key=lambda x: x[2])
    return la, n


muchii_disp = []
c = citire()[0]
n=citire()[1]
viz = []
tata = [0] * (citire()[1] + 1)
h = [0] * (citire()[1] + 1)
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

def kruskal(c):
    cost=0
    nr_muchii=0
    arbore=[]
    for i in c:
        if i != []:
            if Reprez(i[0]) != Reprez(i[1]):
                Reuneste(i[0], i[1])
                arbore.append(i)
                cost += i[2]
                nr_muchii += 1
                if nr_muchii == n - 1:
                    return arbore,cost

arbor=kruskal(c)
print(arbor)
n = int(input())
n1 = int(input())
cos = int(input())
m = (n, n1, cos)
c.append(m)
c.sort(key=lambda x:x[2])
tata = [0] * (citire()[1] + 1)
h = [0] * (citire()[1] + 1) #reinitializare
arbore1=kruskal(c)

print(arbore1)
a=set(arbor[0])
b=set(arbore1[0])
print(a.difference(b))

'''
scirre fisier:
n-nr noduri m-numar muchii
muchii p-zis
5 7
1 4 1
1 3 5
1 2 10
2 3 2
4 2 6
4 5 12
5 2 11
'''
