print ("="*80)

x = False
y = False
z = False
#------------------------------------------------------------------------
while x != True:
    a = input("Írj be egy számot majd nyomj egy (kg) [ENTER-t]: ")
    x = a.isdigit()

aa = int(a)*1000
#------------------------------------------------------------------------
while y != True:
    b = input("Írj be egy számot majd nyomj egy (dkg)[ENTER-t]: ")
    y = b.isdigit()

bb = int(b)*10
#------------------------------------------------------------------------
while z != True:
    c = input("Írj be egy számot majd nyomj egy (g)[ENTER-t]: ")
    z = c.isdigit()

cc = int(c)
#------------------------------------------------------------------------

print ("="*80)
print (aa,"g +",bb,"g",cc,"g")
print (aa+bb+cc,"gramm")
print ("="*80)
print("Készítette: Pető Milán 2019.1.21.".center(80))
print ("="*80)

