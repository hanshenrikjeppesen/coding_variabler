"""
__________________________________________________
VARIABLER OG DATATYPER 5

Vi skal lære om variabler og datatyper,
Hvordan vi bruger variabler og
hvordan vi gemmer dem

Variabler anvendes til at lagre information,
der skal refereres og manipuleres i et computerprogram
__________________________________________________

I python har vi 5 forskellige standard datayper:

- Tal (numbers)
- Tekst (Strings)
- List              <===
- Tuple
- Dictionary
__________________________________________________

"""
print(10*'-' + ' LIST ' + 20*'-')
print('\n')

myList = ['Tomater', 'Salat', 'Slik', 'Chips', 'Broccoli', 'Mælk', 'Cola']

print(myList)
print('Vores liste "myList" indeholder {} elementer'.format(len(myList)))


print('\n')
print(10*'-' + ' Ændringer i list ' + 20*'-')
print('\n')

print('Element nummer {} i "myList er {}'.format(4, myList[4]))

print('\n')
# Vi kan ændre et element i listen

myInput = input('Hvad vil du gerne skifte element nr. {} som er {} ud med? '.format(4, myList[4]))
myList[4] = myInput

print('\n')

print('Element nummer {} i "myList er {}'.format(4, myList[4]))
print(myList)

print('\n')
print(10*'-' + ' Tilføje til en list ' + 20*'-')
print('\n')

myInput = input('Hvad vil du gerne tilføje til listen "myList"? ')

myList.append(myInput)      # append() metoden tilføjer et element til vores liste

print('\n')

print(myList)
print('Vores liste "myList" indeholder {} elementer'.format(len(myList)))

print('\n')
print(10*'-' + ' Slette et element i LIST ' + 20*'-')
print('\n')
print('Vores liste ser sådan her ud og har {} elementer'.format(len(myList)))
print(myList)
print('\n')

element = int(input('Hvilket element i listen vil du fjerne? (0-7): '))

del myList[1]

print('\n')
print('Nu ser vores liste sådan her ud og har {} elementer'.format(len(myList)))
print(myList)

print('\n')
print(20*'-' +  ' QUIZ TIME ' + 20*'-')
print('\n')
print('Nu er vi klar til den næste kahoot Quiz - Variabler_2')
