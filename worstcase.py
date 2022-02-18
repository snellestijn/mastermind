
import itertools


#feeback functie gemaakt door de docent
def geef_feedback(code, guess):

    # Zet de gok om naar een lijst
    guess = list(guess)

    # De code om de gok mee te vergelijken
    kopie_code = list(code)

    # Juiste kleur op de juiste positie
    helemaal_goed = 0

    # Juiste kleur op de verkeerde positie
    juiste_kleur = 0

    # Loop over de code om de juiste kleur verkeerde positie te bepalen
    for i in range(4):   

        # Exacte match?
        if (kopie_code[i] == guess[i]):
            # Een match qua kleur en positie
            helemaal_goed += 1

            # Vervang het stukje code, zodat we deze niet 
            # als juiste kleur verkeerde positie kunnen markeren
            kopie_code[i] = '-'
            guess[i] = ''


    # Nu we alle juiste eruit gefilterd hebben kunnen we kijken 
    # naar wat nog op de verkeerde plek staat.
    for i in range(4):

        # Zit de kleur ergens anders in de code
        if guess[i] in kopie_code:

            # Verhoog de counter
            juiste_kleur += 1

            # Vervang het element, zodat we geen dubbele feedback krijgen
            kopie_code[kopie_code.index(guess[i])] = '-'
            guess[i] = ''

    return (helemaal_goed, juiste_kleur)


#verwijderen onmogelijke antwoorden uit de lijst
def lijst_aanpassen(gok,feedback):
    #loop over alle elementen uit de lijst van mogelijkheden
    count = 0
    while count < len(mogelijkheden):
        #als de feedback van de gok en het antwoord niet hetzelfde is als de gok en het item
        if feedback != geef_feedback(gok,mogelijkheden[count]):
            #verwijder dat item
            mogelijkheden.pop(count)
            #begin weer onderaan de lijst
            count = 0
        #als wel overeenkomt ga verder met het volgende item
        else: count += 1

#Stel alle mogelijkheden op, gemaakt door de docent
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


#dictionary maken van frequenties
def frequentielijst(mogelijkheden,gok):
    #lijst aanmaken
    lijst = dict()
    #loop over elk element
    for element in mogelijkheden:
        #feedback als variabelen opslaan
        fb = geef_feedback(element,gok)
        #als de feedback nog niet bestond in de lijst
        if fb not in lijst:
            #toevoegen aan de lijst
            lijst[fb] = 1
        #anders
        else: #een maal toevoegen aan de teller
            lijst[fb] += 1
    hoogste = int()
    #loop over de feedbacks heen
    for ele in lijst:
        #als een feedback vaker voorkomt dan de meest voorkomende
        if lijst [ele] > hoogste:
            #dan is dan de nieuwe hoogste feedback
            hoogste = lijst[ele]
    return hoogste

#functie voor de beste worst case te kiezen
def laagste_kiezen(mogelijkheden):
    #de maximale waarde instellen
    laagste = 1300
    #loop over elk element van de mogleijkheden
    for element in mogelijkheden:
        #worst case als variabelen instellen
        wc = int(frequentielijst(mogelijkheden,element))
        #als de worst case lager is dan de laagste tot nu to
        if wc <= laagste:
            #dit wordt de nieuwe beste worst case
            laagste = wc
            nieuwegok = element
    #return de gok
    return nieuwegok



def main_game():
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
            gok = laagste_kiezen(mogelijkheden)
            print(gok)
        else:
            #als er een fout is opgetreden print dat
            print("De code is ongeldig")
            return
        #als de gok goed is print in hoeveel stappen het is gelukt
        if list(gok) == code:
            print(f"gevonden in {stappen} stappen !")
            break
        #verwijder het eerste element (de gok)
        mogelijkheden.remove(gok)
        #geef feedback terug over de gok
        feedback = geef_feedback(code,gok)
        #pas de mogleijkheids lijst aan door alles wat niet meer kan weg te strepen
        lijst_aanpassen(gok,feedback)

#speel oneindig het spel
while True:
    main_game()