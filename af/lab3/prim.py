from heapq import *

def citire(nume_fisier="graf.txt"):
    global n
    a = []
    with open(nume_fisier) as f:
        linie = f.readline()
        n, m = (int(z) for z in linie.split())
        la = [[] for i in range(n + 1)]
        for linie in f:
            x, y, c = (int(z) for z in linie.split())
            la[x].append((c,y, x))
            la[y].append((c, x,y))
    return la, n


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


def parc(graph, cur, nr_muchii=0):
    global cost
    muchii_disp.extend(graph[cur])
    heapify(muchii_disp)
    element_to_be_removed = [i for i in graph[muchii_disp[0][1]] if cur==i[1]]
    #print(graph[muchii_disp[0][1]])
    #print(element_to_be_removed)
    graph[muchii_disp[0][1]].remove(element_to_be_removed[0])
    for i in muchii_disp:
        if Reprez(i[1]) != Reprez(cur):
            Reuneste(muchii_disp[0][1], cur)
            arbore.append(i)
            cost += i[0]
            nr_muchii += 1
            if nr_muchii == citire()[1]-1:
                break
            parc(graph,heappop(muchii_disp)[1],nr_muchii)


    return (arbore,cost)



ar=parc(c, 1)
print(ar)
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
