# Getränkezuordnung

liste = {"peter":"Bier", "dora":"Wein", "kevin":"Spritzer", "Fritz":"Most"}

name = input("Geben Sie einen Namen ein, um sein/ihr Lieblingsgetränk zu erfahren:")
name = name.lower()

if name not in liste:
    print("Dieser Name ist in der Liste nicht vorhanden!")
    
else:
    print("Lieblingsgetränk von", name, ":", liste[name])