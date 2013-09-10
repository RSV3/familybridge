from django.shortcuts import render
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import StreamingHttpResponse
from django.db.models import Sum
from django.forms.formsets import formset_factory

import json

from expense.models import Expense, Contribution
from core.models import EmailUser
from expense.forms import AddTeamMemberForm



# Create your views here.

@login_required
def index(request):
  """
    Shows the list/history of expenses

    Allow filter by month and by people 
  """ 
  data = {}

  data["current_page"] = "expense"

  data["expenses"] = Expense.objects.all()

  agg = Expense.objects.aggregate(total_expenses=Sum('amount'))
  data["total_expenses"] = agg['total_expenses']
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
def add_teammembers(request):
  """
    Shows view for adding team members and processes new teammember add
  """
  data = {}

  data["current_page"] = "home"

  AddTeamMemberFormset = formset_factory(AddTeamMemberForm, can_delete=True)
  data["teammember_formset"] = AddTeamMemberFormset()
  return render(request, "expense/add_contributors.html", data)

@login_required
def add_teammember_mixin(request):
  sub_data = {}
  data = {}

  u = request.user
  #users = EmailUser.objects.filter(groups__in=u.groups.all())
  new_form_id = int(request.GET['new_form_id'])
  sub_data["new_form_id"] = new_form_id
  data["teammember_form"] = render_to_string("expense/add_teammember_mixin.html", sub_data)
  data["result"] = 1
  return StreamingHttpResponse(json.dumps(data), content_type="application/json")

@login_required
def add_contributor_mixin(request):
  sub_data = {}
  data = {}

  u = request.user
  #users = EmailUser.objects.filter(groups__in=u.groups.all())
  users = EmailUser.objects.all()
  new_form_id = int(request.GET['new_form_id'])
  if new_form_id < users.count():
    sub_data["new_form_id"] = new_form_id
    sub_data["users"] = users
    data["contributor_form"] = render_to_string("expense/add_contributor_mixin.html", sub_data)
    data["result"] = 1
  else:
    data["result"] = 0
  return StreamingHttpResponse(json.dumps(data), content_type="application/json")

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


@login_required
def comment_on_feed(request):
  data = {}

  return StreamingHttpResponse(json.dumps(data), content_type="application/json") 

@login_required
def close_feed(request):
  data = {}

  return StreamingHttpResponse(json.dumps(data), content_type="application/json")

@login_required
def contribute(request):
  """
    @param contribution_id
    @param percentage: only if optional percentage
  """
  data = {}  

  return StreamingHttpResponse(json.dumps(data), content_type="application/json")

@login_required
def requested_contributions(request):

  data = {}

  u = request.user

  data["current_page"] = "contribute"

  # just top 4
  data["contributions"] = Contribution.objects.filter(contributor=u)[:4]
  return render(request, "expense/requested_contributions.html", data)

