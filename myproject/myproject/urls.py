
from django.contrib import admin
from django.urls import path
from .views import home_page_view , about_view


urlpatterns = [
    path("" , home_page_view),
    path("about/",about_view),
    path("hello-world/",home_page_view),
    path("admin/", admin.site.urls),
]