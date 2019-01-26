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








