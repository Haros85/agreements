from django.shortcuts import render
from .models import Agreements, Protocol


def index(request):
    docs = Agreements.objects.order_by("-reg_date")
    protocols = Protocol.objects.all
    return render(request, "index.html", {"docs": docs, "protocols": protocols})
