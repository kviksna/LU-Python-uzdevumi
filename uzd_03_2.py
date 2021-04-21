# Uzdevums 03_02:
# Atrast cik skaitļi norādītajā intervālā dalās ar lietotāja norādīto dalītāju.

start = int(input("Start: "))
end = int(input("End: "))
div = int(input("Divider: "))
cnt = 0
for i in range(start, end+1):
    if i%div == 0:
        cnt += 1
print(f"{cnt} numbers between {start} and {end} can be divided by {div}")