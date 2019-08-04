#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys


e = 3

print (e,"életed van")

x = False
y = False
z = False
zs = False


a = ""
b = ""
c = ""
d = ""

while x != True:
    a = input("124-12: ")
    x = a.isdigit()

    if a == "112":
        print("Ügyes vagy :)")
        print(e,"Életed Van")
    else:
        print("Nem sikerült, próbáld újra.")

        e = e - 1
        print(e," Életed maradt!")
        if e == 0:
            sys.exit()
        x = False

while y != True:
    b = input("573-37: ")
    y = b.isdigit()

    if b == "536":
        print("Ügyes vagy :)")
        print(e,"Életed Van")
    else:
        print("Nem sikerült, próbáld újra.")

        e = e - 1
        print(e," Életed maradt!")
        if e == 0:
            sys.exit()
        y = False

while z != True:
    c = input("893-127: ")
    z = c.isdigit()

    if c == "766":
        print("Ügyes vagy :)")
        print(e,"Élettel Játszottad Végig")
    else:
        print("Nem sikerült, próbáld újra.")

        e = e - 1
        print(e," Életed maradt!")
        if e == 0:
            sys.exit()
        z = False


i = input("Szeretnél Bónusz Kérdest?[I] Vagy [N]: ")

if i == "I" or i == "i":
    print("Rendben")
    while zs != True:
        d = input("1204+56-458: ")
        zs = d.isdigit()

        if d == "802":
            print("Ügyes vagy :)")
            print("Nagyon Ügyes vagy:)")
        else:
            print("Nem sikerült, próbáld újra.")

            e = e - 1
            print(e, " Életed maradt!")
            if e == 0:
                sys.exit()
            zs = False

if i == "N" or i == "n":
    print("legalább Megpróbálhattad Volna :(")
    sys.exit(0)

sys.exit (0)

