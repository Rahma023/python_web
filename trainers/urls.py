from django.urls import path
from .views import edit_trainers, register_trainers, trainers_profile
from .views import register_trainers, trainers_list
from django.conf.urls import url


urlpatterns=[
    path('register/',register_trainers,name='register_trainers'),
    path('list/',trainers_list,name='trainers_list'),
    path('profile/<int:id>/', trainers_profile, name="trainers_profile"),
    path('edit/<int:id>/', edit_trainers, name="edit_trainers"),
]