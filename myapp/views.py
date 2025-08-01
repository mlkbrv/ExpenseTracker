from django.db.models import Sum
from django.shortcuts import render, redirect
from .forms import ExpenseForm
from .models import Expense
import datetime

def index(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=ExpenseForm()
    expenses = Expense.objects.all()
    total_expenses = expenses.aggregate(Sum('amount'))

    last_year = datetime.date.today() - datetime.timedelta(days = 365)
    year_data = Expense.objects.filter(date__gte=last_year)
    yearly_sum = year_data.aggregate(Sum('amount'))

    last_month = datetime.date.today() - datetime.timedelta(days=30)
    month_data = Expense.objects.filter(date__gte=last_month)
    month_sum = month_data.aggregate(Sum('amount'))

    last_week = datetime.date.today() - datetime.timedelta(days=7)
    week_data = Expense.objects.filter(date__gte=last_week)
    week_sum = week_data.aggregate(Sum('amount'))

    daily_sums = Expense.objects.filter().values('date').order_by('date').annotate(Sum('amount'))

    categorical_sums = Expense.objects.filter().values('category').order_by('category').annotate(Sum('amount'))

    return render(request, 'myapp/index.html', {'form':form, 'expenses':expenses, 'total_expenses':total_expenses,'yearly_sum':yearly_sum, 'month_sum':month_sum, 'week_sum':week_sum,'daily_sums':daily_sums, 'categorical_sums':categorical_sums})

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

def delete(request, id):
    if request.method == "POST" and 'delete' in request.POST:
        expense = Expense.objects.get(id=id)
        expense.delete()
    return redirect('index')