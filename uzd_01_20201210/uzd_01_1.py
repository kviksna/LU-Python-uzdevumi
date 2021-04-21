# Uzdevums: 01-1: Izveidot programmu, kas prasa lietotâjam ievadît skaitli n, tad programma aprçíina n+nn+nnn. Rezultâts tiek parâdîts konsolç.

sk = input("Enter number: ")
sum = int(sk) + int(sk*2) + int(sk*3)
print(sk,"+",sk*2,"+",sk*3,"=",sum)
#print(sk+"+"+sk*2+"+"+sk*3+"="+str(sum)) #bez atstarpçm