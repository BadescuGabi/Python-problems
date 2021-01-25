from heapq import *

def citire(orientat=1, nume_fisier="graf.txt"):
    n = 0
    with open("graf.txt") as fisier:
        linie = fisier.readline()
        n, m = [int(z) for z in linie.split()]
        a = [[] for i in range(n + 1)]
        for linie in fisier:
            x, y,c = [int(z) for z in linie.split()]
            a[x].append((y,c))
            if not orientat:
                a[y].append((x,c))
    return a,n


c=citire()
print(c[0])
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

def dijsktra(graph, start):
  d = [0] *(citire()[1]+1)
  tata = [0] *(citire()[1]+1)
  d[1]=start
  j=1
  noduri = [i for i in range(1,c[1]+1)]
  while noduri:
    min_nod = None
    for nod in noduri:
      if d[nod]!=0:
        if min_nod is None:
          min_nod = nod
        elif d[nod] < d[min_nod]:
          min_nod = nod

    if min_nod is None:
      break

    noduri.remove(min_nod)
    if min_nod==start:
        cost_cur = d[min_nod]-1
    else:
        cost_cur=d[min_nod]
    for edge in graph[min_nod]:
      cost = cost_cur + edge[1]
      if edge[0] not in tata or cost < d[edge[0]]or d[edge[0]]==0:
            d[edge[0]] = cost
            tata[edge[0]] = min_nod

  return d, tata

a=dijsktra(c[0],1)
print(a)
'''
6 9
1 2 15
1 3 11
5 2 10
3 5 8
2 4 3
2 6 2
6 2 5
5 6 20
3 6 9
4 6 1
6 4 2
'''
