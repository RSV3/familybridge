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

  def contributors(self):
    return self.contribution_set.all()


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

  def feed_str(self):
    owner = self.expense.owner
    amount = self.expense.amount
    title = self.expense.title
    feed_str = "{0} spent ${1} on {2}.".format(owner.first_name, amount, title)
    return feed_str

  def contribute_str(self):
    contribute_str = "Contribute ${0} ({1}%)".format(self.amount, self.percentage)
    return contribute_str

  def contributed_exists(self):
    return self.expense.contribution_set.filter(contributed__isnull=False).exists()

  def contributed_users(self):
    return self.expense.contribution_set.filter(contributed__isnull=False)

  def requested_exists(self):
    return self.expense.contribution_set.filter(contributed__isnull=True).exists()

  def requested_users(self):
    """
      People who have been requested but not yet contributed
    """
    return self.expense.contribution_set.filter(contributed__isnull=True)
