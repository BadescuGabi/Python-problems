from heapq import *


def citire(nume_fisier="graf.txt"):
    with open(nume_fisier) as f:
        la = []
        linie = f.readline().split()
        i = 1
        while linie:
            for x in linie:
                la.append([x, i])
                i += 1
            linie = f.readline().split()

    return la


import numpy as np


def levenshtein(seq1, seq2):
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
    matrix = np.zeros((size_x, size_y))
    for x in range(size_x):
        matrix[x, 0] = x
    for y in range(size_y):
        matrix[0, y] = y

    for x in range(1, size_x):
        for y in range(1, size_y):
            if seq1[x - 1] == seq2[y - 1]:
                matrix[x, y] = min(
                    matrix[x - 1, y] + 1,
                    matrix[x - 1, y - 1],
                    matrix[x, y - 1] + 1
                )
            else:
                matrix[x, y] = min(
                    matrix[x - 1, y] + 1,
                    matrix[x - 1, y - 1] + 1,
                    matrix[x, y - 1] + 1
                )

    return (matrix[size_x - 1, size_y - 1])


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


a = citire()
#print(a)
arbore = []
cost = 0
nr_muchii = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        arbore.append((levenshtein(a[i][0], a[j][0]), a[i], a[j]))

tata = [0] * (len(a) + 1)
h = [0] * (len(a) + 1)
heapify(arbore)
cluster = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nr = 10
arbore1 = []
# print(arbore)
while arbore:
    aa=arbore[0][1][1]
    bb=arbore[0][2][1]
    if Reprez(arbore[0][1][1]) != Reprez(arbore[0][2][1]):
        Reuneste(arbore[0][1][1], arbore[0][2][1])
        arbore1.append(arbore[0])
        for i in range(len(cluster)):
            if cluster[i] == cluster[arbore[0][2][1]] and cluster[i] == i:
                nr -= 1
            if cluster[i] == cluster[arbore[0][2][1]]:
                cluster[i] = cluster[arbore[0][1][1]]

        nr_muchii += 1
        if nr_muchii == len(a) -3:

            break
    heappop(arbore)
#print(arbore1)
#print(cluster)

for i in range(len(a)):
    a[i][1]=cluster[i+1]
a.sort(key=lambda x:x[1])
j=a[0][1]
for i in a:
    if i[1]!=j:
        print()
    print(i[0],end=' ')
    j=i[1]
print()
print(arbore[0][0])
#print(a)
'''martian care este sinonim ana
case apa arbore partial minim'''
