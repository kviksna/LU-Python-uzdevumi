# 2021.03.04, Uzd 5:
# Izveidot klasi Phone. Klasei ir klases atribūti brand un os. Ir instances atribūts number, kura vērtība ir nejauši
# ģenerēts 11 ciparu skaitlis. Uz Phone klases pamata izveidot klasi Samsung un Apple.

import random
import string


class Phone:
    brand = None
    os = None

    def __init__(self, msisdn):
        self.brand = None
        self.os = None
        self.msisdn = msisdn

    def __str__(self):
        #raise NotImplementedError
        #pass
        return f"This instance phone is {self.brand} with OS {self.os}"

    def set_brand(self, brand):
        self.brand = brand


class Samsung(Phone):
    brand = "Samsung"
    os = "Android"
    amount = 0

    def __init__(self, msisdn):
        super().__init__(msisdn=msisdn)
        Samsung.amount += 1


class Apple(Phone):
    brand = "Apple"
    os = "iOS"
    amount = 0

    def __init__(self, msisdn):
        super().__init__(msisdn=msisdn)
        Apple.amount += 1


def gen_msisdn():
    return ''.join((random.choice(string.digits) for i in range(11)))


print(gen_msisdn())
phone_1 = Samsung(gen_msisdn())
phone_2 = Apple(gen_msisdn())
print(phone_1)
print(phone_2)
