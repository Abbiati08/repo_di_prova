import calcolatrice as clc

while True:
    print("Benvenuto nella nostra calcolatrice")
    print("Inserisci l'operazione che vuoi effettuare")
    scelta = int(input("1)sottrazione\n2)addizione\n"))
    if scelta == 0:
        break
    if scelta == 1:
        clc.Sottrazione()
    elif scelta == 2:
        clc.Somma()
    else:
        print("Scelta non corretta!")
