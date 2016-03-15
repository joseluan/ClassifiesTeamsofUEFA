from random import randint
from collections import OrderedDict

print "---Classifies the UEFA Champions League teams---"
print ""
print "Enter resultadopra show rating"
print ""

dicionario = {'Athletic Club': 0, 'Arsenal': 0, 'Galatasaray': 0, 'Shakhtar Donetsk': 0, 'AS Roma': 0, 'Barcelona': 0, 'PFC Moskva': 0, 'Bayer Leverkusen': 0, 'Juventus': 0, 'Basel': 0, 'Benfica': 0, 'Atletico de Madrid': 0, 'Schalke 04': 0, 'Anderlecht': 0, 'Ludogorets Razgrad': 0, 'BATE Borisov': 0, 'NK Maribor': 0, 'Ajax': 0, 'Malmo FF': 0, 'Borussia Dortmund': 0, 'Liverpool': 0, 'Sporting Clube de Portugal': 0, 'Paris Saint-Germain': 0, 'Bayern Leverkusen': 0, 'AS Monaco': 0, 'Real Madrid': 0, 'FC Porto': 0, 'APOEL': 0, 'Manchester City': 0, 'Zenit': 0, 'Zenit': 0, 'Chelsea': 0, 'Bayern': 0, 'Olympiacos': 0}
xlista = []
x = []
y = 0
lista = dicionario.keys()
while y == 0:

     prime =lista[randint(0,25)]
     segund = lista[randint(0,25)]
     while prime == segund:
          prime =lista[randint(0,25)]
          segund = lista[randint(0,25)]

     print "A =  %s    VS    B = %s" %(prime,segund)
     escolha = raw_input("Enter the club of your choice: ")
     if escolha.upper() == "RESULT":
                    y = 1
                    x.append(1)
     while x == []:
          if escolha.upper() == "A" or escolha.upper() == "B":
               if escolha.upper() == "B":

                    segundindex = lista.index(prime)
                    sorted_dict = sorted(dicionario.items(), key = lambda t: t[1])
                    xlista = (OrderedDict(sorted_dict[::-1]))

                    dicionario[segund] += 1.0/(400+len(lista)+segundindex)

                    x.append(1)
               if escolha.upper() == "A":

                    primeindex = lista.index(segund)
                    sorted_dict = sorted(dicionario.items(), key = lambda t: t[1])
                    xlista = (OrderedDict(sorted_dict[::-1]))

                    dicionario[prime] += 1.0/(400+len(lista)+primeindex)

                    x.append(1)
          else:
               escolha = raw_input("Enter the club of your choice: ")
               if escolha.upper() == "RESULT":
                    y = 1
                    x.append(1)
          if escolha.upper() == "RESULTADO":
               y = 1
               x.append(1)
     x = []

sorted_dict = sorted(dicionario.items(), key = lambda t: t[1])
xlista = (OrderedDict(sorted_dict[::-1]))

print "\n\n\n"
contador = 1
for x in xlista:
     print contador, " : ", x
     contador += 1


     

