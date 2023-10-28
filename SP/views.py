from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import *


def is_admin(user):
    return user.is_authenticated and user.is_staff


def not_found(request,exception):
    return render(request,'404.html')

def index(request):
    return render(request,'index.html')
def products(request):
    categorys=Machine_category.objects.all
    context={"categorys":categorys}
    return render(request,'products.html',context)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

@user_passes_test(is_admin)
def adminpanel(request):
    return render(request,'admin.html')

@user_passes_test(is_admin)
def quotation(request):
    return render(request,'quotation.html')

@user_passes_test(is_admin)
def performa(request):
    return render(request,'performa.html')