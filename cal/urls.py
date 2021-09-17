from django.conf.urls import url
from . import views

app_name = 'cal'
urlpatterns = [
    url('calendar/',views.CalendarView.as_view(),name='calendar'),
    url('forms/', views.event, name='event_form'),
]