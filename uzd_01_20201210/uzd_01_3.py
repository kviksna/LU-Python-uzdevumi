# Izveidot programmu, kura prasa lietot�jam sekun�u skaitu. Sekundes tiek p�rveidotas par �x hours y minutes z seconds� tipa tekstu. Rezult�ts tiek par�d�ts konsol�.

sec = int(input("Seconds: "))
h = sec//(60*60)
min = (sec-(h*60*60))//60
sec2 = sec-(h*60*60)-(min*60)
print(h, "hours", min, "minutes", round(sec2), "sec.")