from django.urls import path
from .views import course_list, register_course, edit_course,course_update
from django.conf.urls import url


urlpatterns=[
    path('register/',register_course,name='register_course'),
    path('list/',course_list,name='course_list'),
    path('update/<int:id>/',course_update,name='course_update'),
    path('edit/<int:id>/',edit_course,name='edit_course'),
]