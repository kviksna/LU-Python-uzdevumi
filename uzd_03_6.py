# Uzdevums 03_06:
# Izveidot reizināšanas tabulu lietotāja ievadītam skaitlim.

strSk = input("Ievadiet skaitli: ")
try:
    sk = int(strSk)
    for i in range(10):
        print(f"{sk}*{i+1}={sk*(i+1)}")
except ValueError:
    print("Nav ievadīts skaitlis!")