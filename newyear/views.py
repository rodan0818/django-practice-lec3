from django.shortcuts import render
from datetime import date, datetime


def index(request):
    now = datetime.now()
    return render(request, "newyear/index.html", {
        "newyear": now.day == 1 and now.month == 1
    })
