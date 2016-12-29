from django.conf.urls import url
from django.contrib import admin
from .views import get_content,post_content


urlpatterns = [
url(r'^getinfo/',get_content),
url(r'^postcontent/',post_content)
]