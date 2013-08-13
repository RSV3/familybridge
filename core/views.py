from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
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
    return HttpResponseRedirect(reverse('core:home'))

  # if didn't login, return error
  auth_form = TopLoginForm()
  data["form"] = auth_form
  data["signup_form"] = signup_form
  data["next"] = reverse("core:home")
  return render(request, "core/index.html", data)


@login_required
def home(request):

  data = {}

  data["current_page"] = "home"

  return render(request, "core/home.html", data)


@login_required
def profile(request):

  data = {}

  return render(request, "core/profile.html", data)


def about(request):

  data = {}

  data["current_page"] = "about"

  return render(request, "core/about.html", data)


