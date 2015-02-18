from django.db import models


class Userss(models.Model):
    user_name = models.CharField(max_length=125)
    e_mail = models.EmailField()
    password = models.CharField(max_length=125)

class Groups(models.Model):
    group_name = models.CharField(max_length=120)

class GroupsCompany(models.Model):
    group_name = models.CharField(max_length=500, blank=True, null=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()

class Mail(models.Model):
    groups_company = models.ForeignKey(Groups)
    sender_username = models.CharField(max_length=125)
    receiver_username = models.CharField(max_length=125)
    mail_dateclock = models.DateTimeField(blank=True, null=True)
    delete_time = models.DateTimeField(blank=True, null=True)
    mail_content = models.TextField(max_length=100000000, blank=True, null=True)
    mail_status = models.BooleanField(max_length=255, default=False)
    mail_title = models.CharField(max_length=255, blank=True, null=True)
    isdeleted = models.BooleanField(default=False)





# Create your models here.
