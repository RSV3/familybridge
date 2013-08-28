from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib import messages

from core.forms import TopLoginForm, FrontSignUpForm


def index(request):

  data = {}

  if request.user.is_authenticated():
    return HttpResponseRedirect(reverse('core:home'))

  auth_form = TopLoginForm()
  data["form"] = auth_form

  signup_form = FrontSignUpForm()
  data["signup_form"] = signup_form

  data["next"] = reverse("core:home")
  return render(request, "core/index.html", data)


def sign_up(request):

  data = {}

  # login and redirect to homepage
  signup_form = FrontSignUpForm(request.POST or None)
  if signup_form.is_valid():
    signup_form.save()
    user = authenticate(username=signup_form.cleaned_data['email'], password=signup_form.cleaned_data['password1'])
    login(request, user)

    # create a default group
    import uuid
    random_str = str(uuid.uuid4())
    default_group = Group(name="cg_{0}_{1}_{2}".format(user.first_name, user.last_name, random_str ))
    default_group.save()
    user.groups.add(default_group)
    return HttpResponseRedirect(reverse('core:home'))

  # if didn't login, return error
  auth_form = TopLoginForm()
  data["form"] = auth_form
  data["signup_form"] = signup_form
  data["next"] = reverse("core:home")
  return render(request, "core/index.html", data)


@login_required
def home(request, group_id=None):
  """
    Show dashboard of a particular care group with group_id or default group
  """
  data = {}

  data["current_page"] = "home"

  u = request.user

  # displays dashboard
  active_group = None
  group_owner = False
  if group_id:
    active_group = Group.objects.get(id=group_id)
    group_owner = True if active_group in u.groups.all() else False
    if not group_owner:
      # check if you are a member of the group or not
      if active_group not in u.member_groups.all():
        raise Http404 
  else:
    active_group = u.groups.all()[0]
    if active_group:
      group_owner = True
    else:
      # there's no owned group so it will display a group they are member of
      active_group = u.member_groups.all()[0]
      group_owner = False
  data["group_owner"] = group_owner
  data["active_group"] = active_group

  return render(request, "core/home.html", data)

@login_required
def invite_team_members(request):
  """
    Display a form to invite team members
    List of first name, last name, email, phone (optional)

    TODO: use formsets

    When submitted successfully, it adds a message and go to dashboard
  """

  data = {}

  list_of_invitees = "hello@example.com"

  messages.success("Successfully invited %s" % list_of_invitees)

  return render(request, "core/invite_team_members.html", data)

@login_required
def add_expense(request):
  """
    Shows form to add expense, upload receipt

    Saves expense and redirects to the history page
  """

  data = {}



  return render(request, "core/add_expense.html", data)

@login_required
def expenses(request):
  """
    Shows the list/history of expenses

    Allow filter by month and by people 
  """

  data = {}

  return render(request, "core/expenses.html", data)

@login_required
def payments(request):
  """
    Show list of payments that one owes and list of payments that one has received

    It should also show any payments one has made
  """

  data = {}

  return render(request, "core/payments.html", data)

@login_required
def mark_paid(request, payment_id):
  """
    After a user has paid their team member, they click confirm/log payment  
  """

  data = {}

  # need to verify this is something that they owe

  return render(request, "core/payments.html", data)


@login_required
def profile(request):

  data = {}

  return render(request, "core/profile.html", data)

@login_required
def change_group_name(request, group_id):

  data = {}
  u = request.user

  if u.groups.filter(id=group_id).exists():
    # user is owner to modify the group
    g = Group.objects.get(id=group_id)

    g.name = request.POST['group_name']
    g.save()

  return render(request, "core/home.html", data)

def about(request):

  data = {}

  data["current_page"] = "about"

  return render(request, "core/about.html", data)


