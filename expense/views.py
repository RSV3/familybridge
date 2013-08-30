from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
  data = {}

  data["current_page"] = "expense"

  return render(request, "expense/index.html", data)

@login_required
def contributions(request):
  data = {}

  data["current_page"] = "contribute"

  return render(request, "expense/contributions.html", data)

@login_required
def add_expense(request):
  data = {}

  data["current_page"] = "expense"
  return render(request, "expense/index.html", data)

@login_required
def add_contributors(request):
  data = {}

  data["current_page"] = "expense"
  return render(request, "expense/add_contributors.html", data)


@login_required
def add_bank_card(request):
  data = {}

  data["current_page"] = "expense"
  return render(request, "expense/add_bank_card.html", data)


@login_required
def add_multiple_expenses(request):
  data = {}

  data["current_page"] = "expense"
  return render(request, "expense/add_multiple_expenses.html", data)


