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

    return a,n,m

graph=citire()[0]
nr_noduri=citire()[1]
nr_muchii=citire()[2]


def BellmanFord(graph, noduri, muchii, start):
    
    dis = [99999999999] *( noduri-1)

    dis[start] = 0
    for i in range(noduri-1):
        for j in range(muchii):
            if dis[graph[j][0]] + graph[j][2] < dis[graph[j][1]]:
                dis[graph[j][1]] = dis[graph[j][0]] + graph[j][2]
    for i in range(muchii):
        x = graph[i][0]
        y = graph[i][1]
        cost = graph[i][2]
        if dis[x] != 999999 and dis[x] + cost < dis[y]:
            print("qu fost detectate cicluri negative")

    print("distanta fata de nodul de start")
    for i in range(noduri-1):
        print(i,"->", dis[i])

BellmanFord(graph, nr_noduri, nr_muchii, 2)
