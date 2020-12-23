# Izveidot sp�li �Akmens ���res pap�r�t�s�.
# Lietot�js ievada skaitli 1, 2 vai 3. Skaitlis 1 apz�m� akmeni, 2 � ���res, 3 � pap�ru.
# Programma nejau�i izv�l�s akmeni, ���res, vai pap�ru.
# Uz ekr�na tiek par�d�ts ko ir izv�l�jies lietot�js, ko � dators.
# Ja lietot�js ir uzvar�jis vienu reizi, lietot�jam tiek pie��irts punkts, ja ir uzvar�jis dators,
# punkts tie pie��irts datoram. Ja lietot�js un dators ir izv�l�ju�ies vien�du elementu, punkts
# netiek pie��irts nevienam.
# P�c katra m��in�juma tiek par�d�ts lietot�ja un datora punktu skaits.
# Sp�le turpin�s tikl�dz k�ds, dators vai lietot�js, ieg�st tr�s punktus.

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
