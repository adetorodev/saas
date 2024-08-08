
from django.contrib import admin
from django.urls import path
from .views import home_page, about_view

urlpatterns = [
    path("", home_page),
    path("home/", home_page),
    path("about/", about_view),
    path("admin/", admin.site.urls),
]
