# Zemniekam ir govis, cûkas un vistas. Govîm un cûkâm ir pa 4 kâjâm, vistâm – 2. Izveidot programmu, kas prasa lietotâjam ievadît cûku, govju un vistu skaitu. Tiek aprçíinâts kopçjais kâju daudzums. Rezultâts tiek izvadîts konsolç.

pigs = int(input("Amount of pigs: "))
cows = int(input("Amount of cows: "))
chicks = int(input("Amount of chickens: "))
print("Amount of legs: ", pigs*4 + cows*4 + chicks*2)