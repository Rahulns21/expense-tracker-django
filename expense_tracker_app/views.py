from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import *

@login_required
def index(request):
    if request.method == 'POST':
        expense = ExpenseForm(request.POST)
        if expense.is_valid():
            expense_instance = expense.save(commit=False)
            expense_instance.user = request.user
            expense.save()

    expense_form = ExpenseForm()
    context = {'expense_form': expense_form}
    return render(request, 'expense_tracker_app/index.html', context=context)