# Uzdevums 03_05:
# Atrast pozitīva skaitļa ciparu summu. Piemērs: 14214 => 12

strSk = input("Ievadiet pozitīvu skaitli: ")
sum = 0
try:
    sk = int(strSk)
    if sk > 0:
        for i in strSk:
            sum += int(i)
        print("Skaitļa ciparu summa: ", sum)
    else:
        print("Nav ievadīts pozitīvs skaitlis!")
except ValueError:
    print("Nav ievadīts skaitlis!")