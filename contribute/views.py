from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
  data = {}

  data["current_page"] = "contribute"

  return render(request, "contribute/index.html", data)