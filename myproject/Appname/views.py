import random

from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect, render
import mysql.connector as sql

from .models import LoginTable


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Replace these with your actual user validation logic


    return render(request, 'Login.html')

def dashboard(request):
    return render(request, 'Dashboard.html')

def sign(request):
    return render(request, 'SignUp.html')


def forget(request):
    return render(request, 'ForgotPass.html')
def Mainpage(request):
    return render(request,'MainPage.html')
def Location(request):
    return render(request,'Location.html')
def Cart(request):
    return render(request,'cart.html')
def AddToCart(request):
    return render(request,'AddToCart.html')
def Groceries(request):
    return render(request,'Groceries.html')
def Electronics(request):
    return render(request,'ElectronicDevices.html')
def Clothes(request):
    return render(request,'Clothes.html')
def Books(r):
    return render(r,'Books.html')
def Admin(r):
    return render(r,'Admin.html')
def Payment(t):
    return render(t,'Payment.html')
def AdminLogin(r):
    return render(r,'AdminLogin.html')
def NetworkBank(request):
    return render(request,'NetworkBanking.html')
def Aboutus(request):
    return render(request,'AboutUs.html')

def checklogin(request):
    if request.method == "POST":
        uname = request.POST["username"]
        pwd = request.POST["password"]
        flag = Admin.objects.filter(username=uname,password=pwd).values()  # replace 'User' with your model name
        if flag:
            return render(request,"Dashboard.html")
        else:
            return render(request,"loginfail.html")



def OTP(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        otp = ""
        for _ in range(4):
            otp += str(random.randint(0, 9))
        comment = "Welcome to KL Stores. Thanks for visiting our KL Stores. This is your OTP:"
        comment1 = comment + otp
        send_mail(
            "OTP for KL Stores",
            comment1,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False
        )

        # Storing OTP in session



    return render(request, "OTPVerification.html")

from django.shortcuts import render

def validateOTP(request):
    if request.method == 'POST':
        OTP = request.POST.get('OTP')
        OTP_length = len(OTP)
        valid_OTPs = ['2005', '1234', '5467', '7890']

        if OTP  in valid_OTPs or OTP_length != 4:
            return render(request, 'OTPVerification.html')
        else:
            return render(request, 'Dashboard.html')
    else:
        return render(request, 'Dashboard.html')



def verify(request):
    return  render(request,'OTPVerification.html')



