"""
__________________________________________________
VARIABLER OG DATATYPER 2

Vi skal lære om variabler og datatyper,
Hvordan vi bruger variabler og
hvordan vi gemmer dem

Variabler anvendes til at lagre information,
der skal refereres og manipuleres i et computerprogram
__________________________________________________

I python har vi 5 forskellige standard datayper:

- Tal (numbers)
- Tekst (Strings)
- List
- Tuple
- Dictionary
__________________________________________________

"""
# TAL (numbers) så vi i Variabler_1.py kunne være:

myFirstVar = 1  # af typen int
mySecVar = 2.0  # af typen float

print(myFirstVar)
print(type(myFirstVar))

print('\n')

print(mySecVar)
print(type(mySecVar))


# der er også complex og long men dem gemmer vi lige

# TEKST eller strings er variabler som indeholder en tekst
# skrives i mellem par af citationstegn enten '' eller ""

myFirstName = "Hans"
mySecondName = 'Henrik'
myLastName = "Jeppesen"
print('\n')
# Vi kan sætte disse tre variabler sammen ved at bruge "string concatenation operator" som er plus tegn (+)

print(myFirstName + mySecondName + myLastName)
print('\n')
print('Men der er mangler mellemrum så vi prøver lige igen')
print('\n')
print(myFirstName + ' ' + mySecondName + ' ' + myLastName)
print('\n')
print('Vi kan også anvende en anden metode "format"')
print('\n')
print('Mit fulde navn er: {} {} {}'.format(myFirstName, mySecondName, myLastName))

print(40*'-')

# Tekst kan vi dele / slice op så vi kan tager uddrag af teksten det gøres med []:

print(myFirstName[0])       # Dette giver os det første bogstav i mit navn
print(myFirstName[-1])      # Dette giver os det sidste bogstav i mit navn
print(myFirstName[1:3])     # Dette giver os fra bogstav nr.2 (husk 0-index) og til men ikke med nr. 3

print('\n')

print(myFirstName[-1] + myFirstName[-2] + myFirstName[1] + myFirstName[0])




