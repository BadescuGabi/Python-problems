from _collections import deque
from itertools import combinations
import re


corect=0

l=[]
with open("graf.txt") as fisier:
   for i in range(1000):

       n=re.split(r'[\n\s]|:|-',fisier.readline())
       l.append(n)

for i in l:
    min=int(i[0])
    max=int(i[1])
    litera=i[2]
    aparitii=0
    for j in i[4]:
        if j==litera:
            aparitii+=1
    if aparitii>=min and aparitii<=max:
        corect+=1

print(corect)
