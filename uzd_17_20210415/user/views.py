from django.shortcuts import render
from user.models import User


def index(request):

    # View all objects
    user = User.objects.all()

    context = {
        'user': user,
    }

    if request.method == 'POST':

        user = User(
            name=request.POST['name'],
            date=request.POST['date'],
            reason=request.POST['reason'],
        )

        edit_id = int(request.POST.get('edit_id', 0))
        if edit_id > 0:
            user = User.objects.get(id=edit_id)
            user.name = request.POST['name']
            user.reason = request.POST['reason']
            context['info'] = f"eddited {user.name} ({user.reason}) with ID: {user.id}"
        else:
            context['info'] = f"added {user.name} ({user.reason}) with ID: {user.id}"

        user.save()

    elif request.method == 'GET':

        del_id = int(request.GET.get('del', 0))
        if del_id > 0:
            user = User.objects.get(id=del_id)
            user.delete()
            context['info'] = f"deleted {user.name} ({user.reason}) with ID: {user.id}"

        edit_id = int(request.GET.get('edit', 0))
        if edit_id > 0:
            user = User.objects.get(id=edit_id)
            context['edit_id'] = edit_id
            context['edit_name'] = user.name
            context['edit_email'] = user.reason

    return render(
        template_name='index.html',
        request=request,
        context=context,
    )
