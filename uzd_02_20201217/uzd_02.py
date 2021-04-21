"""
Izveidot spēli “Akmens šķēres papīrīt’s”.
Lietotājs ievada skaitli 1, 2 vai 3. Skaitlis 1 apzīmē akmeni, 2 – šķēres, 3 – papīru.
Programma nejauši izvēlās akmeni, šķēres, vai papīru.
Uz ekrāna tiek parādīts ko ir izvēlējies lietotājs, ko – dators.
Ja lietotājs ir uzvarējis vienu reizi, lietotājam tiek piešķirts punkts, ja ir uzvarējis dators,
punkts tie piešķirts datoram. Ja lietotājs un dators ir izvēlējušies vienādu elementu, punkts
netiek piešķirts nevienam.
Pēc katra mēģinājuma tiek parādīts lietotāja un datora punktu skaits.
Spēle turpinās tiklīdz kāds, dators vai lietotājs, iegūst trīs punktus.
"""

from random import randint

words = ["Exit", "Rock", "Paper", "Scissors"]
winUser = 0
winComp = 0

while winUser < 3 and winComp < 3:
    print("Enter 1 for Rock, 2 for Paper, 3 for Scissors (0 to exit)")
    skUser = int(input("Your turn: "))
    if skUser == 0:
        print("Exiting...")
        quit()  # terminates program execution
    if skUser not in [1, 2, 3]:
        print(f"Wrong choice: {skUser}\n")
        continue  # to new loop cycle
    skComp = randint(1, 3)
    print(f"{words[skUser]} vs. {words[skComp]}")
    if skUser == skComp:
        print("Draw.")
    if (skUser == 1 and skComp == 3) or (skUser == 2 and skComp == 1) or (skUser == 3 and skComp == 2):
        winUser += 1
        print("User wins this round.")
    if (skComp == 1 and skUser == 3) or (skComp == 2 and skUser == 1) or (skComp == 3 and skUser == 2):
        winComp += 1
        print("Computer wins this round.")
    print(f"{winUser}:{winComp}\n")

if winUser == 3:
    print("User wins!")
if winComp == 3:
    print("Computer wins!")
