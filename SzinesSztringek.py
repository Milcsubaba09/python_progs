#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from termcolor import colored, cprint
import sys

cprint ("A nevem Pető Milán.",color='blue')

x = False
while x != True:
    a = input("Írd be hogy mekkora fenyőfát szeretnél: ")
    x = a.isdigit()
    aa = int(a)


for i in range(1,aa+1):
    print((aa-i)*" ","O "*i, (aa-i)*" ")


x = input("Tetszik? Igen [I] vagy nem [N]?")

if x == "I" or x == "i":
    cprint("Köszönöm.", color='green', attrs=['dark', 'bold'])
elif x == "N" or x == "n":
    cprint("Ne hazudjál!!!", color='red', attrs=['dark', 'bold'])
else:
    cprint("Ennyire nem rossz hogy nem válaszolsz!!!",color='red')

k = ("Pető Milán")
cprint(f"A készítő neve:{k}",color='blue')



sys.exit(0)



