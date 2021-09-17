from django.conf.urls import include
from django.urls import path, include 
from rest_framework import routers, urlpatterns
from .views import StudentViewSet
from .views import TrainerViewSet
from .views import CourseViewSet
from .views import EventViewSet


router=routers.DefaultRouter()
router.register(r"students", StudentViewSet)
router.register(r"trainers", TrainerViewSet)
router.register(r"courses", CourseViewSet)
router.register(r"events", EventViewSet)


urlpatterns=[
    path("", include(router.urls)),
]