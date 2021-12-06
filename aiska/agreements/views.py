from django.shortcuts import render
from .models import Agreements


def index(request):
    qs = Agreements.objects.order_by("-reg_date")[:2]
    return render(request, "index.html", {"docs": qs})
