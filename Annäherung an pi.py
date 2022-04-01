zählvariable = 0
ergebnis = 0

strTerme = input("Bitte geben Sie die Anzahl der Terme an: ")
intTerme = int(strTerme)

while zählvariable <= intTerme:

    floatPi = (((-1)**zählvariable) / (2*zählvariable +1))
    ergebnis += floatPi
    zählvariable += 1
    
print("Die Annäherung an Pi beträgt: ", ergebnis * 4)