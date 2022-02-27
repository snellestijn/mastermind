#hier staan de functies die worden gebruikt bij het spel mastermind


import random
import itertools

#functie voor het leveren van feedback op een gok
#gemaakt door docent in de les
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
    for i in range(len(kopie_code) - 1): 
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
    for i in range(len(kopie_code)):
        # Zit de kleur ergens anders in de code
        if guess[i] in kopie_code:     
            # Verhoog de counter
            juiste_kleur += 1
            # Vervang het element, zodat we geen dubbele feedback krijgen
            kopie_code[kopie_code.index(guess[i])] = '-'
            guess[i] = ''
    return (helemaal_goed, juiste_kleur)


#functie om een willekeurig code te genereren (bron: docent)
def code_generen(kleuren):
    return tuple(random.choices(kleuren,k=4))

#kijk of het antwoord juist is
def geraden(feedback):
    
    #de feedback methode uit de les wil nog wel eens 3,1 geven ;/
    if feedback == (3,1) or feedback == (4,0):
        return True
    return False

#beoordeel of de code valid is
def valid(code,kleuren):
    
    #moet 4 cijfers lang zijn
    if len(code) != 4:
        return False
    #en moet uit de kleuren bestaan (Hoofdletter lijst 'kleuren')
    for c in code:
        if c not in kleuren:
            return False
    return True
 
#functie om de feedback mooier (duidelijker) weer te geven
def feedback_printen(feedback):
    print(f"{feedback[0]} letter(s) staan op de goede plek.")
    print(f"{feedback[1]} letter(s) staan niet op de goede plek")

#maak een lijst van alle mogelijke antwoorden (bron: docent)
def permutaties(kleuren):
    perms = itertools.product(kleuren, repeat=4)
    return [p for p in perms]

#functie om de lijst up te daten (onmogelijke antwoorden eruit filteren)
def mog_updaten(over,gok,feedback):
    #een kopie van de lijst maken
    lijst = over
    
    #loop over de elementen van de lijst
    count = 0
    while count < len(lijst):
        
        #als de feedback niet overeen komt met de gegeven gok
        if feedback != geef_feedback(gok,lijst[count]):
            
            #dan kan dat het antwoord niet zijn en dus verwijder uit de lijst
            lijst.pop(count)
            count = 0
        
        #while loop om 'out of range' te verkomen
        else: count += 1
    return lijst



def gokken(kleuren):
    #vraag om een input gok
    gues = input("Geef een 4 Letterige code: ")
    while not valid(gues,kleuren):
        #zolang de gok niet geldig is blijf opnieuw om een gok vragen
        print("Zorg dat uw vier letterige code kloppend is\n")
        gues = input("Geef een 4 Letterige code: ")
    return gues