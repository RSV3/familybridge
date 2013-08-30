from django.db import models
from django.conf import settings


class Expense(models.Model):
  owner = models.ForeignKey(settings.AUTH_USER_MODEL)
  title = models.CharField(max_length=64)
  description = models.CharField(max_length=256, blank=True, null=True)
  amount = models.DecimalField(max_digits=16, decimal_places=2)

  CATEGORY_CHOICES = (
    (0, 'Living Expense'),
    (1, 'Housing'),
    (2, 'Food'),
    (3, 'Medication'),
    (4, 'Health'),
    (5, 'Recreation'),
    (6, 'Other'),
  )

  category = models.IntegerField(choices=CATEGORY_CHOICES)
  date = models.DateField()
  contribution_requested = models.BooleanField(default=False)

  timestamp = models.DateTimeField(auto_now_add=True)  
  updated = models.DateTimeField(auto_now=True)


class Contribution(models.Model):
  contributor = models.ForeignKey(settings.AUTH_USER_MODEL)
  expense = models.ForeignKey(Expense)
  percentage = models.IntegerField(default=0)
  # for easy calculation without joining
  amount = models.DecimalField(max_digits=16, decimal_places=2)

  # if the user confirmed contribution
  contributed = models.DateTimeField(blank=True, null=True)
  # if the user was reminded to contribute
  last_reminded = models.DateTimeField(blank=True, null=True)
  # if payment has been fully reconciled
  reconciled = models.DateTimeField(blank=True, null=True)

  timestamp = models.DateTimeField(auto_now_add=True)  
  updated = models.DateTimeField(auto_now=True)

  def update_contribution(self):
    self.amount = self.expense.amount * float(percentage) / 100.0
    self.save()
