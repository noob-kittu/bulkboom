from django.db import models

# Create your models here.

class SentEmails(models.Model):
    subject = models.CharField(max_length=30)
    message = models.CharField(max_length=1030)
    emails = models.CharField(max_length=1030)