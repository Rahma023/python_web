from course.views import course_list
from django.urls import path
from .views import register_event
from .views import register_event, events_list
from django.conf.urls import url



urlpatterns=[
    path('register/',register_event,name='register_event'),
    path('list/',events_list,name='events_list'),
]