"""
URL configuration for companySite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from SP import views
from django.conf.urls.static import static
from django.conf import settings

# import SP.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('SP.urls')),
    path('products',views.products,name="views"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('adminpanel',views.adminpanel,name="adminpanel"),
    path('quotation',views.quotation,name="quotation"),
    path('performa',views.performa,name="performa"),
]
handler404=views.not_found
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)