from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import *
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
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
    if(request.method=='POST'):
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        message=request.POST.get('message')
        Contact.objects.create(
            name=name,
            phone=phone,
            email=email,
            message=message
        )
        mail=f'''
        {name} 
        with
        {email} 
        and
        {phone} 
        sent 
        "{message}"
        '''
        send_mail(name,mail,'',['vystudent68@gmail.com'])
        return HttpResponseRedirect(request.path_info)

    return render(request,'contact.html')

@user_passes_test(is_admin)
def adminpanel(request):
    return render(request,'admin.html')

@user_passes_test(is_admin)
def quotation(request):
    categorys=Machine_category.objects.all
    context={"categorys":categorys}
    return render(request,'quotation.html',context)

@user_passes_test(is_admin)
def performa(request):
    return render(request,'performa.html')