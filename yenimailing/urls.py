from django.conf.urls import patterns, include, url

import app.views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'yenimailing.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^eposta_olustur/', app.views.sending_mail),
    url(r'^gap_gelen_kutusu/', app.views.mailbox),
    url(r'^mailcontent/', app.views.mailcontent),
    url(r'^mailekle/', app.views.mailekle),
    url(r'^maillerin_listesi/', app.views.mail_list),
    url(r'^gap_maillerin_listesi/', app.views.gap_mail_list),
    url(r'^gap_gonderilen_mailler/', app.views.gap_sended_mail),
    url(r'^propars_maillerin_listesi/', app.views.propars_mail_list),
    url(r'^efatura_maillerin_listesi/', app.views.efatura_mail_list),
    url(r'^edefter_maillerin_listesi/', app.views.edefter_mail_list),

    url(r'^deneme/', app.views.deneme),

)
