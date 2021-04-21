# Patstāvīgais darbs 2022-02-05 (pēc 7 nodarbības)
# Izveidot programmu, kurā būtu saraksts ar lietotājiem. Programmā ir izvēle, iegūt informāciju par konkrētu lietotāju,
# pievienot jaunu lietotāju, dzēst lietotāju no saraksta vai pārtraukt programmas izpildi.
#
# Izvēloties opciju “iegūt informāciju” tiek piedāvāta iespēja atrast lietotāju pēc e-pasta vai lietotājvārda.
# Ja lietotājs ir atrasts, tiek izvadīta visa zināma informācija par lietotāju, ja nav, tiek izvadīts atbilstošs paziņojums.
#
# Izvēloties opciju “pievienot lietotāju” sarakstam tiek pievienots lietotājs. Lai izveidotu lietotāju ir nepieciešams
# norādīt tā vārdu, lietotājvārdu, e-pastu. Automātiski tiek saglabāts laiks, kurā tika pievienots lietotājs.
#
# Izvēloties opciju “dzēst lietotāju” tiek piedāvāta iespēja atrast lietotāju pēc e-pasta vai lietotājvārda.
# Ja lietotājs ir atrasts, tas tiek dzēsts no saraksta, ja nav, tad tiek izvadīts atbilstošs paziņojums.
#
# Pēc izvēlētās darbības izpildīšanas lietotājam atkal tiek piedāvātas 4 opcijas.

from datetime import datetime

class User:
    def __init__(self, name, user_name, email, created):
        self.name = name
        self.user_name = user_name
        self.email = email
        self.created = created


users = []
users.append(User(name="Lucy", user_name="Australopithecus", email="Dinkinesh@Ethiopia.his", created="1974.11.24"))
users.append(User(name="Albert", user_name="Emc2", email="Albert.Einstein@relativity.de", created="1879.03.14"))
users.append(User(name="Elon", user_name="IronMan", email="Elon.Musk@tesla.com", created="1971.06.28"))

def user_add():
    print("\nAdd new user:")
    name = input("Name: ")
    user_name = input("Username: ")
    email = input("Email: ")
    created = datetime.now().strftime("%Y.%m.%d %H:%M:%S")
    users.append(User(name=name, user_name=user_name, email=email, created=created))
    print("User added at:", created)

def user_idx_search():  # search for 1st occurance!
    found_idx = -1  # not found yet
    search_str = input("\nSearch user by Name, Email or Username: ").lower()
    for i in range(len(users)):
        if search_str in users[i].name.lower():
            print(f"[{search_str}] found at Name[{users[i].name}]")
            return i
        if search_str in users[i].email.lower():
            print(f"[{search_str}] found at Email[{users[i].email}]")
            return i
        if search_str in users[i].user_name:
            print(f"[{search_str}] found at Username[{users[i].user_name}]")
            return i
    return found_idx


while True:  # main menu
    # print("")  # New line
    print(f"\nUsers stored: {len(users)}")
    print("[1] to search user by email or username")
    print("[2] to add new user")
    print("[3] to delete user")
    print("[4] to exit")
    try:
        ans = int(input("Your choice: "))
    except ValueError:
        print("Wrong choice! You entered non integer value!")
        continue  # to main menu
    if ans == 4:
        break  # Quit main menu loop
    elif ans == 1:
        i = user_idx_search()
        if i != -1:
            print("User found: ", users[i].name, users[i].user_name, users[i].email, users[i].created)
        else:
            print("User not found!")
    elif ans == 2:
        user_add()
    elif ans == 3:
        user_to_del = user_idx_search()
        if user_to_del != -1:  # not found
            if input(f"Delete user [{user_to_del}]={users[user_to_del].name} ? (Y/n): ") == "Y":
                users.pop(user_to_del)
                print("User deleted!")
    elif ans == 5:
        # print("\nStored users: ")
        for i in users:
            print(i.name, i.user_name, i.email, i.created)
    else:
        print("Wrong choice! You entered: ", ans)
print("Exiting... Bye!")
