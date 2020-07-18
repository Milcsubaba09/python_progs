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
# Pf a élet fizetés jele
ef = 100
# Efe a élet vásárlás értéke
efe = 50
# XP a szint jele
xp = 24
# Vas a vas jele
vas = 0
#ec az energia cella jele
ec = 0
#kt a kötszer jele
kt = 0

xp5 = 0
xp10 = 0
xp15 = 0
xp20 = 0
xp25 = 0


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
	a = randrange(1, 10)
	return 1 if a == 1 or a == 3 or a == 5 or a == 7 or a == 9 else 2


print("")
print("")
cprint("Üdv a Zombie Rush játékban!".center(80), 'blue')
print("")

while True:
	menu = ["1 = Kezdés",
			"2 = A játékról",
			"3 = Beállítások",
			]

	for m in menu:
		cprint(f"{m}", 'cyan')

	print("")
	k = range_check("Válassz menüpontot[1-3]: ", 1, 3)

	if k == 1:

		while True:
			if pe == 0 or pe < 0:
				pe = 0
			if pe == 1500 or pe > 1500:
				pe = 1500
				cprint("Megtelt a pénz mennyiség",'yellow')
			print("")
			cprint(f"Arany: {pe}", 'yellow')
			cprint(f"Élet: {e}", 'red')
			cprint(f"Pajzs: {p}", 'blue')
			print("")

			fomenu = ["1 = Fejlesztés",
					  "2 = Gyártás",
					  "3 = Csata",
					  ]

			for fm in fomenu:
				print(fm)

			fe = range_check("Válassz menüpontot[1-3]: ", 1, 3)

			if fe == 1:
				cprint("", 'green', attrs=['dark', 'bold'])
				cprint(f"Arany: {pe}".center(100), 'yellow')

				print("1 = ", ef, " Arany", efe, "Élet")
				print("2 = 200 Arany 50 pajzs")
				print("3 = Kilépés a vásárlásból")
				print("")

				f = range_check("Mit szeretnél fejleszteni?[1-3]: ", 1, 3)
				if f == 1:
					if e < 5000:
						if pe == ef or pe > ef:
							e = e + efe
							pe = pe - ef
							print("")
							print("")
						else:
							print("")
							cprint("Ehhez nincs elég pénzed!", 'red')
							print("")
							if pe == 0 or pe < 0:
								pe = 0

					if e == 1500 or e > 1500:
						cprint("Megtelt az élet mennyiség", 'red')
						e = 1500

				if f == 2:
					if p < 50:
						if pe == 200 or pe >= 200:
							p = p + 50
							pe = pe - 200
							print("")
							print(pe, "Aranyad,", e, "Életed, és", p, "Pajzsod van.")
							print("")
						else:
							print("")
							cprint("Ehhez nincs elég pénzed!", 'red')
							print("")
							if pe == 0 or pe < 0:
								pe = 0
					if p == 50 or p > 50:
						cprint("Megtelt a pajzs mennyiség!", 'blue')
						p = 50


			if fe == 2:
				print("")
				print(vas,"vasad,",ec,"energia cellád",kt,"kötszered van!")
				gyartas = ["1 = Élet (3 Energia cella,5 kötszer/50 élet)",
						   "2 = Pajzs (4 Energia cella,6 vas/50 pajzs)",
						   "3 = Kilépés a gyártásból",
						   ]
				for gy in gyartas:
					cprint(f"{gy}",'cyan')

				b = range_check("Mit szeretnél gyártani[1-3]: ", 1, 3)

				if b == 1:
					if ec >= 3 and kt >= 5:
						if e < 1500:
							ec = ec -3
							kt = kt -5
							e = e + 50
							if ec <= 0:
								ec = 0
							if kt <= 0:
								kt = 0
						if e > 1500 or e == 1500:
							cprint("Megtelt az élet mennyiség", 'red')
							e = 1500
					else:
						cprint("Ehhez nincs elég alapanyagod!",'red')


				if b == 2:
					if ec >= 4 and vas >= 6:
						if p < 50:
							ec = ec -4
							vas = vas - 6
							p = p + 50
							if ec <= 0:
								ec = 0
							if vas <= 0:
								vas = 0
						if p > 50 or p == 50:
							cprint("Megtelt a pajzs mennyiség!", 'blue')
							p = 50
					else:
						cprint("Ehhez nincs elég alapanyagod!", 'red')


			if fe == 3:
				print("")
				a = randcsata()
				cprint("Rendben! Akkor indul a csata!", 'red', attrs=['dark', 'bold'])
				print("")
				if efe < 250:
					ef = ef + 15
					efe = efe + 5

				if a == 1:
					psz = psz + 15
					pe = pe + psz
					xp = xp + 1
					vas = vas + 1
					ec = ec + 1
					kt = kt + 1

					seconds = 5

					for i in range(seconds):
						cprint("\r %d. másodperc kell a csata végéhez" % (seconds - i), 'blue', end="")
						time.sleep(0.75)
					print("")
					cprint("\nSikeresen megnyerted a csatát!", 'green')
					print("")
					cprint("Csatában megszerzett dolgok: Arany, +Pénz gyűjtés, +XP, +Vas, +Energia cella, +Kötszer", 'cyan')
					cprint(f"XP szinted: {xp}".center(80), 'green')
					print("")

				if xp5 == 0:
					if xp == 5:
						cprint("Elérted a 5. XP szintet.", 'cyan')
						p = p + 25
						print("")
						cprint("Jutalom: 25 Pajzs".center(100), 'yellow')
						xp5 = 1
				if xp10 == 0:
					if xp == 10:
						cprint(f"Elérted a {xp}. XP szintet.", 'cyan')
						print("")
						cprint("Jutalom: 750 Arany".center(100), 'yellow')
						pe = pe + 750
						xp10 = 1
				if xp15 == 0:
					if xp == 15:
						cprint(f"Elérted a {xp}. XP szintet.", 'cyan')
						e = e + 25
						print("")
						cprint("Jutalom: 25 élet".center(100), 'yellow')
						xp15 = 1
				if xp20 == 0:
					if xp == 20:
						cprint("Elérted a 20. XP szintet.", 'cyan')
						pe = pe + 750
						print("")
						cprint("Jutalom: 750 Arany".center(100), 'yellow')
						xp20 = 1
				if xp25 == 0:
					if xp == 25:
						cprint("Elérted a 25. XP szintet.", 'cyan')
						p = p + 50
						print("")
						cprint("Megnyerted a zombik ellen a háborút! Gratulálok!".center(80),'green')
						xp25 = 1
						sys.exit(0)

				if a == 2:
					pe = pe + 20
					if p > 0:
						p = p - zt
					if p == 1 or p < 1:
						p = 0
					if p == 0:
						e = e - zt
					if zt < 500:
						zt = zt + 5
					if zt == 500 or zt > 500:
						zt = 500
					seconds = 5

					for i in range(seconds):
						cprint("\r %d. másodperc kell a csata végéhez" % (seconds - i), 'blue', end="")
						time.sleep(0.75)
					print("")
					cprint("\nVesztettél", 'red')
					print("")

				if e < 0 or e == 0:
					cprint("Elveszteddet a játékot", 'red')
					cprint(f"{xp} XP szintet érted el.", 'cyan')
					print("")
					e = 0
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
					ef = 100
					# Efe a élet vásárlás érték
					efe = 50
					# XP a szint jele
					xp = 0
					# Vas a vas jele
					vas = 0
					# ec az energia cella jele
					ec = 0
					# kt a kötszer jele
					kt = 0

					xp5 = 0
					xp10 = 0
					xp15 = 0
					xp20 = 0
					xp25 = 0
					break



	if k == 2:
		print("")
		cprint("A Játék lényege hogy legyőzd a zombikat és megnyerd a csatákat.", 'red')
		cprint("Ha vesztettél akkor lemegy az életed és a zombik nagyobbat fognak sebezni.", 'red')
		cprint("Ha viszont megnyersz egy csatát akkor kapsz XP-t,pénzt és pénz gyűjtést.", 'red')
		cprint("A pénz gyűjtés azt jelenti hogy minden győzelem után több pénzt fogsz kapni.", 'red')
		print("")

	if k == 3:
		nehezsegiszint = ["1 = Könnyű",
						  "2 = Normál",
						  "3 = Nehéz",
						  ]
		for n in nehezsegiszint:
			cprint(f"{n}", 'red')

		print("")
		neh = range_check("Válassz nehézségi szintet[1-3]: ", 1, 3)

		if neh == 1:
			# E az élet jele
			e = 100
			# P a pajzs jele
			p = 25
			# Pe a pénz jele
			pe = 125
			# Zt a zombi támadás jele
			zt = 15
			# Psz a pénz szerzés jele
			psz = 60
			# Pf a élet fizetés jele
			ef = 50
			# Efe a élet fizetés érték
			efe = 50
			# XP a szint jele
			xp = 0
			# Vas a vas jele
			vas = 0
			# ec az energia cella jele
			ec = 0
			# kt a kötszer jele
			kt = 0

			xp5 = 0
			xp10 = 0
			xp15 = 0
			xp20 = 0
			xp25 = 0

		if neh == 2:
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
			ef = 100
			# Efe a élet vásárlás érték
			efe = 50
			# XP a szint jele
			xp = 0
			# Vas a vas jele
			vas = 0
			# ec az energia cella jele
			ec = 0
			# kt a kötszer jele
			kt = 0

			xp5 = 0
			xp10 = 0
			xp15 = 0
			xp20 = 0
			xp25 = 0

		if neh == 3:
			# E az élet jele
			e = 100
			# P a pajzs jele
			p = 0
			# Pe a pénz jele
			pe = 50
			# Zt a zombi támadás jele
			zt = 35
			# Psz a pénz szerzés jele
			psz = 40
			# Pf a élet fizetés jele
			ef = 150
			# Efe a élet fizetés érték
			efe = 50
			# XP a szint jele
			xp = 0
			vas = 0
			# ec az energia cella jele
			ec = 0
			# kt a kötszer jele
			kt = 0

			xp5 = 0
			xp10 = 0
			xp15 = 0
			xp20 = 0
			xp25 = 0