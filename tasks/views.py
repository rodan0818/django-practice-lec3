from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse


def index(request):
    if "tasks" not in request.session:
        request.session['tasks'] = []
    return render(request, 'tasks/index.html',
                  {"tasks": request.session['tasks']}
                  )


def add(request):
    if (request.method == "POST"):
        request.session['tasks'] += [request.POST['task']]
        return HttpResponseRedirect(reverse('tasks:index'))
    return render(request, 'tasks/add.html')
