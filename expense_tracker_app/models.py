from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):
    class Meta:
        verbose_name_plural = 'Expense'

    def __str__(self):
        return f"{self.user} - {self.name}"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    amount = models.PositiveIntegerField()
    category = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
