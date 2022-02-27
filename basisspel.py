#het hoofdscherm voor het speplen van master mind

from basismethodes import *
import slechtstekans
import time
import random





#het spel
def play(simple,worst,willekeurig):
    
    #de kleuren die in het spel gebruikt worden
    kleuren = ['R', 'O', 'Y', 'G', 'C', 'B']
    print(f"De kleuren zijn: {kleuren}")


    #het antwoord genereren
    code = code_generen(kleuren)
    print(code)
    
    #het max aantal pogingen instellen
    pogingen = 10
    
    #een lijst van alle mogelijke antwoorden aanmaken
    mogelijkheden = permutaties(kleuren)
    
    #gewonnen op false zolang de code niet geraden is
    gewonnen = False
    
    #de loop die afspeelt zolang het spel gespeeld wordt
    while pogingen:
        print(f"Er zijn nog {pogingen} pogingen over.")
        
        #bepaal welke moethode gebruikt wordt
        #per methode wordt steeds een nieuwe gok gedefinierd
        if simple:
            #simpel methode pakt de eerste uit de lijst
            gues = mogelijkheden[0]
        elif worst:
            #worstcase gok wordt bepaald met geinporteerde functie uit slechtstekans.py
            gues = slechtstekans.nieuwe_gok(mogelijkheden)
        elif willekeurig:
            #bij willekeurig wordt de nieuwe gok een willekeurig antwoord uit de lijst
            gues = random.choice(mogelijkheden)
        
        
        #manier om zelf te gokken
        else:
            gues = gokken(kleuren)

        #weergeef wat de gok is
        print(f"De gok: {gues}")

        #een poging gebruikt
        pogingen -= 1

        #geef feedback over de gok
        fb = geef_feedback(code,gues)
        #update de lijst met mogelijke antwoorden
        mogelijkheden = mog_updaten(mogelijkheden,gues,fb)
        
        
        
        #als alles op zijn plek staat dan is het spel klaar
        if geraden(fb):
            print(f"Gefeliciteerd het woord is geraden in {(10 - pogingen)} poging(en) ")
            gewonnen = True
            break
        
        #geef de feedback weer
        feedback_printen(fb)
        
        #print een witregel en laat de tijd een tijdje vertragen wachten (voor de sier)
        print("")
        time.sleep(0.1)
    
    #laat de gebruiker weten dat de code niet is geraden
    if not gewonnen:
        print("helaas de code is niet geraden!\nprobeer het opnieuw!")

