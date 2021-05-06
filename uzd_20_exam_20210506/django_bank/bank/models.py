from django.db import models


class Deposit(models.Model):

    def __init__(self):
        interest = 0
        for i in range(self.term):
            interest += self.deposit * self.rate
        self.interest = interest

    deposit = models.IntegerField(verbose_name="Deposit (euro)")
    term = models.IntegerField(verbose_name="Term (years)")
    rate = models.FloatField(verbose_name="Rate (decimal")

    @property
    def interest(self):
        interest = 0
        for i in range(self.term):
            interest += self.deposit * self.rate
        self.interest = interest
