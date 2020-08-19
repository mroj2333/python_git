from django.conf.urls import url
from . import views

urlurlpatterns = [
    url(r'^login/$', views.LoginView.as_view()),

    ]