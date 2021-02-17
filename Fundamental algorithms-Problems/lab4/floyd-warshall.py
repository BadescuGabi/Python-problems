from heapq import *

def citire(orientat=1, nume_fisier="graf.txt"):
    n = 0
    with open("graf.txt") as fisier:
        linie = fisier.readline()
        n, m = [int(z) for z in linie.split()]
        a =[]
        for linie in fisier:
            x, y,c = [int(z) for z in linie.split()]
            a.append([x,y,c])

    return a,n

def matrice(lista,noduri):
    a = [[0 for i in range(n+1)] for j in range(n+1)]
    for i in lista:
        if i!=[]:
            a[i[0]][i[1]]=i[2]
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j]==0 and i!=j:
                a[i][j]=999999
    return a

c=citire()[0]
n=citire()[1]

#print(d)
#print(c[0])
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
def floydWarshall(graph,n): #n=no. of vertex
    dist=graph
    for k in range(n+1):
        for i in range(n+1):
            for j in range(n+1):
                dist[i][j] = min(dist[i][j] ,dist[i][k]+ dist[k][j])
    return dist
d=floydWarshall(matrice(c,n),n)
print(d)
