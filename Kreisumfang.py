# Kreisumfang

import math

def eingabe():
    
    correct = False
    
    while correct == False:
        radius = input("Bitte geben Sie eine positive Zahl für den Radius ein:")

        try:
            
            r = float(radius)
        
            if r > 0:
                correct = True
                return r
            
            else:
                print("Keine gültige Eingabe! Bitte geben Sie eine positive Zahl ein.")
            
        except :
            print("Keine gültige Eingabe! Bitte geben Sie eine Zahl ein.")
    

rad = eingabe()        
def kreisumfang(rad):
    umfang = 2*rad*math.pi
    return umfang

kreisradius = eingabe()
print("Radius:", kreisradius)

ergebniss = kreisumfang(rad)
print("Kreisumfang:", ergebniss)
    
    
    
    
    
    
    
            
            
            
            
            
            