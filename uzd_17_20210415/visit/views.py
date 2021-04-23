from django.shortcuts import render
from visit.models import Visit


def index(request):
    info = None
    if request.method == 'POST':

        visit = Visit(
            name=request.POST['name'],
            date=request.POST['date'],
            reason=request.POST['reason'],
        )

        visit.save()

        info = f"added {visit.name} ({visit.reason}) with ID: {visit.id}"

    # Delete entry by id
    elif request.method == 'GET':

        del_id = int(request.GET.get('del', 0))
        if del_id > 0:
            visit = Visit.objects.get(id=del_id)
            visit.delete()
            info = f"deleted {visit.name} ({visit.reason}) with ID: {visit.id}"

        edit_id = int(request.GET.get('edit', 0))
        if edit_id > 0:
            info = f"edit not implemented yet! (ID: {edit_id})"

    # View all objects
    visits = Visit.objects.all()

    context = {
        'info': info,
        'visits': visits,
    }

    return render(
        template_name='index.html',
        request=request,
        context=context,
    )
