from django.shortcuts import render
from user.models import User


def index(request):
    info_invalid = ''  # Valid value

    # View all objects
    user = User.objects.all()

    context = {
        'user': user,
    }

    if request.method == 'POST':

        posted_name = request.POST.get('name', '')
        if posted_name == '':
            info_invalid = 'Username can not be empty!'

        user = User(
            name=request.POST.get('name', ''),
            email=request.POST.get('email', ''),
        )

        edit_id = int(request.POST.get('edit_id', 0))
        if edit_id > 0:
            user = User.objects.get(id=edit_id)
            user.name = request.POST.get('name', '')  # request.POST['name']
            user.email = request.POST.get('email', '')
            context['info'] = f"eddited {user.name} ({user.email}) with ID: {user.id}"
        else:
            context['info'] = f"added {user.name} ({user.email}) with ID: {user.id}"

        if info_invalid == '':
            user.save()
        else:
            context['info'] = info_invalid

    elif request.method == 'GET':

        del_id = int(request.GET.get('del', 0))
        if del_id > 0:
            user = User.objects.get(id=del_id)
            user.delete()
            context['info'] = f"deleted {user.name} ({user.email}) with ID: {user.id}"

        edit_id = int(request.GET.get('edit', 0))
        if edit_id > 0:
            user = User.objects.get(id=edit_id)
            context['edit_id'] = edit_id
            context['edit_name'] = user.name
            context['edit_email'] = user.email

    return render(
        template_name='index.html',
        request=request,
        context=context,
    )
