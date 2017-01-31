"""testDjango2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
#from testDjango2.views import hello, current_datetime, hours_ahead, testnavpage, display_meta, contact
#from books import views
from . import views
from django.conf import settings


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.review_form),
    url(r'^review-form/$', views.review_form),
    url(r'^sentiment-form/$', views.sentiment_form),
    url(r'^forward-sentiment/$', views.forward_sentiment),
    url(r'^thanks/$', views.thanks),
#    url(r'^time/$', views.current_datetime),
#    url(r'^another-time-page/$', views.current_datetime),
#    url(r'^time/plus/(\d{1,2})/$', views.hours_ahead),
#    url(r'^testnavpage/$', views.testnavpage),
#    url(r'^getmeta/$', views.display_meta),
#    url(r'^search/$', views.views.search),
#    url(r'^contact/$', views.contact),

#    url(r'^reviews/2003/$', views.special_case_2003),
#    url(r'^reviews/([0-9]{4})/$', views.year_archive),
#    url(r'^reviews/([0-9]{4})/([0-9]{2})/$', views.month_archive),
#    url(r'^reviews/([0-9]{4})/([0-9]{2})/([0-9]+)/$', views.review_detail),

#    url(r'^reviews/2003/$', views.special_case_2003),
#    url(r'^reviews/(?P<year>[0-9]{4})/$', views.year_archive),
#    url(r'^reviews/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive),
#    url(r'^reviews/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', views.review_detail),

#    url(r'^reviews/$', views.page),
#    url(r'^reviews/page(?P<num>[0-9]+)/$', views.page),

]

