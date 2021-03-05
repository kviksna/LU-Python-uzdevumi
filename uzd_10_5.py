# 2021.03.04, Uzd 5:
# Izveidot klasi Phone. Klasei ir klases atribūti brand un os. Ir instances atribūts number, kura vērtība ir nejauši
# ģenerēts 11 ciparu skaitlis. Uz Phone klases pamata izveidot klasi Samsung un Apple.

import random
import string

class Phone:
    def __init__(self, msisdn):
        self.brand = None
        self.os = None
        self.msisdn = msisdn
    def __str__(self):
        pass
    def set_brand(self, brand):
        self.brand = brand

class Samsung(Phone):
    # def __init__(self):
        #super.brand = "Samsung"
        super.set_brand("Samsung")
        super.os = "Android"

class Apple(Phone):
    # def __init__(self):
        super.brand = "Apple"
        super.os = "iOS"


def gen_msisdn():
    return ''.join((random.choice(string.digits) for i in range(11)))


print(gen_msisdn())
phone_1 = Samsung(gen_msisdn())
phone_2 = Apple(gen_msisdn())
print(phone_1)
print(phone_2)
