# Izveidot spçli “Akmens ðíçres papîrît’s”.
# Lietotâjs ievada skaitli 1, 2 vai 3. Skaitlis 1 apzîmç akmeni, 2 – ðíçres, 3 – papîru.
# Programma nejauði izvçlâs akmeni, ðíçres, vai papîru.
# Uz ekrâna tiek parâdîts ko ir izvçlçjies lietotâjs, ko – dators.
# Ja lietotâjs ir uzvarçjis vienu reizi, lietotâjam tiek pieðíirts punkts, ja ir uzvarçjis dators,
# punkts tie pieðíirts datoram. Ja lietotâjs un dators ir izvçlçjuðies vienâdu elementu, punkts
# netiek pieðíirts nevienam.
# Pçc katra mçìinâjuma tiek parâdîts lietotâja un datora punktu skaits.
# Spçle turpinâs tiklîdz kâds, dators vai lietotâjs, iegûst trîs punktus.

import sys  # for sys.exit()
from random import randint

winUser = 0
winComp = 0

while winUser == 3 or winComp == 3:
    print("Enter 1 for Rock, 2 for Paper, 3 for Scissors (0 to exit)")
    skUser = int(input("Your turn: "))
    if skUser == 0:
        print("Exiting...")
        sys.exit() # terminates program execution
    if skUser not in [1,2,3]:
        print("Wrong choice: ", skUser)
        quit() # terminate this loop cycle
    skComp = randint(1,3)
    print(f"{skUser} vs. {skComp}")
    if skUser == skComp:
        print("Draw.")
    if (skUser == 1 and skComp == 3) or (skUser == 2 and skComp == 1) or (skUser == 3 and skComp == 2):
        winUser += 1
        print("User wins this round.")
    if (skComp == 1 and skUser == 3) or (skComp == 2 and skUser == 1) or (skComp == 3 and skUser == 2):
        winComp += 1
        print("Computer wins this round.")
    print(f"{winUser}:{winComp}")

if winUser == 3:
    print("User wins!")
if winComp == 3:
    print("Computer wins!")
