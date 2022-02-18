import random
import itertools
kleuren = ['A', 'B', 'C', 'D', 'E', 'F']

#random code maken
def code_generen():
    return tuple(random.choices(kleuren,k=4))


#code controlleren

#kijk hoeveel items overeen komen in 2 antwoorden
def controleer(gok,antwoord): 
    #variabelen instellen
    teller = 0
    aantalgoed = 0
    aantalbijnagoed = 0
    kopiecode = list(antwoord)
    
 #loop over alle 4 de elementen
    while teller < 4:
        #als het element in het antwoord zit
        if gok[teller] == kopiecode[teller]:
            #vervang het element met een streepje zodat deze niet nog een keer wordt gelezen
            kopiecode[teller] = "-"
            #tel een op bij de gevonden inclusieve elementen
            aantalgoed += 1
        #verder naar het volgende element
        teller += 1
    #reset teller
    teller = 0
    #loop over alle 4 de elementen
    while teller < 4:
        #als het element in het antwoord zit
        if gok[teller] in kopiecode:
            #vervang het element met een streepje zodat deze niet nog een keer wordt gelezen
            kopiecode[kopiecode.index(gok[teller])] = "-"
            #tel een op bij de gevonden inclusieve elementen
            aantalgoed += 1
        #verder naar het volgende element
        teller += 1
    return aantalgoed,aantalbijnagoed

#nieuw spel of doorgaan


#spel
def maingame():
    #gok counter bij houden
    gokken = 0
    #een willekeurige code generenen
    code = code_generen()
    print(code)
    #oneindige loop
    while True:
        #vraag op een gok te doen
        gok = input("Raad de code: ")
        #gokken teller aanvullen
        gokken += 1
        #geef feedback over de gok
        feedback = controleer(gok,code)
        #als de feedback aangeeft dat alles op de juiste plek staat
        if feedback[0] == 4:
            #geef aan dat gewonnen
            print(f"Gefeliciteerd u heeft het geraden in {gokken} gok(ken)")
            return
        print(f"{feedback[0]} cijfers staan op de goede plek")
        print(f"{feedback[1]} cijfers staan op de verkeerde plek")


#speel oneindig lang
while True:
    maingame()
    if input("Wilt u stoppen? ") == "ja":
        break