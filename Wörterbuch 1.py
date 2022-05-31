# Wörterbuch 1

woerterbuch= {"apfel":"apple", "birne":"pear", "kirsche":"cherry", "melone":"melon", "marille":"apricot", "pfirsich":"peach"}

eingabe = input("Bitte geben Sie ein Wort zum übersetzen ein:")
eingabe = eingabe.lower()

if eingabe not in woerterbuch:
    print("Dieses Wort ist nicht im Wörterbuch vorhanden!")
    
else:
    print("Englische Übersetzung:", woerterbuch[eingabe])