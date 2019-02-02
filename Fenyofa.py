#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import time
import sys



print ("*="*40)

x = False
while x != True:
    a = input("Írd be hogy mekkora fenyőfát szeretnél: ")
    x = a.isdigit()
    aa = int(a)

start = time.time()

# Loop
for i in range(1,aa+1):
    print((aa-i)*" ","A "*i, (aa-i)*" ")

end = time.time()
e = end - start

#
print("\nA program %.2f" % e, "másodpecig futott.")




sys.exit(0)

