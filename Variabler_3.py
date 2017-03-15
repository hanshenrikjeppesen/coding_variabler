"""
__________________________________________________
VARIABLER OG DATATYPER 3

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
# TEKST

myFirstName = "Hans"
mySecondName = 'Henrik'
myLastName = "Jeppesen"
print('\n')

# Vi kan få antal af bogstaver i variablen med metoden len

antalBogstaver1 = len(myFirstName)
antalBogstaver2 = len(mySecondName)
antalBogstaver3 = len(myLastName)

antalTotal = antalBogstaver1 + antalBogstaver2 + antalBogstaver3

print(antalBogstaver1)
print(antalBogstaver2)
print(antalBogstaver3)

print('\n')

print(antalTotal)

print('\n')

myFullName = myFirstName + mySecondName + myLastName
print(myFullName)
print(len(myFullName))

print('\n')

myFullName = myFirstName + ' ' + mySecondName + ' ' + myLastName
print(myFullName)
print(len(myFullName))

print('\n')
print(20*'-' +  'QUIZ TIME' + 20*'-')
print('\n')
print('Nu er vi klar til den første kahoot Quiz - Variabler_1')

