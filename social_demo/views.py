from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView

from django.core.mail import send_mail


def home(request):
    return render(request,'home.html')

# class Home(TemplateView):
#     template_name = 'home.html'

