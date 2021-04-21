# Izveidot programmu, kura prasa lietotâjam sekunþu skaitu. Sekundes tiek pârveidotas par “x hours y minutes z seconds” tipa tekstu. Rezultâts tiek parâdîts konsolç.

sec = int(input("Seconds: "))
h = sec//(60*60)
min = (sec-(h*60*60))//60
sec2 = sec-(h*60*60)-(min*60)
print(h, "hours", min, "minutes", round(sec2), "sec.")