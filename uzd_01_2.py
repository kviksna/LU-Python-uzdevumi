# Izveidot programmu, kura prasa lietotâjam ievadît cilindra râdiusu un tâ augstumu, tiek aprçíinâts cilindra laukums un tilpums. Rezultâts tiek parâdîts konsolç.
# tilpums = 3.14 * râdiuss * râdiuss * augstums
# laukums = 2 * (3.14 * râdiuss * râdiuss) + augstums * (2 * 3.14 * râdiuss)

h = int(input("Enter the height: "))
r = int(input("Enter the radius: "))

pi = 3.14
vol = pi * r**2 * h
area = 2 * pi * r**2 + h * 2 * pi *r

print("Volume: ", vol)
print("Area: ", area)