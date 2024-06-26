# events/urls.py
from django.urls import re_path
from . import views

app_name = 'mycalendary'

urlpatterns = [
    re_path(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
    re_path(r'^event/new/$', views.event, name='event_new'),
    re_path(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
]