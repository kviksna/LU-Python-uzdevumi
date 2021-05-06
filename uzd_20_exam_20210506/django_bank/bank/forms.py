from django import forms
from bank.models import Deposit


class DepositForm(forms.ModelForm):
    class Meta:
        model = Deposit
        fields = [
            'deposit',
            'term',
            'rate',
        ]
