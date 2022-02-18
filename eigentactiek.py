import itertools
import random
 

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

#kijk of de code geldig is (bron: docent in de les)
def valide(code):
    #alle kleur mogelijkheden
    kleuren = ["A","B","C","D","E","F"]
    #als de lengte van de code niet 4 is
    if len(code) != 4:
        #ongeldige code
        return False
    #loop over de elementen van de code
    for c in code:
        #als het element niet bij de kleuren behoort
        if c not in kleuren:
            #code is ongeldig
            return False
    return True


#mogelijkheden opschrijven (bron: docent)
def permutaties():
    perms = itertools.product(["A","B","C","D","E","F"], repeat=4)
    return [p for p in perms]
mogelijkheden = permutaties()

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

#fucntie voor het verwijderen van een element
def verwijderen(letter,aantal):
    #loop over alle elementen van de lijst
    count = 0
    while count < len(mogelijkheden):
        #als het aantal kleuren ergens meer bevat dan ongeldig
        if mogelijkheden[count].count(letter) > aantal:
            mogelijkheden.pop(count)
            count=0
        else: count +=1



#eerst achter de getallen komen
a = ('A','A','A','A')
b = ('B','B','B','B')
c = ('C','C','C','C')
d = ('D','D','D','D')
e = ('E','E','E','E')
f = ('F','F','F','F')
inclusieflijst = [a,b,c,d,e,f]


#de maingame
def maingame():
    #reset de mogelijkheden
    mogelijkheden = permutaties()
    #vraag om input code totdat de code geldig is
    code = list(input("GEEF EEN VIER LETTERIGE CODE: "))
    geldig = valide(code)
    while not geldig:
        code = list(input("GEEF EEN VIER LETTERIGE CODE: "))
        geldig = valide(code)
    
    #ga eerste alle verschillende kleuren langs
    res_getallen = 0
    inc_teller = 0
    while res_getallen < 4: #totdat er 4 kleueren zijn gevonden die erin voor komen
        gok = inclusieflijst[inc_teller]
        feedback = vergelijk_item(gok,code)
        res_getallen += feedback
        verwijderen(gok[0],feedback)
        inc_teller += 1
    gokcount = inc_teller
    #loop van begin tot eind tot de code is gevonden
    gevonden =  False
    while not gevonden:
        gokcount += 1
        gok = random.choice(mogelijkheden)
        if list(gok) == code:
            print(f"gevonden! het duurde {gokcount} stappen.")
            return
        #verwijder het eerste element (de gok)
        mogelijkheden.pop(0)

        
    
#oneindig spel spelen
while True:
    maingame()