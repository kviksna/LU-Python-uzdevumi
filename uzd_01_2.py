# Izveidot programmu, kura prasa lietot�jam ievad�t cilindra r�diusu un t� augstumu, tiek apr��in�ts cilindra laukums un tilpums. Rezult�ts tiek par�d�ts konsol�.
# tilpums = 3.14 * r�diuss * r�diuss * augstums
# laukums = 2 * (3.14 * r�diuss * r�diuss) + augstums * (2 * 3.14 * r�diuss)

h = int(input("Enter the height: "))
r = int(input("Enter the radius: "))

pi = 3.14
vol = pi * r**2 * h
area = 2 * pi * r**2 + h * 2 * pi *r

print("Volume: ", vol)
print("Area: ", area)