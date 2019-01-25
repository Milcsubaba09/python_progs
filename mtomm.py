print ("="*80)

x = False
y = False

#------------------------------------------------------------------------
while x != True:
    a = input("Írj be egy számot majd nyomj egy (m) [ENTER-t]: ")
    x = a.isdigit()

aa = int(a)*1000
#------------------------------------------------------------------------
while y != True:
    b = input("Írj be egy számot majd nyomj egy (dm) [ENTER-t]: ")
    y = b.isdigit()
bb = int(b)*100
#------------------------------------------------------------------------


print ("="*80)
print (aa, "mm +", bb, "mm")
print (aa+bb, "mm")
print ("="*80)
print ("Készítette: Pető Milán".center(80))
print ("="*80)
#------------------------------------------------------------------------








