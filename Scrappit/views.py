from django.http import HttpResponse
from django.shortcuts import render
from service.models import service
from review.models import review
from django.shortcuts import redirect
from pickup.models import pickup

def homepage(request):
    return render(request,"main.html")
def about(request):
        
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")
def save_pickup(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone_no=request.POST.get('phone')
        address=request.POST.get('address')
        scrap_type=request.POST.get('service')
        date=request.POST.get('date')
        time=request.POST.get('time')
        en=pickup.objects.create(name=name,email=email,phone_no=phone_no,address=address,scrap_type=scrap_type,date=date,time=time)
        en.save()
    return render(request,"book.html")
def save_en(request):
    if request.method=="POST":
        Name=request.POST.get('name')
        Email=request.POST.get('email')
        phone_no=request.POST.get('tel')
        Subject=request.POST.get('subject')
        Message=request.POST.get('message')
        en=service.objects.create(name=Name,e_mail=Email,phone_no=phone_no,subject=Subject,message=Message)
        en.save() 
    return render(request,"contact.html")

def save_review(request):
    if request.method=="POST":
        name=request.POST.get('name')
        rating=request.POST.get('rating')
        Message=request.POST.get('message')
        en=review.objects.create(name=name,rating=rating,message=Message)
        en.save()
    return render(request,"feedback.html")
def educational_resourses(request):
    return render(request,"educational_resourses.html")
def scrap_price(request):
    return render(request,"scrap_price.html")
def scrrrap_points(request):
    return render(request,"scrrrap_points.html")

def feedback(request):
    return render(request,"feedback.html")
def book(request):
    return render(request,"book.html")

def course(request):
    return HttpResponse('welcome')
def coursedetails(request,abc):
    return HttpResponse(abc)
