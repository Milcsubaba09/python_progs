#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import time
from termcolor import colored, cprint
import sys
from random import randrange


# E az élet jele
e = 100
# P a pajzs jele
p = 0
# Pe a pénz jele
pe = 100
# Zt a zombi támadás jele
zt = 25
# Psz a pénz szerzés jele
psz = 50
# Ef az élet fizetés jele
ef = 50
# Efe az élet fizetés érték
efe = 50
# XP a szint jele
xp = 0
# Játék újrakezdés
ch = True


# Itt csinálom a range check function-t
def range_check(question, a, b):
    """
    Checks your choice between two numbers.
    Returns the selected number.
    Example:
        a = range_check('Please choose in the range: ',1,10)
    """
    y = 0
    while y != 1:
        try:
            i = int(input(question))
            if i in range(a, b + 1):
                y = 1
                pass
            else:
                cprint("A megadott számokig válassz!", 'red')
                y = 0
        except ValueError:
            cprint("Számot kérek!", 'red')
            y = 0
    return i


# A csata végeredménye
def randcsata():
    """
    Legenerálom hogy a játékos nyerjen vagy veszítsen.
    """
    a = randrange(1,10)
    return 1 if a == 1 or a == 3 or a == 5 or a == 7 or a == 9 else 2


# Itt írom ki a szöveget
print("")
print("")
cprint("Üdv a Zombie Rush játékban!".center(143),'blue')
print("="*143)
cprint("A játék lényege az hogy fejleszd a bázisodat és megvédd a zombik elől!                                                                        | ",'red')
cprint("De vigyázz mert ha az eggyik csatában lement az életed a következőt is ugyanazzal az életmennyiséggel kezded! Ugyanez a pajzsra is vonatkozik |",'red')
print("="*143)
print("")
jj = True


while jj == True:
    x = input("Szeretnél játszani? Igen [I] vagy nem [N]: ")

    if x == "I" or x == "i":
        # Itt kezdődik a játék
        while True:

            print("")
            cprint(f"Arany: {pe}", 'yellow')
            cprint(f"Élet: {e}", 'red')
            cprint(f"Pajzs: {p}", 'blue')
            print("")
            x = input("Szeretnél fejleszteni? Igen [I] vagy nem [N]: ")



            if x == "I" or x == "i":
                cprint("",'green', attrs=['dark', 'bold'])
                cprint(f"Arany: {pe}".center(100),'yellow')


                print("1 = ",ef," Arany",efe, "Élet")
                print("2 = 100 Arany 50 pajzs")
                print("3 = Kilépés a vásárlásból")
                print("")



                f = range_check("Mit szeretnél venni? 1-3-ig válassz: ",1, 3)
                if f == 1:
                    if e < 5000:
                        if pe == 50 or pe > 50:
                            e = e + efe
                            pe = pe - ef
                            print("")
                            print("")
                        else:
                            print("")
                            cprint("Ehhez nincs elég pénzed!",'red')
                            print("")

                    if e == 5000 or e > 5000:
                        cprint("Megtelt az élet mennyiség",'red')
                        e = 500

                if f == 2:
                    if p < 50:
                            if pe == 100 or pe >= 100:
                                p = p + 50
                                pe = pe -100
                                print("")
                                print(pe, "Aranyad,", e, "Életed, és", p, "Pajzsod van.")
                                print("")
                            else:
                                print("")
                                cprint("Ehhez nincs elég pénzed!", 'red')
                                print("")
                    if p == 50 or p > 50:
                        cprint("Megtelt a pajzs mennyiség!",'blue')
                        p = 50

                if pe == 0 or pe < 0:
                    pe = 0


            elif x == "N" or x == "n":
                print("")
                c = input("Biztosan akarsz csatázni? Igen [I] vagy nem [N]: ")
                print("")
                if c == "I" or c == "i":
                    a = randcsata()
                    cprint("Rendben! Akkor indul a csata!",'red', attrs=['dark', 'bold'])
                    print("")
                    if efe < 250:
                        ef = ef + 10
                        efe = efe + 5

                    if a == 1:
                        psz = psz + 15
                        pe = pe + psz
                        xp = xp + 1
                        seconds = 5

                        for i in range(seconds):
                            cprint(str(seconds - i) + " másodperc kell a csata végéhez",'blue')
                            time.sleep(0.5)
                        print("")
                        cprint("Sikeresen megnyerted a csatát!",'green')
                        print("")
                        cprint("Csatában megszerzett dolgok: Arany, +Pénz gyűjtés, +XP",'cyan')
                        cprint(f"XP szinted: {xp}".center(80),'green')
                        print("")

                    if xp == 5:
                        cprint("Elérted a 5. XP szintet.", 'cyan')
                        p = p + 25
                        print("")
                        cprint("Jutalom: 25 Pajzs".center(100), 'yellow')

                    if xp == 10:
                        cprint("Elérted a 10. XP szintet.",'cyan')
                        print("")
                        cprint("Jutalom: 750 Arany".center(100),'yellow')
                        pe = pe + 750

                    if xp == 15:
                        cprint("Elérted a 15. XP szintet.",'cyan')
                        e = e + 25
                        print("")
                        cprint("Jutalom: 25 élet".center(100), 'yellow')

                    if xp == 20:
                        cprint("Elérted a 20. XP szintet.", 'cyan')
                        pe = pe + 750
                        print("")
                        cprint("Jutalom: 750 Arany".center(100), 'yellow')

                    if xp == 25:
                        cprint("Elérted a 25. XP szintet.", 'cyan')
                        p = p + 25
                        print("")
                        cprint("Jutalom: 25 Pajzs".center(100), 'yellow')

                    if a == 2:
                        pe = pe + 20
                        if p > 0:
                            p = p - zt
                        if p == 1 or p < 1:
                            p = 0
                        if p == 0:
                            e = e - zt
                        if zt < 2250:
                            zt = zt + 5
                        if zt == 2250 or zt > 2250:
                            zt = 2250
                        seconds = 5

                        for i in range(seconds):
                            cprint(str(seconds - i) + " másodperc kell a csata végéhez",'blue')
                            time.sleep(0.5)
                        print("")
                        cprint("Vesztettél",'red')
                        print("")
                    if e < 0 or e == 0:
                        e = 0
                        print("=" *24)
                        cprint("Elvesztetted a játékot |",'red')
                        print("="*24)
                        ch = True

                        while ch == True:
                            print("")
                            j = input("Szeretnél játszani még egyet? Igen [I] vagy nem [N]: ")

                            if j == "I" or j == "i":
                                cprint("Rendben", 'blue')
                                # E az élet jele
                                e = 100
                                # P a pajzs jele
                                p = 0
                                # Pe a pénz jele
                                pe = 100
                                # Zt a zombi támadás jele
                                zt = 25
                                # Psz a pénz szerzés jele
                                psz = 50
                                # Pf a élet fizetés jele
                                ef = 50
                                # Efe a élet fizetés érték
                                efe = 50
                                # XP a szint jele
                                xp = 0
                                ch = False
                            elif j == "N" or j == "n":
                                print("")
                                sys.exit("Viszlát!")
                            else:
                                cprint("Ezt nem választhatod!", 'red', attrs=['dark', 'bold'])


            else:
                cprint("Ezt nem választhatod!",'red', attrs=['dark', 'bold'])

    elif x == "N" or x == "n":
        sys.exit("Viszlát!")
    else:
        print("")
        cprint("Ezt nem választhatod!",'red')
        print("")