zilele_saptamanii={
    1:"Luni",
    2:"Marti",
    3:"Miercuri",
    4:"Joi",
    5:"Vineri",
    6:"Sambata",
    0:"Duminica"
}
lunile_anului={
    1:"Ianuarie",
    2:"Februarie",
    3:"Martie",
    4:"Aprilie",
    5:"Mai",
    6:"Iunie",
    7:"Iulie",
    8:"August",
    9:"Septembrie",
    10:"Octombrie",
    11:"Noiembrie",
    12:"Decembrie"
}
zile_luna={
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}
ziua=int(input())
luna=int(input())
anul=int(input())
print("prima data: ",end=" ")
print(ziua,end="-")
print(lunile_anului.get(luna),end="-")
print(anul,end="--")
print(zilele_saptamanii.get(ziua%7)) #magarie ,merge pentru ca vreau eu sa aleg 1 ianuarie 1923 si pica lunea
ziua2=int(input())
luna2=int(input())
anul2=int(input())
print("Data aleasa este: ",end="")
print(ziua2,end="-")
print(lunile_anului.get(luna2),end="-")
print(anul2)
#iau data de afisare 28 octombrie 1986 si pica marti
anibis=0
for i in range(anul,anul2+1):
    if i%400==0:
        anibis+=1
    elif i%4==0 and i%100!=0:
        anibis+=1
nrzile=0
for i in range(1,luna2):
     nrzile+=zile_luna[i]
nrzile+=ziua2
nrzile+=(anul2-anul)*365+anibis
if nrzile%7==1:
        print(zilele_saptamanii.get(1))
if nrzile%7==2:
        print(zilele_saptamanii.get(2))
if nrzile%7==3:
        print(zilele_saptamanii.get(3))
if nrzile%7==4:
        print(zilele_saptamanii.get(4))
if nrzile%7==5:
        print(zilele_saptamanii.get(5))
if nrzile%7==6:
        print(zilele_saptamanii.get(6))
if nrzile%7==0:
        print(zilele_saptamanii.get(0))
print(nrzile)
#problema an bisect, citesc o data din tastatura, cu an,luna,zi sapt iar apoi citesc alta.problema vrea sa aflu numarul de zile dintre ceo 2 ani si sa zic in ce zi pica a 2 a data aleasa

#are hiba,de revazut maine