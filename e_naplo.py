print ("*="*40)
print ("Pető Milán negyedikes jegyek.")
print ("*="*40)
#------------------------------------------------------------------------
subjects =[
    "Magatartás",
    "Szorgalom",
    "Olvasás",
    "Irodalom",
    "Angol",
    "Matek",
    "Környezet",
    "Ének-Zene",
    "Vizuális Kúltúra",
    "Testnevelés",
    "Technika",
]

print("A tantárgyak listája:")
for i in subjects:
    print (i)
#------------------------------------------------------------------------
magat = (4,4,5,5,5)

szorg = (5,5,5,5,5)

olvas = (5,5,5,5,5,4,5,5,5,5,5)

iroda = (3,5,5,5,3,5,5,5,5,5,5,5,5)

angol = (5,5,5,5,5,5,5,5,4)

matek = (5,5,5,5,5,5,5,5,5,4,5,5,5)

korny = (5,5,5,5,5,5,5,5)

enekz = (5,5,5,5,5,5)

vizua = (5,5,4,5,4,5)

testn = (5,5,5,5,5,5,5,5)

techn = (5,5,5,5,5,5)
#------------------------------------------------------------------------
print ("*="*40)
print ("A Magatartás jegyek:", magat)               #Magatartás
szj = len(magat)
sza = sum(magat)/szj
print ("Magatartás átlag:", "%.2f" % sza)
print ("")
#------------------------------------------------------------------------
print ("A Szorgalom jegyek:", szorg)
szoj = len(szorg)                                   #Szorgalom
szoa = sum(szorg)/szoj
print ("Szorgalom átlag", "%.2f"% szoa)
print ("")
#------------------------------------------------------------------------
print ("Az Olvasás jegyek:", olvas)
oj = len(olvas)                                     #Olvasás
oa = sum(olvas)/oj
print ("Olvasás átlag:", "%.2f"% oa)
print ("")
#------------------------------------------------------------------------
print ("Az Irodalom jegyek:", iroda)
ij = len(iroda)                                     #Irodalom
ia = sum(iroda)/ij
print ("Irodalom átlag:", "%.2f"% ia)
print ("")
#------------------------------------------------------------------------
print ("Az Angol jegyek:", angol)
aj = len(angol)                                     #Angol
aa = sum(angol)/aj
print ("Angol átlag:", "%.2f"% aa)
print ("")
#------------------------------------------------------------------------
print ("A Matek jegyek:", matek)
mj = len(matek)                     # A Matek jegyek száma
ma = sum(matek)/mj                  # A Matek jegy átlag = sum(matek) osztva a jegyek számával
print ("Matek átlag:", "%.2f"% ma)  # Itt meg kiíratom megformázva az eredményt
print ("")
#------------------------------------------------------------------------
print ("Az Környezet jegyek:", korny)
kj = len(korny)                                     #Angol
ka = sum(korny)/kj
print ("Környezet átlag:", "%.2f"% ka)
print ("")
#------------------------------------------------------------------------
print ("Az Ének-Zene jegyek:", enekz)
zj = len(enekz)                                     #Ének-Zene
za = sum(enekz)/zj
print ("Ének-Zene átlag:", "%.2f"% za)
print ("")

print ("A Vizuális Kúltúra jegyek:", vizua)
vj = len(vizua)
va = sum(vizua)/vj
print ("Vizuális Kúltúra átlag:", "%.2f"% va)
print ("")
#------------------------------------------------------------------------
print ("A Testnevelés jegyek:", testn)
tj = len(testn)                                     #Testnevelés
ta = sum(testn)/tj
print ("Testnevelés átlag:", "%.2f"% ta)
print ("")
#------------------------------------------------------------------------
print ("A Technika jegyek:", techn)
tcj = len(techn)                                    #Technika
tca = sum(techn)/tcj
print ("Techinka átlag:", "%.2f"% tca)
print ("")
#------------------------------------------------------------------------

orarend = [
    "Hétfő:     Olvasás, Nyelvtan, Környezet, Angol, Matematika, Testnevelés, Informatika",
    "Kedd:      Testnevelés, Matemetika, Technika, Olvasás, Rajz, Rajz",
    "Szerda:    Angol, Testnevelés, Matemetika, Fogalmazás, Etika",
    "Csütortök: Nyelvtan, Angol, Ének-Zene, Matematika, Testnevelés",
    "Péntek:    Testnevelés, Matemetika, Nyelvtan, Olvasás, Környezet, Ének-Zene",
]
print("Heti Órarend:")
for o in orarend:
    print (o)
print("")
print("Viszlát!")








