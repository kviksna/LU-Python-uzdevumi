from django.shortcuts import (
    render,
    HttpResponse,
    redirect,
)

from django.views.generic import (
    View,
    ListView,
    DetailView,
    FormView,
)

from django.urls import reverse_lazy

from bank.models import Deposit
from bank.forms import DepositForm


class DepositListView(ListView):

    model = Deposit
    template_name = 'index.html'


class DepositDetailView(DetailView):

    model = Deposit
    template_name = 'deposit.html'


class AddDepositView(FormView):

    form_class = DepositForm
    template_name = 'deposit_new.html'
    success_url = reverse_lazy('deposit-list')

    def form_valid(self, form):
        form.save()

        response = super().form_valid(form)
        return response
