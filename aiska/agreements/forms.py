from django.forms import ModelForm
from .models import Agreements
# from django_select2.forms import Select2Widget, Select2MultipleWidget

class AgreementsForm(ModelForm):
    class Meta:
            model = Agreements
            fields = ['foiv_id', 'title', 'number', 'reg_date', 'inv_number', 'subject', 'departments', 'note', 'file',]