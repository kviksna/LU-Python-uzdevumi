from django.db import models


class Deposit(models.Model):
    def __init__(self):
        interest = 0
        for i in range(self.term):
            interest += self.deposit * self.rate
        self.interest = interest

    deposit = models.IntegerField()
    term = models.IntegerField()
    rate = models.FloatField()
