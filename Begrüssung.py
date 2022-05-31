# Begrüßung

namen = ["Peter", "Dora", "Kevin", "Fritz", "Sarah"]

def begruessung1(name):
    print("Hallo", name, "!")
    
print("Begrüssung 1:")
for name in namen:
    begruessung1(name)
    
    
def begruessung2(namen):
    for name in namen:
        print("Hallo", name, "!")

print("")
print("Begrüssung 2:")
begruessung2(namen)