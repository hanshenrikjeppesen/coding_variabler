"""
__________________________________________________
VARIABLER OG DATATYPER 1

Vi skal lære om variabler og datatyper,
Hvordan vi bruger variabler og
hvordan vi gemmer dem

Variabler anvendes til at lagre information,
der skal refereres og manipuleres i et computerprogram
__________________________________________________

I Python har man Dynamically typed variabler, hvad betyder det så?

- Man skal ikke først deklarer type af variabel (det skal man i Java, C++ etc)
- Man kan ædre variabel type under programkørsel (runtime )
- kan indeholde forskellige typer i hele dens livstid

Hvordan give vi variabler et navn?

Style Guide: https://www.python.org/dev/peps/pep-0008/
__________________________________________________

"""
minVariabel = "mixedCase eller camelCase"
MinVariabel = "CapWords eller PascalCase"
min_variabel = "lower_case_with_underscores"
ENKONSTANT = "En variabel (Konstant) som ikke ændre sig og skrivers med STORT"
TIMER_PAA_EN_DAG = 24
myFirstVar = 4.012
mySecondVar = 2

# Det er lidt rodet, så der er ikke nogen entydig retningslinje
# Vær konsekvent:

print(40*'-')
print('Navngivning af Variabler')

print('\n')     # Dette er en "escape sequence" \n => en ny linje

print('Variablen "minVariabel" er {} og af typen {}'
      .format(minVariabel, type(minVariabel)))

print('\n')

print('Variablen "MinVariabel" er {} og af typen {}'
      .format(MinVariabel, type(MinVariabel)))

print('\n')

print('Variablen "min_Variabel" er {} og af typen {}'
      .format(min_variabel, type(min_variabel)))

print('\n')

print('Variablen "ENKONSTANT" er {}'
      .format(ENKONSTANT))

print('\n')

print('Variablen "TIMER_PAA_EN_DAG" er = {} og af typen {}'
      .format(TIMER_PAA_EN_DAG, type(TIMER_PAA_EN_DAG)))

print('\n')

print('Variablen "myFirstVar" er = {} og af typen {}'
      .format(myFirstVar, type(myFirstVar)))

print('\n')

print('Variablen "myFirstVar" + "TIMER_PAA_EN_DAG" er  = {} og af typen {}'
      .format(myFirstVar + TIMER_PAA_EN_DAG, type(myFirstVar + TIMER_PAA_EN_DAG)))

print('\n')

print('Variablen "mySecondVar" * "TIMER_PAA_EN_DAG" er  = {} og af typen {}'
      .format(mySecondVar * TIMER_PAA_EN_DAG, type(mySecondVar * TIMER_PAA_EN_DAG)))

print('\n')

print('Variablen "TIMER_PAA_EN_DAG" / "mySecondVar" er  = {} og af typen {}'
      .format(TIMER_PAA_EN_DAG / mySecondVar, type(TIMER_PAA_EN_DAG / mySecondVar)))

print(40*'-')
