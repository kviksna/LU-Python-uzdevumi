# 2021.03.04, Uzd 5:
# Izveidot klasi Phone. Klasei ir klases atribūti brand un os. Ir instances atribūts number, kura vērtība ir nejauši
# ģenerēts 11 ciparu skaitlis. Uz Phone klases pamata izveidot klasi Samsung un Apple.

import random
import string


class Phone:
    def __init__(self, brand, os, msisdn):
        self.brand = brand
        self.os = os
        self.msisdn = msisdn

    def __str__(self):
        return f"{self.brand}, {self.os}, {self.msisdn}"

    def set_brand(self):
        print("Brand of the phone change is physically impossible!")


def gen_msisdn():
    return ''.join((random.choice(string.digits) for i in range(11)))


# print(gen_msisdn())
phone_1 = Phone("Samsung", "Android", gen_msisdn())
phone_2 = Phone("Apple", "iOS", gen_msisdn())
print(phone_1)
print(phone_2)
