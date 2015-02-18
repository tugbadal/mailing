# -*- coding: utf-8 -*-
from django.http import *
from app.models import GroupsCompany, Groups, Mail
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render, render_to_response
#from django.core.mail import send_mail, BadHeaderError
from django.core import mail
import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import Encoders
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart


def sending_mail(request):
    groups = Groups.objects.all()
    if request.method == "POST":
        list = []
        alici = request.POST.get('alici')
        grubu = request.POST.get('grubu')
        konu = request.POST.get('konu')
        icerik = request.POST.get('icerik')

        if alici:
            list.append(alici)
        if grubu:
            list = GroupsCompany.objects.filter(group_name=grubu)


        gonderen = "tugba.dal@bil.omu.edu.tr"
        password = 5444181110

        for kisi in list:
            alici = kisi.email
            x = Groups(id=kisi.id)
            #print x
            if konu and icerik:
                mymail = Mail(groups_company=x, sender_username=gonderen, receiver_username=alici, mail_title=konu, mail_content=icerik)
                mymail.save()
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.ehlo()
                server.starttls()
                server.login(gonderen, password)
                a = MIMEMultipart()
                a = MIMEText(icerik, 'html', 'utf-8')
                a['From'] = gonderen
                a['Subject'] = konu
                a['To'] = alici
                a = a.as_string()
                try:
                    server.sendmail(gonderen, alici, a)
                    print "basarili"
                except:
                    print "basarisiz"
                server.quit()
        return HttpResponseRedirect('/gap_gonderilen_mailler/')
    else:
        return render_to_response('app/create_e_posta.html', locals(), context_instance=RequestContext(request))

def mailbox(request):
    return render(request, 'app/mailbox.html')

def mailcontent(request):
    mailID = request.GET["id"]
    if mailID:
        try:
            mail = Mail.objects.get(id=mailID)
            return render_to_response("app/m")
        except:
            return HttpResponse(u'aradığınız mail bulunamadı')



def gap_sended_mail(request):
    if "process" in request.GET.keys():
        if request.GET["process"] == "delete":
            return mailcontent(request)
    sendedmails = Mail.objects.all()

    return render_to_response('app/gap_sended_mails.html', locals())


def mail_list(request):
    if "process" in request.GET.keys():
        if request.GET["process"] == "delete":
            return mail_delete(request)
    emails = GroupsCompany.objects.all()
    return render_to_response('app/mail_list.html', locals())
def gap_mail_list(request):
    if "process" in request.GET.keys():
        if request.GET["process"] == "delete":
            return mail_delete(request)
    gap_emails = GroupsCompany.objects.filter(group_name="GAP Bilisim")
    return render_to_response('app/gapmail_list.html', locals())

def propars_mail_list(request):
    if "process" in request.GET.keys():
        if request.GET["process"] == "delete":
            return mail_delete(request)
    propars_emails = GroupsCompany.objects.filter(group_name="PROPARS")
    return render_to_response('app/propars_mail_list.html', locals())

def efatura_mail_list(request):
    if "process" in request.GET.keys():
        if request.GET["process"] == "delete":
            return mail_delete(request)
    efatura_emails = GroupsCompany.objects.filter(group_name="E-Fatura")
    return render_to_response('app/efatura_mail_list.html', locals())

def edefter_mail_list(request):
    if "process" in request.GET.keys():
        if request.GET["process"] == "delete":
            return mail_delete(request)
    edefter_emails = GroupsCompany.objects.filter(group_name="E-Defter")
    return render_to_response('app/edefter_mail_list.html', locals())

def mail_delete(request):
    mailID = request.GET["id"]
    if mailID:
        try:
            mail = GroupsCompany.objects.get(id=mailID)
        except:
            return HttpResponse(u'aradığınız mail adresi bulunamadı')
        if mail in GroupsCompany.objects.filter(group_name="GAP Bilisim"):
            mail.delete()
            return HttpResponseRedirect('/gap_maillerin_listesi/')
        if mail in GroupsCompany.objects.filter(group_name="PROPARS"):
            mail.delete()
            return HttpResponseRedirect('/propars_maillerin_listesi/')
        if mail in GroupsCompany.objects.filter(group_name="E-Fatura"):
            mail.delete()
            return HttpResponseRedirect('/efatura_maillerin_listesi/')
        if mail in GroupsCompany.objects.filter(group_name="E-Defter"):
            mail.delete()
            return HttpResponseRedirect('/edefter_maillerin_listesi/')


def deneme(request):
    return render(request, 'app/denem.html')

def mailekle(request):
    groups = Groups.objects.all()
    if request.method == 'POST':
        adi = request.POST.get('adi')
        maili = request.POST.get('maili')
        grubu = request.POST.get('grubu')

        record = GroupsCompany(group_name=grubu, company_name=adi, email=maili)
        record.save()
        if record.group_name == "GAP Bilisim" :
            return HttpResponseRedirect('/gap_maillerin_listesi/')
        if record.group_name == "PROPARS":
            return HttpResponseRedirect('/propars_maillerin_listesi/')
        if record.group_name == "E-Fatura":
            return HttpResponseRedirect('/efatura_maillerin_listesi/')
        if record.group_name == "E-Defter":
            return HttpResponseRedirect('/edefter_maillerin_listesi/')
    else:
        return render_to_response('app/add_eposta.html', locals(), context_instance=RequestContext(request))


# Create your views here.
