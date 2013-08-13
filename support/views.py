from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.template import RequestContext
from premailer import transform

def email_render(request):

  data = {}

  data["title"] = "Welcome to Family Bridge"
  data["headline"] = "Welcome to Family Bridge"
  data["main_content"] = "You have registered with kwan@redstar.com, please verify"
  email_str = render_to_string("email/pink/mailer.html", context_instance=RequestContext(request, data))

  safe_email_str = transform(email_str)

  return HttpResponse(safe_email_str)
