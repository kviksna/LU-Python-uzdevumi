# Uzdevums: 01-1: Izveidot programmu, kas prasa lietot�jam ievad�t skaitli n, tad programma apr��ina n+nn+nnn. Rezult�ts tiek par�d�ts konsol�.

sk = input("Enter number: ")
sum = int(sk) + int(sk*2) + int(sk*3)
print(sk,"+",sk*2,"+",sk*3,"=",sum)
#print(sk+"+"+sk*2+"+"+sk*3+"="+str(sum)) #bez atstarp�m