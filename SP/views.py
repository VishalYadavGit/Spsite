from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import *
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.shortcuts import redirect

def not_found(request,exception):
    return render(request,'404.html')

def footerdata():
    data = {
        'categorys': Machine_category.objects.all,
    }
    return data

def index(request):
    categorys = Machine_category.objects.all
    images = Carousel.objects.all
    context = {
        'categorys': categorys, 'images': images
    }
    return render(request,'index.html',context)

def products(request):
    categorys=Machine_category.objects.all
    context={"categorys":categorys}
    return render(request,'products.html',context)

def category(request,id):
    category=Machine_category.objects.get(id=id)
    categorys=Machine_category.objects.all
    machines = Machine.objects.filter(category=category)
    print(machines)
    context={"category":machines,"categorys":categorys}
    return render(request,'category.html',context)

def product(request,id):
    machine=Machine.objects.get(id=id)
    related_machines = Machine.objects.filter(category=machine.category).exclude(id=id)
    categorys=Machine_category.objects.all
    print(related_machines)
    context={"machine":machine,"related_machines":related_machines,"categorys":categorys}
    return render(request,'product.html',context)


def about(request):
    categorys=Machine_category.objects.all
    return render(request,'about.html',{"categorys":categorys})

def contact(request):
    if(request.method=='POST'):
        name=request.POST.get('name')
        option=request.POST.get('quote')
        if not option:
            option="General Enquiry"
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        message=request.POST.get('message')
        Contact.objects.create(
            name=name,
            phone=phone,
            email=email,
            message=message,
            enquiry=option
        )
        mail=f'''
        {name} 
        with
        {email} 
        and
        {phone} 
        sent 
        "{message}"
        enquiry type is {option}
        '''
        send_mail(name,mail,'',['vystudent68@gmail.com'])
        return HttpResponseRedirect(request.path_info)

    qna = faq.objects.all
    products = Machine.objects.all
    categorys=Machine_category.objects.all
    context={"faq":qna,"products":products,"categorys":categorys}
    return render(request,'contact.html',context)

def get_quote(request,id):
    machine=Machine.objects.get(id=id)
    return redirect(f'/contact/?machine_id={machine.id}')

def terms(request):
    categorys=Machine_category.objects.all
    return render(request,'terms.html',{"categorys":categorys})

def privacy(request):
    categorys=Machine_category.objects.all
    return render(request,'privacy.html',{"categorys":categorys})