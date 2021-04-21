# Kâda valsts nolçma pâriet uz jaunu naudas sistçmu. Vecajâ sistçmâ bija trîs naudas vienîbas: dâlderis, grasis, santîms. Naudas vçrtîbas norâdîtas zemâk.
# 1 dâlderis = 37 graði
# 1 grasis = 162 santîmi
# Jaunajâ naudas sistçmâ paliek tikai santîmi un dâlderi. Santîms saglabâ savu vçrtîbu, bet 1 dâlderis bûs vienâds ar 100 santîmiem. Izveidot programmu, kas pârveidotu vecâs sistçmas naudu uz jaunu. Lietotâjam prasa ievadît vecâs sistçmas dâlderus, graðus un santîmus. Tiek aprçíinâts jaunâs sistçmas dâlderu un graðu daudzums. Rezultâts tiek parâdîts konsolç.

dald = int(input("Dâlderi: "))
gras = int(input("Graði: "))
cents = int(input("Santîmi: "))

cents = cents + gras*162 + dald*37*162
dald2 = cents//100
cents2 = cents - dald2*100

print("Jaunie dâlderi: ", dald2)
print("Jaunie santîmi: ", cents2)