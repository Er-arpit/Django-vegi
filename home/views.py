from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact , Checkout
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    # com={
    #     "variable":"this is First variable..!"
    # }
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

@login_required(login_url="login_page")
def contact(request):
    if request.method =="POST":
        name =request.POST.get('name') 
        phone =request.POST.get('phone')
        userid =request.POST.get('userid')
        email =request.POST.get('email')
        desc =request.POST.get('desc')
        contact=Contact(name=name,phone=phone,userid=userid,email=email,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, "your Message has being send.! ")

    return render(request,"contact.html")

@login_required(login_url="login_page")
def services(request):
    return render(request,"services.html")

def checkout(request):
    if request.method =="POST":
        fname =request.POST.get('fname') 
        lname =request.POST.get('lname')
        username =request.POST.get('username')
        email =request.POST.get('email')
        address =request.POST.get('address')
        address2 =request.POST.get('address2')
        country =request.POST.get('country')
        state =request.POST.get('state')
        zipp =request.POST.get('zipp')
        card_name =request.POST.get('card_name')
        card_no =request.POST.get('card_no')
        card_ex =request.POST.get('card_ex')
        card_cvv =request.POST.get('card_cvv')
        checkout=Checkout(fname=fname,lname=lname,username=username,email=email,address=address,address2=address2,country=country,state=state,zipp=zipp,card_name=card_name,card_no=card_no,card_ex=card_ex,card_cvv=card_cvv,date=datetime.today())
        checkout.save()
        messages.success(request, "your Address has been save ")

    return render(request,"checkout.html")

def registration(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user=User.objects.filter(username=username)
        if user.exists():
            messages.success(request, "this username already exists..! ")
            return redirect('/registration')

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        user.set_password(password)
        user.save()
        
        messages.success(request, "Account successfully created..! ")
        return redirect('/registration/')


    return render(request,"registration.html")

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.success(request, "invalid Username..! ")
            return redirect('/login_page')
        
        if (not username):
            messages.success(request, "Please enter username")
            return redirect('/login_page')

        user = authenticate(username = username , password = password)

        if user is None:
            messages.success(request, "invalid password..! ")
            return redirect('/login_page')
        else:
            login(request, user)
            return redirect('/')

    return render(request,"login.html")

def logout_page(request):
    logout(request)
    return redirect("/")