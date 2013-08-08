from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from core.forms import UserCreationForm


def index(request):

  data = {}
  data["form"] = AuthenticationForm()
  data["signup_form"] = UserCreationForm()
  data["next"] = reverse("index")
  return render(request, "core/index.html", data)


def sign_up(request):

  data = {}

  # login and redirect to homepage
  form = UserCreationForm(request.POST or None)
  if form.is_valid():
    form.save()
    user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password1'])
    login(request, user)
    return HttpResponseRedirect(reverse('index'))

  # if didn't login, return error
  data["form"] = AuthenticationForm()
  data["signup_form"] = form
  data["next"] = reverse("index")
  return render(request, "core/index.html", data)

