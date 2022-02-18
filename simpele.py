import itertools
import random

#mogelijkheden opschrijven #bron: docent in de klas
def permutaties():
    perms = itertools.product(["A","B","C","D","E","F"], repeat=4)
    return [p for p in perms]
mogelijkheden = permutaties()

#controleer of de code geldig is Bron: docent
def valide(code):
    kleuren = ["A","B","C","D","E","F"]
    if len(code) != 4:
        return False
    for c in code:
        if c not in kleuren:
            return False
    return True

#kijk hoeveel items overeen komen in 2 antwoorden
def vergelijk_item(gok,antwoord): 
    #variabelen instellen
    teller = 0
    aantalgoed = 0
    kopiecode = list(antwoord)
    
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
    return aantalgoed


#verwijderen onmogelijke antwoorden uit de lijst
def lijst_aanpassen(gok,feedback):
    #loop over alle elementen uit de lijst van mogelijkheden
    count = 0
    while count < len(mogelijkheden):
        #als de feedback van de gok en het antwoord niet hetzelfde is als de gok en het item
        if feedback != vergelijk_item(gok,mogelijkheden[count]):
            #verwijder dat item
            mogelijkheden.pop(count)
            #begin weer onderaan de lijst
            count = 0
        #als wel overeenkomt ga verder met het volgende item
        else: count += 1

#het spel
def main_game():
    #herstel de lijst van mogelijkheden
    mogelijkheden = permutaties()
    #vraag om input voor een code
    code = list(input("GEEF EEN VIER LETTERIGE CODE: "))
    #zolang de code niet geldig is blijf om een nieuwe code vragen
    geldig = valide(code)
    while not geldig:
        code = code = list(input("GEEF EEN VIER LETTERIGE CODE: "))
        geldig = valide(code)
    #een teller voor het aantal stappen maken
    stappen = 0
    #een oneindige loop (tot gevonden is)
    while True:
        #een stap er bij
        stappen += 1
        #als er nog items over zijn, pak de eerste uit de lijst. anders 
        if len(mogelijkheden):
            gok = mogelijkheden[0]
        else:
            #als er een fout is opgetreden print dat
            print("De code is ongeldig")
            return
        #als de gok goed is print in hoeveel stappen het is gelukt
        if list(gok) == code:
            print(f"gevonden in {stappen} stappen !")
            break
        #verwijder het eerste element (de gok)
        mogelijkheden.pop(0)
        #geef feedback terug over de gok
        feedback = vergelijk_item(gok,code)
        #pas de mogleijkheids lijst aan door alles wat niet meer kan weg te strepen
        lijst_aanpassen(gok,feedback)
    
#oneindig spel loop
while True:
    main_game()


        
