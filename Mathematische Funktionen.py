# Mathematische Funktionen: Summe, Differnez, Produkt, Quotient

zahl1 = float(input("Bitte geben Sie die 1. Zahl ein:"))
zahl2 = float(input("Bitte geben Sie die 2. Zahl ein:"))

def summe(zahl1, zahl2):
    summe = zahl1 + zahl2
    return summe

def differenz(zahl1, zahl2):
    differenz = zahl1 - zahl2
    return differenz

def produkt(zahl1, zahl2):
    produkt = zahl1 * zahl2
    return produkt

def quotient(zahl1, zahl2):
    
    if zahl2 == 0:
        print("Division durch 0 nicht möglich!")
        return
    
    quotient = zahl1 / zahl2
    return quotient

outputsumme = summe(zahl1, zahl2)
outputdifferenz = differenz(zahl1, zahl2)
outputprodukt = produkt(zahl1, zahl2)
outputquotient = quotient(zahl1, zahl2)

print("Summe: ", outputsumme)
print("Differenz: ", outputdifferenz)
print("Produkt: ", outputprodukt)
print("Quotient: ", outputquotient)








    
    
    
    