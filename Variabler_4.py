"""
__________________________________________________
VARIABLER OG DATATYPER 4

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

# List kan bruges til at opbevare flere værdier i
# og er omgivet af hård klamme [] og adskildt af komma

alpha = "a b c d e f g h i j k l m n o p q r s t u v w x y z æ ø å"
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
myListAlpha = alpha.split()     # split() en smart method til at opdele en tekst / string til en liste

print(40*'-')
print('Variablen "alpha" er af typen {}'.format(type(alpha)))
print('Variablen "numbers" er af typen {}'.format(type(numbers)))


print('\n')

print(myListAlpha)

print('\n')

# på Sammen måde som vi kunne får antal af bogstaver i en string (tekst)
# kan Vi kan også tælle indhold i listen, altså hvor mange elementer
# indeholder listen. Vi bruger samme metode len()

print('Listen "myListeAlpha" indeholder {} elementer'.format(len(myListAlpha)))

# Som med en tekst / String kan vi slice en liste og få uddrag af den
print('\n')
print(10*'-' + ' SLICING ' + 20*'-')
print('\n')

x = int(input('Hvilket nummer elementer vil du have vist i listen, indtast et tal mellem 0 og 28: '))

print('\n')

print('Element nummer {} i listen "myListAlpha" er {}'.format(x, myListAlpha[x]))

# En liste kan indeholde forskellige datatyper
print('\n')
print(10*'-' + ' Forskellige datatyper i én liste ' + 20*'-')
print('\n')

newList = [1, "tomat", 42, "cheeseburger", 2.0, myListAlpha]  # En liste kan også indeholde en liste

print('herunder er vores newList')
print(newList)

print('\n')

x = int(input('Hvilket nummer elementer vil du have vist i listen, indtast et tal mellem 0 og 5: '))

print('\n')

print('Element nummer {} i listen "myListAlpha" er {} og er af typen {}'.format(x, newList[x], type(newList[x])))

print('\n')
print(10*'-' + ' Prøv igen denne gang prøv nr. 5 ' + 20*'-')
print('\n')
x = int(input('Hvilket nummer elementer vil du have vist i listen, indtast et tal mellem 0 og 5: '))

print('\n')

print('Element nummer {} i listen "myListAlpha" er {} og er af typen {}'.format(x, newList[x], type(newList[x])))
