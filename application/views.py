from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext

from application.models import Entry
from application.forms import AddUrlForm


def index(request):
    instance = False
    form = AddUrlForm()

    if request.method == 'POST':
        form = AddUrlForm(request.POST)

        if form.is_valid():
            instance = Entry.objects.filter(url=request.POST.get('url'))

            if not instance.exists():
                instance = form.save()
            else:
                instance = instance.first()  # Rework this!

    ctx = {
        'form': form,
        'instance': instance
    }
    return render_to_response('index.html', ctx,
                              context_instance=RequestContext(request))


def link(request, key):
    link_entry = get_object_or_404(Entry, key=key)
    return redirect(link_entry.url)


def settings(request, key):
    link_entry = get_object_or_404(Entry, key=key)

    ctx = {
        'link_entry': link_entry
    }

    return render_to_response('settings.html', ctx,
                              context_instance=RequestContext(request))
