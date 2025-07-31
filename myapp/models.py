from django.db import models

class Expense(models.Model):
    name = models.CharField()
    amount = models.IntegerField()
    category = models.CharField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name