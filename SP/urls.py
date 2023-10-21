from django.contrib import admin
from django.urls import path,include
from SP import views
# import SP.urls

urlpatterns = [
    path('',views.index)
]
