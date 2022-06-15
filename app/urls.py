
from django.urls import path
#now import the views.py file into this code
from . import views
urlpatterns=[
  path('',views.index),
  path('dashboard/',views.dashboard),
  path('dashboard/email',views.emails),
  path('dashboard/etemplate',views.email_template),
  path('dashboard/sms',views.sms),
  path('login/',views.loginUser)
]