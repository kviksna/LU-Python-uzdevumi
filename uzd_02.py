# Izveidot spçli “Akmens ðíçres papîrît’s”.
# Lietotâjs ievada skaitli 1, 2 vai 3. Skaitlis 1 apzîmç akmeni, 2 – ðíçres, 3 – papîru.
# Programma nejauði izvçlâs akmeni, ðíçres, vai papîru.
# Uz ekrâna tiek parâdîts ko ir izvçlçjies lietotâjs, ko – dators.
# Ja lietotâjs ir uzvarçjis vienu reizi, lietotâjam tiek pieðíirts punkts, ja ir uzvarçjis dators, punkts tie pieðíirts datoram. Ja lietotâjs un dators ir izvçlçjuðies vienâdu elementu, punkts netiek pieðíirts nevienam.
# Pçc katra mçìinâjuma tiek parâdîts lietotâja un datora punktu skaits.
# Spçle turpinâs tiklîdz kâds, dators vai lietotâjs, iegûst trîs punktus.

print("")
sk = input("Enter number: ")
sum = int(sk) + int(sk*2) + int(sk*3)
print(sk,"+",sk*2,"+",sk*3,"=",sum)
#print(sk+"+"+sk*2+"+"+sk*3+"="+str(sum)) #bez atstarpçm