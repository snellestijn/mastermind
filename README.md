# mastermind
School project voor mastermind

Speel het spel door playme.py te runnen.
Dit programma gebruikt functies uit andere bestanden.

De drie bruikbaare algoritmes zijn:

1. Simple
Dit algoritme kiest telkens het eerste mogelijke antwoord uit de lijst en sluit op basis van de gegeven feedback de onmogelijke antwoorden uit. en gaat zo door tot het juiste antwoord is gegeven.
De modale snelheid van dit algoritme is 6 pogingen

2. Worstcase
Dit algoritme bepaalt de volgende gok op basis van het berekenen welke gok in zijn slechtste geval het minste resterende aantal antwoorden over laat. Hier wordt dus telkens uit gegaan van de slechts mogelijke feedback. Dit algoritme is geinspireerd door de universiteit van groningen
De modale snelheid van dit algoritme is 6 pogingen

3. Willekeurig
Dit algoritme kies telkens een willekeurig antwoord en op basis van de feedback streept het de amtwoorden weg die niet meer mogelijk zijn.
De modale snelheid van dit algoritme is 5 pogingen


De modale snelheiden zijn bepaald door +- 20 testen te draaien en het meest voorkomende antwoord te nemen.
Willekeurig blijkt hieruit net iets sneller te zijn dan de andere twee algoritmes.
En overduidelijk zijn alle drie de aalgoritmes sneller dan ik :)