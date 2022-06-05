from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Agreements, Protocol
from .forms import AgreementsForm


@login_required
def index(request):
    docs = Agreements.objects.order_by("-reg_date")
    protocols = Protocol.objects.all
    return render(request, "index.html", {"docs": docs, "protocols": protocols})


@login_required
def add_agreem(request):
    if request.method == "POST":
        form = AgreementsForm(request.POST or None)
        if form.is_valid():
            link = form.save(commit=False)
            link.save()
            # form.save_m2m()
            return redirect("index")
    form = AgreementsForm()
    return render(request, "new_agr.html", {"form": form})
