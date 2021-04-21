# Uzdevums 03_01:
# Apgriezt pozitīva skaitļa ciparu secību. Piemērs: 12345 => 54321

strSk = input("Ievadiet pozitīvu skaitli: ")
try:
    sk = int(strSk)
    if sk > 0:
        print("Apgrieztais skaitlis: ", end=" ")
        for i in range(len(strSk)-1, -1, -1):
            print(strSk[i], end="")
    else:
        print("Nav ievadīts pozitīvs skaitlis!")
except ValueError:
    print("Nav ievadīts skaitlis!")