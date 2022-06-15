from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template, render_to_string
from django.template import Context
from django.conf import settings
from app.models import SentEmails
from django.contrib import messages



# Create your views here.

def index(request):
  return render(request, 'index.html')


def dashboard(request):
  return render(request, 'dashboard/index.html')

def emails(request):
  if request.method == 'POST':
        """settings.EMAIL_HOST_USER= request.POST.get('from')
        settings.EMAIL_HOST_PASSWORD = request.POST.get('password')"""
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        # html_message = get_template(message)
        email_list = "vimalsahuweb@gmail.com"
        emails = ["vimalsahuweb@gmail.com", "lycostar4@gmail.com"]
        mail = SentEmails(subject=subject, message=message, emails=emails)
        mail.save()
        for i in range(len(emails)):
            email = emails[i]
            print(email)
            send_mail(subject, message, settings.EMAIL_HOST_USER,
                      [email], fail_silently=False) 

        messages.add_message(request, messages.INFO, 'Email Sent.')
 
  return render(request, 'dashboard/mail.html')

def email_template(request):
  return render(request, 'dashboard/etemp.html')

def sms(request):
  return render(request, 'dashboard/sms.html')

def loginUser(request):
    if request.method == 'POST':
   
        # AuthenticationForm_can_also_be_used__
   
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' wecome {username} !!')
            return redirect('/dashboard')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form':form, 'title':'log in'})
