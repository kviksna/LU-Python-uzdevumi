from django.shortcuts import render
from visit.models import Visit


def index(request):

    # View all objects
    visits = Visit.objects.all()

    context = {
        'visits': visits,
    }

    if request.method == 'POST':

        visit = Visit(
            name=request.POST['name'],
            date=request.POST['date'],
            reason=request.POST['reason'],
        )

        edit_id = int(request.POST.get('edit_id', 0))
        if edit_id > 0:
            visit = Visit.objects.get(id=edit_id)
            visit.name = request.POST['name']
            visit.reason = request.POST['reason']
            context['info'] = f"eddited {visit.name} ({visit.reason}) with ID: {visit.id}"
        else:
            context['info'] = f"added {visit.name} ({visit.reason}) with ID: {visit.id}"

        visit.save()

    # Delete entry by id
    elif request.method == 'GET':

        del_id = int(request.GET.get('del', 0))
        if del_id > 0:
            visit = Visit.objects.get(id=del_id)
            visit.delete()
            info = f"deleted {visit.name} ({visit.reason}) with ID: {visit.id}"

        edit_id = int(request.GET.get('edit', 0))
        if edit_id > 0:
            visit = Visit.objects.get(id=edit_id)
            context['edit_id'] = edit_id
            context['edit_name'] = visit.name
            context['edit_email'] = visit.reason

    return render(
        template_name='index.html',
        request=request,
        context=context,
    )
