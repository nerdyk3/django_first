from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^articles/([0-9]{4})/$' views.year_archive),
    url(r'^articles/([0-9]{4})/([0-9]{2})/$',views.month_archive),
    url(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$',views.article-detail),

]
