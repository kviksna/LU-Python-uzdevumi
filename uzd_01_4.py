# Izveidot kalkulatoru. Programma prasa lietotājam ievadīt divus skaitļus. Ar šiem skaitļiem tiek veiktas operācijas (saskaitīšana, atņemšana, reizināšana, dalīšana). Rezultāts tiek parādīts konsolē.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(num1, "+", num2, "=", num1 + num2)
print(num1, "-", num2, "=", num1 - num2)
print(num1, "*", num2, "=", num1 * num2)
print(num1, "/", num2, "=", num1 / num2)
#null check:
#print(num1, "/", num2, "=", "E" if num2==0 else num1 / num2)