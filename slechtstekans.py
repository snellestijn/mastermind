#hier staan de functies die worden gebruikt voor het expected algoritme

from basismethodes import *

#functie maken voor het meest voorkomde feedback per gok te bepalen
def frequentielijst(mogelijkheden,gok):
    #definier een lege dict
    freqs = dict()
    
    #per mogelijk antwoord uit de lijst van permutaties
    for antwoord in mogelijkheden:
        
        #kijk wat de feedback zou opleveren als dit het goeie antwoord is
        fb = geef_feedback(antwoord,gok)
        
        #als deze vorm van feedback nog niet in de frequentie lijst met feedbacks voorkomt
        if fb not in freqs:
            
            #voeg dan toe aan de lijst en zet het aantal op 0
            freqs[fb] = 0
        
        #tel een maal op bij de vorm van feedback
        freqs[fb] += 1
    #nu bestaat de lijst van feedbak uit keys: feedback en values: de frequentie ervan
    
    #bepaal wat de meest voorkomende feednack is
    hoogste = 0
    #per feedback, als deze vaker voorkomt..
    for freq in freqs:
        if freqs[freq] > hoogste:
            #dat is dan de nieuwe hoogste-frequentie
            hoogste = freqs[freq]
    #retrun het hoogste frequentie (oftewel wat is het slechts mogelijke resulaat)
    return hoogste


#functie voor de nieuwe gok bepalen
def nieuwe_gok(mogelijkheden):
    
    #ga elk mogelijke nieuwe gok langs
    for mog in mogelijkheden:
        
        #kijk wat de laagste worstcase is
        fre = frequentielijst(mogelijkheden,mog)
        laagste = 1300
        
        #stel dit in als gok
        if fre < laagste:
            laagste = fre
            gok = mog
    
    #retrun de gok
    return gok