from django.shortcuts import render


def index(request, name):
    return render(request, "hello/index.html", {
        "name": name.capitalize()
    })
