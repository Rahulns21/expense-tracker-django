from django.forms import ModelForm
from .models import *

class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = ('name', 'amount', 'category')