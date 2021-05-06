from django.shortcuts import render, HttpResponse
from user.models import User
from django.views.generic import View, ListView, FormView, DetailView
from django.urls import reverse_lazy
from user.forms import UserForm


class UserListView(ListView):
    model = User
    template_name = 'user_list.html'


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'


class AddUserView(FormView):

    form_class = UserForm
    template_name = 'add_user.html'
    success_url = reverse_lazy('user-list')

    def form_valid(self, form):
        form.save()

        response = super().form_valid(form)
        return response


def index(request):

    users = User.objects.all()

    context = {
        'users': users,
    }

    return render(
        template_name='index.html',
        request=request,
        context=context,
    )


def add_user(request):

    if request.method == 'POST':

        user = User(
            username=request.POST['name'],
            email=request.POST['email'],
        )

        user.save()

        context = {
            'user': user,
        }

        return render(
            template_name='deposit.html',
            request=request,
            context=context,

        )

    return render(
        template_name='deposit_new.html',
        request=request
    )


def get_user(request, user_id):

    user = User.objects.get(pk=user_id)

    context = {
        'user': user,
    }

    return render(
        template_name='deposit.html',
        request=request,
        context=context,

    )


def delete_user(request, user_id):

    user = User.objects.get(pk=user_id)
    user.delete()

    return HttpResponse(f'Deleted {user.username}')


def edit_user(request, user_id):

    user = User.objects.get(id=user_id)

    if request.method == 'POST':

        username = request.POST['name']
        email = request.POST['email']

        if len(username) != 0:
            user.username = username

        if len(email) != 0:
            user.email = email

        user.save()

        context = {
            'user': user,
        }

        return render(
            template_name='deposit.html',
            request=request,
            context=context,

        )

    return render(
        template_name='deposit_new.html',
        request=request
    )