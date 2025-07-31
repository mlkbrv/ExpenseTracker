from django.shortcuts import render
from .forms import ExpenseForm
def index(request):
    form=ExpenseForm()
    return render(request, 'myapp/index.html', {'form':form})