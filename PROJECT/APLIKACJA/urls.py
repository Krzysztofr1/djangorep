from django.urls import path
from .views import viewszhtml, viewszid

urlpatterns = [
    path("strona/",viewszhtml),
    path("strona/<int:id>/", viewszid)
]
