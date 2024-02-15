from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("location/<int:location_id>", views.location_detail, name="location_detail")
]