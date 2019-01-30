import sys
print ("*="*40)

while True:
    try:
        a = input("Írd be a neved: ")
        f = float(a)
    except ValueError:
        break
print ("*="*40)
h = False

while h != True:
    b = input("Írd be a korod: ")
    h = b.isdigit()
print ("*="*40)
while True:
    try:
        c = input("Írd be hogy melyik iskolába jársz: ")
        g = float(c)
    except ValueError:
        break
print ("*="*40)
print ("Szia",a,",",
        "Te", b, "éves vagy",",",
        "És a(z)",c,"iskolába jársz."
)
print ("")
x = False

while x != True:
    j = input("Melyik a kedvenc számod: ")
    x = j.isdigit()
print ("")
while True:
    try:
        y = input("Írd be hogy fiú vagy lány esetleg robot vagy:")
        z = float(y)
    except ValueError:
        break
print ("")
print (
    "A kedvenc számod a(z)",j,","
    "És", y ,"vagy."
)
print ("")
v = False
while v != True:
    w = input("Írd be számmal hogy mikor születtél:")
    if len(w) == 0:
        print("Nem írtál semmit!")
        v = False
    else:
        pass
        try:
            int(w)
            v = False
        except:
            try:
                float(w)
                v = True
            except:
                    pass

print ("")
print ("Te",w,"születtél.")

print ("Készítette:Pető Milán".center(80))

sys.exit(0)