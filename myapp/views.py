from django.shortcuts import render, redirect
from .forms import ExpenseForm
from .models import Expense

def index(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=ExpenseForm()
    expenses = Expense.objects.all()
    return render(request, 'myapp/index.html', {'form':form, 'expenses':expenses})

def edit(request, id):
    expense = Expense.objects.get(id=id)
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ExpenseForm(instance=expense)
    return render(request,'myapp/edit.html',{'form':form})