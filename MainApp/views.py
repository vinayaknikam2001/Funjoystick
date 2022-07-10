from decimal import Context
from unittest import result
from django.http import response
from django.shortcuts import render,redirect
from django.http.response import Http404, HttpResponse
#for database importing user
from django.contrib.auth.models import User
#for sending user meassages
from django.contrib import messages
#importing authentication inbuilt function
from django.contrib.auth import authenticate,login,logout
from django.urls import conf
from FunJoystick import settings
#for sending e-mail
from django.core.mail import send_mail
#for confirmation e-mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from . tokens import generate_token
from django.core.mail import EmailMessage,send_mail
from .models import Contact, Game, Playgame
import os

def home(request):
    return render(request, 'home.html')

def signup(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if (User.objects.filter(username=username)):
            messages.error(request, 'This Username is already taken!')
            return redirect('signup')
        
        if (User.objects.filter(email=email)):
            messages.error(request, 'E-mail is already registered!')
            return redirect('signup')
        
        if (len(username)>15):
            messages.error(request, 'Username must be under 15 characters!')
            return redirect('signup')
        
        if (pass1!=pass2):
            messages.error(request, 'Passwords did not match!')
            return redirect('signup')

        if(not username.isalnum()):
            messages.error(request, 'Username must be alpha-numeric')
            return redirect('signup')

        #Creating new user in database
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        
        #Saving user in database
        myuser.is_active = False
        myuser.save()
        messages.success(request, 'Your accout has been successfully created. We have sent you confirmation email, please confirm your email')


        #Welcome e-mail
        subject = 'Welcome to FunJoystick.com'
        msg = 'Hello '+myuser.first_name+'!\nWelcome to FunJoystick.com you can enjoy variety of games here.\nThank you for visiting.\n Happy Gaming !'
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, msg, from_email, to_list, fail_silently=True)


        #Confirmation e-mail
        current_site = get_current_site(request)
        sub = 'Confirm your e-mail @ FunJoystick.com! '
        msg2 = render_to_string('confirmation_email.html',{
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser),
        })
        email = EmailMessage(
            sub,
            msg2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )
        email.fail_silently = True
        email.send()

        return redirect('signin')
        
    return render(request, 'signup.html')


def signin(request):

    if(request.method == 'POST'):
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if(user is not None):
            login(request, user)
            fname = user.first_name 
            return render(request, 'home.html',{'fname': fname})
        else:
            messages.error(request, 'Wrong credentials !')
            return redirect('signin')
    return render(request, 'signin.html')


def signout(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('home')


def activate(request, uidb64, token):

    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        return redirect('home')
    else:
        return render(request, 'activation_failed.html')


def contact(request):

    if(request.method == 'POST'):
        name = request.POST['first_name']
        phone = request.POST['phone']
        mail = request.POST['email']
        query = request.POST['query']

        con_obj = Contact(name=name, phone=phone, email=mail, query=query)
        con_obj.save()
        messages.success(request, 'Thank you for sharing your feedback!')
        return redirect('response')


    return render(request, 'contact.html')

def response(request):
    return render(request,'response.html')


def downloads(request):
    context = {'file':Game.objects.all()}
    return render(request,'download.html',context)

def download(request,path):
    file_path=os.path.join(settings.MEDIA_ROOT,path)
    if(os.path.exists(file_path)):
        with open(file_path,'rb') as fh:
            response=HttpResponse(fh.read(),content_type="applicaion/adminupload")
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return 
    raise Http404

def searchDownloads(request):
    query = request.GET['search']
    allGames = Game.objects.filter(title__icontains=query)
    result = {'file' : allGames}
    return render(request,'searchDownloads.html',result)

def playgames(request):
    games = {'file' :Playgame.objects.all()}
    return render(request,'playgames.html',games)

def searchGames(request):
    query = request.GET['search']
    allGames = Playgame.objects.filter(name__icontains=query)
    result = {'file' : allGames}
    return render(request,'search.html',result)

#Game functions 
def snake(request):
    return render(request,'Snake_Mania.html')

def startFall(request):
    return render(request,'Start_Fall.html')

def fallBall(request):
    return render(request,'Fall_Ball.html')

def ticTacToe(request):
    return render(request,'TicTacToe.html')

def CPU(request):
    return render(request,'CPU.html')

def flappyBird(request):
    return render(request,'Flappy_Bird.html')

def robot(request):
    return render(request,'Robot.html')

def robot2(request):
    return render(request,'Robot2.html')