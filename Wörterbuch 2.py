# Wörterbuch 2

woerterbuch= {"apfel":"apple", "birne":"pear", "kirsche":"cherry", "melone":"melon", "marille":"apricot", "pfirsich":"peach"}

print("Willkommen beim Deutsch-Englisch Wörterbuch.")
print("Um ein Wort ins englische zu übersetzen wähle 'T'.")
print("Um eine neue Übersetzung hinzuzufügen wähle 'N'.")

correct = False

while correct == False:

    eingabe = input("Wählen Sie eine Funktion aus:")
    
    if eingabe == "T":
        
        correct = True
        wort = input("Geben Sie ein Wort zum Übersetzen ein:")
        wort = wort.lower()
        
        if wort not in woerterbuch:
            print("Dieses Wort ist nicht im Wörterbuch vorhanden!")
    
        else:
            print("Englische Übersetzung:", woerterbuch[wort])
            
    elif eingabe =="N":
        
        correct = True
        woerterbuch[input("Deutsches Wort:")] = input("Englisches Wort:")
        
        
        else:
            print("Es konnte keine Funktion ausgewählt werden.")
            
            
            
        
        
            
            
        
        
        
            
        
            
                
                
            
            
            
            
            
            
            
            