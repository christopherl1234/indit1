zaehlvariable = 0
ergebnis = 0

strTerme = input("Bitte geben Sie die Anzahl der Terme an: ")
intTerme = int(strTerme)

while zaehlvariable <= intTerme:

    pi = (((-1)**zaehlvariable) / (2*zaehlvariable +1))
    ergebnis += pi
    zaehlvariable += 1
    
print("Die Annäherung an Pi beträgt: ", ergebnis * 4)